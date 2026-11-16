#!/usr/bin/env python3
import json
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_TRANSCRIPTS_DIR = DATA_DIR / "transcripts" / "raw"
MEDIA_DIR = DATA_DIR / "media"

CHANNEL_URLS = [
    ("long", "https://www.youtube.com/@AceTradingTR/videos"),
    ("short", "https://www.youtube.com/@AceTradingTR/shorts")
]

def run_cmd(cmd):
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout, result.stderr, result.returncode

def fetch_metadata():
    videos = []
    seen_ids = set()

    for vtype, url in CHANNEL_URLS:
        print(f"Fetching {vtype} videos from {url}...")
        cmd = [
            "yt-dlp",
            "--flat-playlist",
            "-J",
            url
        ]
        out, err, code = run_cmd(cmd)
        if code != 0:
            print(f"Error fetching {url}: {err}")
            continue
        data = json.loads(out)
        entries = data.get("entries", [])
        for entry in entries:
            vid = entry.get("id")
            if not vid or vid in seen_ids:
                continue
            seen_ids.add(vid)
            videos.append({
                "id": vid,
                "title": entry.get("title"),
                "duration": entry.get("duration"),
                "url": f"https://www.youtube.com/watch?v={vid}",
                "type": vtype,
                "description": entry.get("description", "")
            })

    output_meta = DATA_DIR / "videos_metadata.json"
    with open(output_meta, "w", encoding="utf-8") as f:
        json.dump(videos, f, ensure_ascii=False, indent=2)
    print(f"Saved metadata for {len(videos)} videos to {output_meta}")
    return videos

def fetch_subtitles(videos):
    RAW_TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
    for idx, v in enumerate(videos, 1):
        vid = v["id"]
        vtitle = v["title"]
        vurl = v["url"]
        print(f"[{idx}/{len(videos)}] Downloading subtitles for {vid}: {vtitle}...")
        out_tmpl = str(RAW_TRANSCRIPTS_DIR / f"{vid}.%(ext)s")
        cmd = [
            "yt-dlp",
            "--skip-download",
            "--write-auto-subs",
            "--write-subs",
            "--sub-lang", "tr,tr-orig,en",
            "--sub-format", "vtt",
            "-o", out_tmpl,
            vurl
        ]
        out, err, code = run_cmd(cmd)
        # Check what got downloaded
        found = list(RAW_TRANSCRIPTS_DIR.glob(f"{vid}.*.vtt"))
        if found:
            print(f"  -> Got {len(found)} subtitle files: {[f.name for f in found]}")
        else:
            print(f"  -> No subtitles found for {vid}")

if __name__ == "__main__":
    videos = fetch_metadata()
    fetch_subtitles(videos)
