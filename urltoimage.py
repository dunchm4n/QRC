import qrcode


def Generate(url , filename="img.png"):
    img = qrcode.make(url)
    img.save(filename)
    return filename