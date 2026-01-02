import os

# --- API KEYS ---
# Required for Audio and Video Clips
ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")
PEXELS_API_KEY = os.environ.get("PEXELS_API_KEY")

# --- DIRECTORY SETUP ---
BASE_DIR = "Policy_Meridian_Factory"
ASSETS_DIR = "assets"

# --- VOICE MAPPING ---
# Voice: "Adam" (Deep American Narrator) - Best for serious news
# This ID (pNInz6obpgDQGcFmaJgB) is a standard pre-made voice.
VOICE_MAP = {
    "The_Policy_Meridian": "pNInz6obpgDQGcFmaJgB"
}

# --- CHANNEL SETUP ---
CHANNELS = ["The_Policy_Meridian"]
