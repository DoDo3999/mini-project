import yt_dlp
import os

def download_mp3(url, output_path="songs"):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{output_path}/%(title)s.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "ffmpeg_location": "ffmpeg",  # ใช้ path ของ ffmpeg ที่อยู่ใน PATH
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    link = "https://youtu.be/xxxxxx"  # 🔗 แก้เป็นลิงก์ YouTube ของคุณ
    download_mp3(link, "./songs")
