#!/usr/bin/env python3
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "transcripts" / "raw"
CLEAN_DIR = DATA_DIR / "transcripts" / "cleaned"
META_PATH = DATA_DIR / "videos_metadata.json"

TAG_RE = re.compile(r"<[^>]+>")
TIMESTAMP_RE = re.compile(r"^(\d{2}:\d{2}:\d{2}\.\d{3})\s+-->\s+(\d{2}:\d{2}:\d{2}\.\d{3})")

def clean_vtt_file(vtt_path: Path):
    with open(vtt_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    lines = content.splitlines()
    cues = []
    current_start = None
    current_end = None
    current_text = []

    for line in lines:
        line_str = line.strip()
        if not line_str or line_str.startswith("WEBVTT") or line_str.startswith("Kind:") or line_str.startswith("Language:"):
            continue

        ts_match = TIMESTAMP_RE.match(line_str)
        if ts_match:
            if current_start and current_text:
                cleaned_text = " ".join(current_text).strip()
                if cleaned_text:
                    cues.append((current_start, current_end, cleaned_text))
            current_start = ts_match.group(1).split(".")[0]
            current_end = ts_match.group(2).split(".")[0]
            current_text = []
            continue

        # Strip inline tags
        raw_text = TAG_RE.sub("", line_str).strip()
        if raw_text:
            current_text.append(raw_text)

    if current_start and current_text:
        cleaned_text = " ".join(current_text).strip()
        if cleaned_text:
            cues.append((current_start, current_end, cleaned_text))

    # Now deduplicate rolling lines across cues
    # Each cue often repeats previous lines. We can extract words and keep order.
    words_with_timestamps = []
    last_words = []

    for start, end, text in cues:
        cue_words = text.split()
        for i, w in enumerate(cue_words):
            # Check if this word is a repeat of recent words
            if words_with_timestamps and words_with_timestamps[-1][1] == w:
                continue
            words_with_timestamps.append((start, w))

    # Second pass: remove multi-word duplicate cycles (e.g. "dediği gibi yüzüne dediği gibi yüzüne")
    filtered_words = []
    i = 0
    n = len(words_with_timestamps)
    while i < n:
        ts, word = words_with_timestamps[i]
        # check for phrase repetition of length 1 to 8
        is_repeat = False
        for plen in range(1, 9):
            if i + 2 * plen <= n:
                phrase1 = [w for _, w in words_with_timestamps[i:i+plen]]
                phrase2 = [w for _, w in words_with_timestamps[i+plen:i+2*plen]]
                if phrase1 == phrase2:
                    # Skip the first instance or skip the duplicate
                    # We will advance i by plen and skip duplicate
                    filtered_words.extend(words_with_timestamps[i:i+plen])
                    i += 2 * plen
                    # continue skipping if it repeats 3rd time
                    while i + plen <= n and [w for _, w in words_with_timestamps[i:i+plen]] == phrase1:
                        i += plen
                    is_repeat = True
                    break
        if not is_repeat:
            filtered_words.append((ts, word))
            i += 1

    # Group into timestamped paragraphs
    paragraphs = []
    current_para_words = []
    para_start = None

    for ts, word in filtered_words:
        if not para_start:
            para_start = ts
        current_para_words.append(word)

        # Split at sentence end or ~60 words
        if len(current_para_words) >= 50 and word.endswith((".", "?", "!")):
            paragraphs.append(f"[{para_start}] " + " ".join(current_para_words))
            current_para_words = []
            para_start = None
        elif len(current_para_words) >= 75:
            paragraphs.append(f"[{para_start}] " + " ".join(current_para_words))
            current_para_words = []
            para_start = None

    if current_para_words:
        paragraphs.append(f"[{para_start or '00:00:00'}] " + " ".join(current_para_words))

    full_text = " ".join([w for _, w in filtered_words])
    return "\n\n".join(paragraphs), full_text

def main():
    CLEAN_DIR.mkdir(parents=True, exist_ok=True)
    if not META_PATH.exists():
        print("Metadata not found!")
        return

    with open(META_PATH, "r", encoding="utf-8") as f:
        videos = json.load(f)

    for v in videos:
        vid = v["id"]
        vtitle = v["title"]
        vtt_file = None
        for cand in [f"{vid}.tr-orig.vtt", f"{vid}.tr.vtt", f"{vid}.en-orig.vtt", f"{vid}.en.vtt"]:
            p = RAW_DIR / cand
            if p.exists():
                vtt_file = p
                break

        if not vtt_file:
            continue

        timestamped, full_text = clean_vtt_file(vtt_file)
        out_file = CLEAN_DIR / f"{vid}.md"
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(f"# {vtitle}\n\n")
            f.write(f"- **Video ID:** {vid}\n")
            f.write(f"- **URL:** {v['url']}\n")
            f.write(f"- **Type:** {v['type']}\n")
            f.write(f"- **Duration:** {v.get('duration')}s\n\n")
            f.write("## Timestamped Transcript\n\n")
            f.write(timestamped)
            f.write("\n\n## Continuous Text\n\n")
            f.write(full_text)
            f.write("\n")
        print(f"Cleaned {vid} -> {out_file.name}")

if __name__ == "__main__":
    main()
