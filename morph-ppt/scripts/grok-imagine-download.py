#!/usr/bin/env python3
import json
import os
import sys
from pathlib import Path

import requests

API_BASE = os.environ.get("GROK_IMAGINE_BASE", "http://192.168.50.188:8887/v1")
API_KEY = os.environ.get("GROK_IMAGINE_KEY", "sk-jown2004")
MODEL = os.environ.get("GROK_IMAGINE_MODEL", "grok-imagine-1.0")


def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: grok-imagine-download.py <prompt> <output_path>", file=sys.stderr)
        return 1

    prompt = sys.argv[1]
    out_path = Path(sys.argv[2]).expanduser().resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": MODEL,
        "prompt": prompt,
    }

    resp = requests.post(f"{API_BASE}/images/generations", headers=headers, json=payload, timeout=180)
    resp.raise_for_status()
    data = resp.json()
    try:
        url = data["data"][0]["url"]
    except Exception:
        print(json.dumps(data, ensure_ascii=False, indent=2), file=sys.stderr)
        raise

    url = url.replace("192.68.50.188", "192.168.50.188")
    img = requests.get(url, timeout=180)
    img.raise_for_status()
    out_path.write_bytes(img.content)
    print(str(out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
