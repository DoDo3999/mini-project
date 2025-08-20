# 🎵 YouTube Music Downloader (yt-dlp + ffmpeg)

สคริปต์ Python สำหรับดาวน์โหลดเพลงจาก YouTube และแปลงไฟล์เป็น MP3 โดยใช้  
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)  
- [FFmpeg](https://ffmpeg.org/)  

## 📌 วิธีใช้งาน

1. ติดตั้ง dependencies:
   ```bash
   pip install yt-dlp
   ```
   และดาวน์โหลด [FFmpeg](https://www.gyan.dev/ffmpeg/builds/)  
   จากนั้นเพิ่ม path `ffmpeg/bin` ลงใน **Environment Variables**

2. แก้ไข `download.py` ใส่ลิงก์ YouTube ที่ต้องการดาวน์โหลด

   ```python
   link = "https://youtu.be/xxxxxx"  # แก้เป็นลิงก์ของคุณ
   download_mp3(link, "./songs")
   ```

3. รันสคริปต์
   ```bash
   python download.py
   ```

4. เพลงที่ดาวน์โหลดจะถูกเก็บไว้ในโฟลเดอร์ `./songs`  

---

## ⚠️ Disclaimer

- โค้ดนี้สร้างขึ้นเพื่อการศึกษาและใช้งานส่วนตัวเท่านั้น  
- ผู้ใช้ต้องรับผิดชอบต่อการใช้งานเอง หากนำไปใช้ดาวน์โหลดไฟล์ที่มีลิขสิทธิ์  
- ผู้พัฒนาโค้ดนี้ **ไม่สนับสนุนการละเมิดลิขสิทธิ์** ในทุกรูปแบบ  

---

## 📄 License

MIT License – คุณสามารถนำไปแก้ไข/ใช้ต่อได้อิสระ
