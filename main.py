import tkinter as tk
from tkinter import messagebox
import threading
from yt_dlp import YoutubeDL

def download_video():
    url = entry_url.get()
    if not url:
        messagebox.showwarning("Input Kosong", "URL video tidak boleh kosong!")
        return

    # Validasi URL sederhana
    if not url.startswith("http"):
        messagebox.showwarning("URL Tidak Valid", "Masukkan URL yang valid!")
        return

    # Fungsi pengunduhan video
    def download():
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Mengunduh video dan audio terbaik, atau yang terbaik secara keseluruhan
            'outtmpl': '%(title)s.%(ext)s',  # Menyimpan dengan nama video
            'quiet': False,  # Menampilkan proses pengunduhan
            'merge_output_format': 'mp4',  # Menggabungkan video dan audio dalam format MP4
        }

        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            messagebox.showinfo("Sukses", "Video berhasil diunduh!")
        except Exception as e:
            messagebox.showerror("Kesalahan", f"Terjadi kesalahan: {str(e)}")

    # Jalankan proses download di thread terpisah agar GUI tetap responsif
    threading.Thread(target=download, daemon=True).start()

# GUI sederhana
root = tk.Tk()
root.title("Downloader Video YouTube")

tk.Label(root, text="Masukkan URL Video:").pack(pady=5)
entry_url = tk.Entry(root, width=50)
entry_url.pack(pady=5)

btn_download = tk.Button(root, text="Download Video", command=download_video)
btn_download.pack(pady=10)

root.mainloop()
