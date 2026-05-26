import pytest
from src.bot import YouTubeViewerBot
from src.utils import extract_video_id, random_user_agent

def test_extract_video_id_standard():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    assert extract_video_id(url) == "dQw4w9WgXcQ"

def test_extract_video_id_short():
    url = "https://youtu.be/dQw4w9WgXcQ"
    assert extract_video_id(url) == "dQw4w9WgXcQ"

def test_extract_video_id_invalid():
    assert extract_video_id("https://example.com") == ""

def test_random_user_agent():
    ua = random_user_agent()
    assert "Chrome" in ua
    assert len(ua) > 50

def test_bot_initialization():
    bot = YouTubeViewerBot(headless=True)
    assert bot.headless is True
    assert bot.driver is None
    bot.close()

def test_bot_get_video_title(monkeypatch):
    bot = YouTubeViewerBot(headless=True)
    # Mock requests to avoid real network call
    class MockResponse:
        status_code = 200
        def raise_for_status(self):
            pass
        @property
        def text(self):
            return "<html><title>Test Video - YouTube</title></html>"
    import requests
    monkeypatch.setattr(requests, "get", lambda url, timeout: MockResponse())
    title = bot.get_video_title("https://www.youtube.com/watch?v=test123")
    assert "Test Video" in title
    bot.close()