import os
import yt_dlp

def download_video():
    url = input("Paste the YouTube video URL: ").strip()

    # Set output directory
    download_folder = os.path.join(os.path.expanduser("~"), "YouTube")
    os.makedirs(download_folder, exist_ok=True)

    # Set options
    ydl_opts = {
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',  # Download best video+audio
        'merge_output_format': 'mp4'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Download completed and saved in: {download_folder}")
    except Exception as e:
        print("Download error:", e)

download_video()
