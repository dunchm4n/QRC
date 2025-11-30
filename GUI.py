from tkinter import ttk
import tkinter as tk
from tkinter import *
from urltoimage import Generate
from imager import load

def clickbutton(url , label):
    image_path = Generate(url)
    tk_img = load(image_path)
    label.config(image=tk_img)
    label.image = tk_img


def start():
    root = Tk()
    root.title("QRC")
    root.geometry("420x360")

    # ----- NEON BLUE THEME -----
    neon_blue = "#00E5FF"
    dark_bg = "#0A0F1F"  # پس‌زمینه تیره

    root.configure(bg=dark_bg)

    style = ttk.Style()
    style.theme_use("clam")

    # فریم‌ها
    style.configure(
        "TFrame",
        background=dark_bg
    )

    # دکمه‌ها
    style.configure(
        "TButton",
        font=("Segoe UI", 11, "bold"),
        padding=6,
        foreground=dark_bg,
        background=neon_blue,
        borderwidth=0
    )

    style.map(
        "TButton",
        background=[("active", "#00FFFF")],
    )

    # لیبل‌ها
    style.configure(
        "TLabel",
        font=("Segoe UI", 11),
        foreground=neon_blue,
        background=dark_bg
    )

    # ورودی
    style.configure(
        "TEntry",
        fieldbackground="#06203A",
        foreground=neon_blue,
        bordercolor=neon_blue,
        lightcolor=neon_blue,
        darkcolor=neon_blue,
        borderwidth=2
    )

    # -------- فریم‌ها (الان کاملاً هماهنگ) --------
    input_frame = ttk.Frame(root, padding=10)
    input_frame.pack()

    qr_frame = ttk.Frame(root, padding=10)
    qr_frame.pack()
    # لیبل نمایش تصویر — پشت‌زمینه یکدست
    image_label = tk.Label(qr_frame, bg=dark_bg)
    image_label.pack()
    # ویجت‌ها
    ttk.Label(input_frame, text="URL:").grid(row=0, column=0, padx=5, pady=5)

    e = ttk.Entry(input_frame, width=35)
    e.grid(row=0, column=1, padx=5)

    ttk.Button(
        input_frame,
        text="Start!",
        command=lambda: clickbutton(e.get() , image_label)
    ).grid(row=1, column=0, columnspan=2, pady=10)


    root.mainloop()