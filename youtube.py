from pytube import YouTube

def download_video():
    try:
        url = input("Enter YouTube video URL: ").strip()
        yt = YouTube(url)
        
        print(f"Title: {yt.title}")
        print("Downloading...")

        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution()
        stream.download()

        print("✅ Download complete!")

    except Exception as e:
        print("❌ An error occurred:", e)

download_video()
