"""Utilities for rendering bundled destination images in Streamlit HTML."""

import base64
import mimetypes
import os
import re
from functools import lru_cache


ASSET_DIR = os.path.join(os.path.dirname(__file__), "assets")
FALLBACK_ASSET = "kashmirHeavenOfEarth.jpg"


@lru_cache(maxsize=128)
def asset_src(image_reference: str, destination: str = "", slot: int = 1) -> str:
    """Return a local data URI for a destination image."""
    if image_reference.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
        candidate = os.path.join(ASSET_DIR, image_reference)
    else:
        destination_key = re.sub(r"[^A-Za-z0-9-]", "", destination.replace(" ", "-"))
        candidate = os.path.join(ASSET_DIR, f"{destination_key}_{slot}.jpg")

    image_id_match = re.search(r"photo-([^?&]+)", image_reference)
    image_id = image_id_match.group(1) if image_id_match else ""
    if not os.path.isfile(candidate):
        candidate = os.path.join(ASSET_DIR, f"unsplash_{image_id}.jpg")
    if not os.path.isfile(candidate):
        candidate = os.path.join(ASSET_DIR, FALLBACK_ASSET)

    mime_type = mimetypes.guess_type(candidate)[0] or "image/jpeg"
    with open(candidate, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"
