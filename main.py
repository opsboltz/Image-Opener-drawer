import tkinter
import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter
from tkinter import ttk

root = tk.Tk()
root.geometry("1000x600")
root.title("Image Drawing Tool")
root.config(bg="#acacac")

pen_color = "black"
pen_size = 5
file_path = ""

def add_image():
    global file_path
    file_path = filedialog.askopenfilename()
    image = Image.open(file_path)
    # Converting the image for the canvas
    ##doing the math
    width, height = int(image.width / 2), int(image.height / 2)
    image = image.resize((width, height), Image.LANCZOS)  # Changed from Image.ANTIALIAS to Image.LANCZOS
    #putting the image on the canvas
    canvas.config(width=image.width, height=image.height)
    image = ImageTk.PhotoImage(image)

    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")

def clear_canvas():
    canvas.delete("all")
    ##doing this to remebr the original canvas
    canvas.create_image(0, 0, image=canvas.image, anchor="nw")

#Color chooser
def change_color():
    global pen_color
    pen_color = colorchooser.askcolor(title="Select Pen Color")[1]

def apply_filter(filter):
    image = Image.open(file_path)
    width, height = int(image.width / 2), int(image.height / 2)
    image = image.resize((width, height), Image.LANCZOS)
    if filter == "Black and White":
        image = ImageOps.grayscale(image)
    if filter == "Blur":
        image = image.filter(ImageFilter.BLUR)
    if filter == "Sharpen":
        image = image.filter(ImageFilter.SHARPEN)
    if filter == "Smooth":
        image = image.filter(ImageFilter.SMOOTH)
    if filter == "Emboss":
        image = image.filter(ImageFilter.EMBOSS)



    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")




def change_size(size):
    #making it so i can get the size varible
    global pen_size
    pen_size = size



def draw(event):
    #event.x is where you clicked
    #enent.y gets the y cord that you clicked
    # so it minus and then adds it so it can get the y and x
    # so it can create the big oval
    x1, y1 = (event.x - pen_size), (event.y - pen_size)
    x2, y2 = (event.x + pen_size), (event.y + pen_size)
    canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline='')

    ##Putting in the left_frame

left_frame = tk.Frame(root, width=200, height=600, bg="#808080")  # Hex color for grey
left_frame.pack(side="left", fill="y")

canvas = tk.Canvas(root, width=750, height=600, bg="#ffffff")  # Hex color for white
canvas.pack()

image_button = tk.Button(left_frame, text="Add Image", command=add_image, bg="#ffffff")  # Hex color for white
image_button.pack(pady=155)

##color Chooser Button

color_button = tkinter.Button(
    left_frame, text="Change Pen color", command=change_color, bg="white")
color_button.pack(pady=5)

pen_size_frame = tk.Frame(left_frame, bg="#c2c2d6")
pen_size_frame.pack(pady=5)

#pen_size_Button
##Radio buttons are used to toggle
##the lambda is used to pass vales back to my function
pen_size_1 = tk.Radiobutton(
    pen_size_frame, text="Small", value=3, bg="white", command=lambda: change_size(3))
pen_size_1.pack(side="left")

pen_size_2 = tk.Radiobutton(
    pen_size_frame, value=5 , text="Medium", bg="white", command=lambda: change_size(5))
pen_size_2.pack(side="left")
##So it selects it on launch
pen_size_2.select()


pen_size_3 = tk.Radiobutton(
    pen_size_frame, text="Large", value=7, bg="white", command=lambda: change_size(8))
pen_size_3.pack(side="left")

clear_button = tk.Button(left_frame, text="Clear",
                         command=clear_canvas, bg="#FF9797")
clear_button.pack(pady=10)

filter_label = tk.Label(left_frame, text="Select Filter", bg="white")
filter_label.pack()


#Combo box is a list of options

filter_combobox = ttk.Combobox(left_frame, values=["Black and White", "Blur", "Emboss", "Sharpen", "Smooth"])
filter_combobox.pack()

filter_combobox.bind("<<ComboboxSelected>>",
                     lambda event: apply_filter(filter_combobox.get()))



#so i can click and let go and it can draw so it will "draw" when click and hold
canvas.bind("<B1-Motion>", draw)

root.mainloop()
