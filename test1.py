import os
import aiohttp
import asyncio
from bs4 import BeautifulSoup


async def fetch_page(session, url):
    async with session.get(url) as response:
        return await response.text()


async def scrape_webpages(base_url):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, "nepaligirl.txt")

    async with aiohttp.ClientSession() as session:
        with open(file_path, "w", encoding="utf-8") as file:
            for letter in range(ord('A'), ord('Z') + 1):
                url = f"{base_url}/{chr(letter)}-Girl"
                print(f"Scraping page {chr(letter)}")
                response_text = await fetch_page(session, url)
                soup = BeautifulSoup(response_text, 'html.parser')
                tds = soup.find_all('td', attrs={'rel': 'tooltip'})
                for td in tds:
                    title_text = td.get('title')
                    if title_text:
                        print(f"Extracted text: {title_text}")
                        file.write(title_text + "\n")


# Example usage
base_url = "https://www.nepaliname.com/babyname/startingWith"

# Create a new event loop
loop = asyncio.new_event_loop()
# Set the new event loop as the current event loop
asyncio.set_event_loop(loop)
# Run the coroutine
loop.run_until_complete(scrape_webpages(base_url))
