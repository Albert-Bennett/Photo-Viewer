from PIL import Image, ImageTk

def tk_image(path,w,h):
    img = Image.open(path)
    img = img.resize((w,h))
    storeobj = ImageTk.PhotoImage(img)
    return storeobj