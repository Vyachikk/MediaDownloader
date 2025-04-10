import subprocess
import os
import re
from config import TOR_PROXY, COOKIES_FILE, DOWNLOAD_FOLDER

def download_video(url):
    use_tor = any(domain in url for domain in ['instagram.com', 'tiktok.com', 'vkvideo.ru'])
    cmd = [
        "yt-dlp",
        url,
        "-P", DOWNLOAD_FOLDER
    ]

    if use_tor:
        cmd += ["--proxy", TOR_PROXY]

    if "instagram.com" in url:
        cmd += ["--cookies", COOKIES_FILE]

    try:
        subprocess.run(cmd, check=True)
        print(f"✅ Скачано: {url}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка при скачивании {url}: {e}")
        return None

    # Возвращаем путь к последнему загруженному файлу
    files = os.listdir(DOWNLOAD_FOLDER)
    latest_file = max(files, key=lambda f: os.path.getctime(os.path.join(DOWNLOAD_FOLDER, f)))
    return os.path.join(DOWNLOAD_FOLDER, latest_file)

# Проверка ссылки
SUPPORTED_PATTERNS = [
    r"vkvideo\.ru/video",
    r"vk\.com/clip",
    r"vk\.com/video",
    r"youtube\.com/watch",
    r"youtu\.be/", 
    r"rutube\.ru/video", 
    r"instagram\.com/reel", 
    r"tiktok\.com/@"
]
def is_supported_url(url):
    return any(re.search(pattern, url) for pattern in SUPPORTED_PATTERNS)
