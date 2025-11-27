"""
Exports base64 or raw PNG sprites to /game/assets/sprites.
Placeholder tool.
"""

import os
from pathlib import Path

SPRITE_DIR = Path("../game/assets/sprites")

def ensure():
    SPRITE_DIR.mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    ensure()
    print("Sprite export tool ready (placeholder).")
