#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
MEDIA_DIR = DATA_DIR / "media"
META_PATH = DATA_DIR / "videos_metadata.json"

def download_audio_and_video(vid, url, vtype):
    MEDIA_DIR.mkdir(parents=True, exist_ok=True)
    # Download audio as 64k m4a
    audio_path = MEDIA_DIR / f"{vid}.m4a"
    if not audio_path.exists():
        cmd = [
            "yt-dlp",
            "-f", "ba[ext=m4a]/ba/b",
            "-x",
            "--audio-format", "m4a",
            "--audio-quality", "64K",
            "-o", str(audio_path),
            url
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return audio_path.exists()

def main():
    if not META_PATH.exists():
        print("Metadata not found!")
        return
    with open(META_PATH, "r", encoding="utf-8") as f:
        videos = json.load(f)

    # Focus on the 17 long-form core videos first
    long_videos = [v for v in videos if v.get("type") == "long"]
    print(f"Downloading audio/media for {len(long_videos)} core long-form videos...")
    for idx, v in enumerate(long_videos, 1):
        vid = v["id"]
        vtitle = v["title"]
        print(f"[{idx}/{len(long_videos)}] {vid}: {vtitle}...")
        ok = download_audio_and_video(vid, v["url"], v.get("type"))
        print(f"  -> Audio downloaded: {ok}")

if __name__ == "__main__":
    main()
