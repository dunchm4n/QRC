from PIL import Image, ImageTk

def load(path , w=300 , h=200):
    img = Image.open(path)
    img = img.resize((w, h), Image.Resampling.LANCZOS)

    return ImageTk.PhotoImage(img)