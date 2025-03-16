import asyncio
import os
import logging
import re
import requests
from datetime import datetime
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor
from pyrogram import Client
from motor.motor_asyncio import AsyncIOMotorClient
import cloudscraper

# Ensure event loop policy is set correctly for Python 3.13+
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

executor = ThreadPoolExecutor()
os.makedirs("downloads", exist_ok=True)

User = Client(
    "User", session_string=USER_SESSION_STRING, api_hash=API_HASH, api_id=API_ID
)

LeoTG = Client("HeartxBotz", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Fetch with CloudScraper to bypass Cloudflare protection
async def fetch(url):
    scraper = cloudscraper.create_scraper()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    }

    loop = asyncio.get_event_loop()
    try:
        response = await loop.run_in_executor(
            executor, lambda: scraper.get(url, headers=headers)
        )
        response.raise_for_status()
        return response, int(response.headers.get("Content-Length", 0))
    except Exception as e:
        logging.error(f"Error fetching {url}: {str(e)}")
        return None, 0

async def is_valid_link(url):
    response, _ = await fetch(url)
    return response is not None and response.status_code == 200

async def download_file(url, local_filename):
    logging.info(f"Starting download: {url}")
    max_retries = 5
    for attempt in range(max_retries):
        try:
            response, expected_size = await fetch(url)
            if response:
                with open(local_filename, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)

                actual_size = os.path.getsize(local_filename)
                if actual_size == expected_size:
                    logging.info(f"Downloaded {local_filename} successfully.")
                    return True
                else:
                    logging.error(f"File size mismatch: Expected {expected_size}, got {actual_size}")
                    os.remove(local_filename)
            else:
                logging.error(f"Failed to fetch {url}. Attempt {attempt + 1}/{max_retries}.")

        except Exception as e:
            logging.error(f"Download failed for {url}: {e}. Attempt {attempt + 1}/{max_retries}.")

        await asyncio.sleep(1)

    logging.error(f"Failed to download file after {max_retries} attempts.")
    return False

async def send_new_link_notification(links):
    async with LeoTG:
        logging.info(f"Sending new links: {links}")
        if not links:
            await User.send_message(chat_id=GROUP_ID, text="Empty Array")
            return

        for link in links:
            logging.info(f"Processing link: {link}")
            local_filename = f"downloads/HeartXBotz {link['name']}.torrent"

            if await is_valid_link(link["link"]):
                if await download_file(link["link"], local_filename):
                    try:
                        logging.info(f"Uploading {local_filename} to Telegram...")
                        sent_msg = await LeoTG.send_document(
                            chat_id=GROUP_ID,
                            document=local_filename,
                            thumb="database/thumb.jpeg",
                            caption=f"""
<b>@HeartXBotz {link['name']}

<blockquote>〽️ Powered by @HeartXBotz</blockquote></b>""",
                        )

                        logging.info(f"Sent document ID: {sent_msg.id}")

                        await LeoTG.send_message(
                            chat_id=GROUP_ID,
                            text="/qbleech1",
                            reply_to_message_id=sent_msg.id,
                        )

                        sent_msg = await LeoTG.send_document(
                            chat_id=RSS_CHAT,
                            document=local_filename,
                            thumb="database/thumb.jpeg",
                            caption=f"""
<b>@HeartXBotz {link['name']}

<blockquote>〽️ Powered by @HeartXBotz</blockquote></b>""",
                        )
                    except Exception as e:
                        logging.error(f"Failed to send document for link {link['link']}: {e}")
                    finally:
                        if os.path.exists(local_filename):
                            os.remove(local_filename)
                else:
                    logging.warning(f"Failed to download file for link: {link['link']}")
            else:
                logging.warning(f"Invalid link: {link['link']}")

# Database Management
class Database:
    def __init__(self, url, db_name):
        self.db = AsyncIOMotorClient(url)[db_name]
        self.users_coll = self.db.users
        self.links_coll = self.db.attachments

    async def add_user(self, id):
        if not await self.is_present(id):
            await self.users_coll.insert_one(dict(id=id))

    async def is_present(self, id):
        return bool(await self.users_coll.find_one({"id": int(id)}))

    async def total_users(self):
        return await self.users_coll.count_documents({})

    async def count_all_links(self):
        return await self.links_coll.count_documents({})

    async def search_movie(self, movie_name):
        search_query = {
            "name": {
                "$regex": re.escape(movie_name).replace(r"\ ", r".*"),
                "$options": "i",
            }
        }
        results = await self.links_coll.find(search_query).to_list(None)
        return results

    async def get_last_documents(self, count):
        return (
            await self.links_coll.find()
            .sort("added_on", -1)
            .limit(count)
            .to_list(count)
        )

    async def add_document(self, document):
        img_url = document.get("img_url")

        for link in document.get("links", []):
            parsed_link = urlparse(link["link"])
            link_path = parsed_link.path + (
                "?" + parsed_link.query if parsed_link.query else ""
            )

            existing_link = await self.links_coll.find_one({"link": link_path})

            if not existing_link:
                new_document = {
                    "img_url": img_url,
                    "name": link["name"],
                    "link": link_path,
                    "added_on": datetime.utcnow(),
                }
                await self.links_coll.insert_one(new_document)
                logging.info(f"New Document Inserted: {new_document}")
                await send_new_link_notification([link])

db = Database(DATABASE_URL, "HeartxScrap")
