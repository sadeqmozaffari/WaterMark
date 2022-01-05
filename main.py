import os
import shutil
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Water Mark")
window.wm_minsize(height=200,width=200)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


def watermark_image():
    label = ttk.Label(text="")
    label.grid(column=0, row=1)
    file_name = filedialog.askopenfilename(initialdir="/", title="Select Image",
                                           filetype=(("jpeg", "*.jpg"), ("png", "*.png")))
    label.configure(text=file_name)


    try:
        with Image.open(file_name) as img:
            base = img.convert('RGBA')
            width, height = base.size

            # make a blank image for the text, initialized to transparent text color
            txt = Image.new('RGBA', base.size, (255, 255, 255, 0))

            # get a font
            fnt = ImageFont.truetype('arial.ttf', 40)
            # get a drawing context
            d = ImageDraw.Draw(txt)

            x = width / 2
            y = height / 2

            # draw text, half opacity
            d.text((x, y), "Sadeq Mozaffari", font=fnt, fill=(255, 255, 255, 128))
            txt = txt.rotate(45)

            out = Image.alpha_composite(base, txt)
            out.show()
    except OSError:
        print("cannot create WaterMark for", file_name)


button = ttk.Button(text="Choose Image", command=watermark_image)
button.grid(column=1, row=1)

window.mainloop()
