import os
import asyncio
import aiohttp
from bs4 import BeautifulSoup


async def fetch_page(session, url):
    async with session.get(url) as response:
        return await response.text()


async def scrape_webpages(base_url, start_page, end_page):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, "wordlist.txt")

    async with aiohttp.ClientSession() as session:
        tasks = []
        for page_num in range(start_page, end_page + 1):
            url = f"{base_url}{page_num}"
            tasks.append(fetch_page(session, url))

        responses = await asyncio.gather(*tasks)

        with open(file_path, "w", encoding="utf-8") as file:
            for response_text in responses:
                soup = BeautifulSoup(response_text, 'html.parser')
                all_links = soup.find_all('a', itemprop="url")
                for link in all_links:
                    extracted_text = link.text.strip()
                    file.write(extracted_text + "\n")


# Example usage
base_url = "https://www.varduzinynas.lt/vardai?page="
start_page = 1
end_page = 78

# Create a new event loop
loop = asyncio.new_event_loop()
# Set the new event loop as the current event loop
asyncio.set_event_loop(loop)
# Run the coroutine
loop.run_until_complete(scrape_webpages(base_url, start_page, end_page))