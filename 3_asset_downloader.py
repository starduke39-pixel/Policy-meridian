import os
import requests
import config

VIDEOS_PER_SEARCH = 15
ORIENTATION = "landscape"

def search_and_download(query, save_folder):
    print(f"\n🔍 Searching Pexels for: '{query}'...")
    headers = {'Authorization': config.PEXELS_API_KEY}
    url = f"https://api.pexels.com/videos/search?query={query}&per_page={VIDEOS_PER_SEARCH}&orientation={ORIENTATION}&size=medium"
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        if not os.path.exists(save_folder): os.makedirs(save_folder)

        for video in data.get('videos', []):
            video_files = video.get('video_files', [])
            target_file = next((v for v in video_files if v['width'] >= 1920), video_files[0])
            download_url = target_file['link']
            file_name = f"{video['id']}.mp4"
            full_path = os.path.join(save_folder, file_name)
            
            if not os.path.exists(full_path):
                print(f"   ⬇️ Downloading: {file_name}")
                with open(full_path, 'wb') as f:
                    f.write(requests.get(download_url).content)
    except Exception as e:
        print(f"Error: {e}")

def main():
    asset_dir = os.path.join(config.BASE_DIR, "Stock_Footage_News")
    # News Keywords
    keywords = ["United States Flag", "Capitol Building", "Gavel", "United Nations", "World Map", "Diplomacy Handshake", "Voting", "Washington DC"]
    channel_asset_dir = os.path.join(asset_dir, "The_Policy_Meridian")
    for keyword in keywords:
        search_and_download(keyword, channel_asset_dir)

if __name__ == "__main__":
    main()
