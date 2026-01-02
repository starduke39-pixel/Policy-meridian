import os
import requests
import random
import config

OUTPUT_DIR = config.ASSETS_DIR

def generate_image_free(prompt, filename, width, height):
    print(f"   🎨 Generating {filename} via Pollinations...")
    
    # URL Encode prompt
    encoded_prompt = requests.utils.quote(prompt)
    seed = random.randint(1, 99999)
    
    # Pollinations.ai (Free, No API Key required)
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width={width}&height={height}&seed={seed}&nologo=true&model=flux"
    
    try:
        response = requests.get(url, timeout=60)
        if response.status_code == 200:
            path = os.path.join(OUTPUT_DIR, filename)
            with open(path, 'wb') as f:
                f.write(response.content)
            print(f"   ✅ Saved: {filename}")
        else:
            print(f"   ❌ Error: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Connection Error: {e}")

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # 1. Logo (Square)
    logo_prompt = "Vector logo for geopolitical news channel 'The Policy Meridian'. Minimalist map of North Carolina with a wireframe globe inside. Dark Navy Blue and Gold. Government agency emblem style."
    generate_image_free(logo_prompt, "channel_logo.jpg", 1024, 1024)

    # 2. Banner (Wide)
    banner_prompt = "Cinematic YouTube banner. Dark moody split screen. Left: North Carolina State Legislative Building. Right: Digital World Map. Text overlay: 'LOCAL LAW. GLOBAL IMPACT.' Dark blue political thriller aesthetic."
    generate_image_free(banner_prompt, "channel_banner.jpg", 1920, 1080)

if __name__ == "__main__":
    main()
