import random
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class YouTubeViewerBot:
    """Simulates organic video views using Selenium."""

    def __init__(self, headless: bool = True):
        self.headless = headless
        self.driver = None

    def _init_driver(self):
        opts = Options()
        if self.headless:
            opts.add_argument("--headless")
        opts.add_argument("--mute-audio")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=opts)

    def watch_video(self, video_url: str, watch_time: int = 30):
        """Watch a YouTube video for a given number of seconds."""
        if not self.driver:
            self._init_driver()
        self.driver.get(video_url)
        time.sleep(3)  # wait for page load
        # Simulate human watching
        watch_seconds = min(watch_time, random.randint(15, 60))
        time.sleep(watch_seconds)
        return watch_seconds

    def get_video_title(self, video_url: str) -> str:
        """Fetch video title using requests + BeautifulSoup fallback."""
        try:
            resp = requests.get(video_url, timeout=10)
            resp.raise_for_status()
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(resp.text, "html.parser")
            title_tag = soup.find("title")
            if title_tag:
                return title_tag.get_text(strip=True)
        except Exception:
            pass
        return "Unknown Title"

    def close(self):
        if self.driver:
            self.driver.quit()
            self.driver = None