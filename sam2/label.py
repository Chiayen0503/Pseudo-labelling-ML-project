import sys
import os
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import shutil

class Interface:
    def __init__(self, root, filelist):
        self.filelist = filelist
        self.root = root
        self.root.title("Data labeller Y/N?")
        frame = ttk.Frame(self.root, width=1000, height=1000)
        frame.grid()
        frame.grid_configure(padx=10,pady=5)
        # To do: configure the text, wrap into a column, etc.
        # To do: put all these labels, buttons etc into a grid.
        self.imgfile = self.filelist.pop()
        loaded_image = Image.open(datafolder+'/'+self.imgfile)
        loaded_image = loaded_image.resize((960,540))
        self.img = ImageTk.PhotoImage(loaded_image)
        self.picturebox = Label(frame, image=self.img)
        # self.picturebox.image = self.img
        self.picturebox.grid()
        self.root.bind('<y>', lambda e : self.move_to('y'))
        self.root.bind('<n>', lambda e : self.move_to('n'))

    def load_image(self, new_filename):
        self.imgfile = new_filename
        loaded_image = Image.open(datafolder+'/'+new_filename)
        loaded_image = loaded_image.resize((960,540))
        self.img = ImageTk.PhotoImage(loaded_image)
        self.picturebox.config(image=self.img)
        
    def move_to(self, yn):
        if yn == 'y':
            destination = datafolder+'/yes/'
        elif yn == 'n':
            destination = datafolder+'/no/'
        shutil.move(datafolder+'/'+self.imgfile, destination)
        txt_file = os.path.splitext(self.imgfile)[0] + '.txt'
        shutil.move(datafolder+'/'+ txt_file, destination)

        if len(self.filelist) == 0:
            # If we've exhausted all the files then close the programme.
            self.root.destroy()
        else:
            self.load_image(self.filelist.pop())
    
if __name__=='__main__':
    # Get list of images
    if len(sys.argv) == 1:
        raise Exception("Gimme source folder.")
    else:
        datafolder = sys.argv[1]

    filelist = [f for f in os.listdir(datafolder+'/') if os.path.isfile(os.path.join(datafolder+'/',f)) and (f.endswith('.jpg') or f.endswith('.png'))]
    filelist.sort(reverse=True)

    for folder in ['yes/','no/']:
        if not os.path.exists(datafolder+'/'+folder):
            os.mkdir(datafolder+'/'+folder)
    root = Tk()
    interface = Interface(root,filelist)
    root.mainloop()

    
