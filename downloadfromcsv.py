import os
import yt_dlp
import pandas as pd
from pytube import YouTube
from youtubesearchpython import VideosSearch


def download_song(track_name, artist_name, output_path="downloads"):
    try:
        query = f"{track_name} {artist_name}"
        

        videos_search = VideosSearch(query, limit=1)
        video_result = videos_search.result()["result"]
        
        if not video_result:
            print(f"No results found for '{query}'")
            return
        
        video_url = video_result[0]["link"]
        print(f"Downloading: {track_name} by {artist_name} ({video_url})")
        
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        
        ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(output_path, f"{track_name} - {artist_name}.%(ext)s"),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'ffmpeg_location': 'C:\\ffmpeg\\bin'
}

        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        
        print(f"Downloaded '{track_name}' successfully!\n")
    
    except Exception as e:
        print(f"Error downloading '{track_name}' by {artist_name}: {e}")

def main():
    input_file = "My Spotify Library.csv"
    songs_df = pd.read_csv(input_file)
    
    if "Track name" not in songs_df.columns or "Artist name" not in songs_df.columns:
        print("CSV file must contain 'Track name' and 'Artist name' columns.")
        return
    
    songs_to_download = songs_df.head(500)
    
    for _, row in songs_to_download.iterrows():
        track_name = row["Track name"]
        artist_name = row["Artist name"]
        download_song(track_name, artist_name)

if __name__ == "__main__":
    main()
