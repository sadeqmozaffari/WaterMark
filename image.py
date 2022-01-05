from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os, shutil


class WaterMark(Tk):
    def __init__(self):
        super().__init__()

        self.label = ttk.Label(self.labelFrame, text="Water Mark For Image")
        self.button = ttk.Button(self.labelFrame, text="Choose A Image", command=self.file_handle)
        self.file_name = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                                    filetype=(("jpeg", "*.jpg"), ("png", "*.png")))
        self.labelFrame = ttk.LabelFrame(self, text="Open A File")
        self.labelFrame.grid(column=0, row=1, padx=20, pady=20)
        self.choose_image()

    def choose_image(self):
        self.button.grid(column=1, row=1)

    def file_handle(self):
        self.label.grid(column=1, row=2)
        self.label.configure(text=self.file_name)
        os.chdir('e:\\')
        os.system('mkdir BACKUP')
        shutil.move(self.fileName, 'e:\\')
