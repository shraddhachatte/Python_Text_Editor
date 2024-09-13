import tkinter as tk
from tkinter import Frame, ttk
from tkinter import Frame, Tk, SUNKEN
from tkinter import Button
from tkinter import OptionMenu
from tkinter import Entry
from tkinter import font, colorchooser, filedialog, messagebox
import os
import subprocess
import sys 

from tkinter import Label
from tkinter import Text, Canvas
from tkinter import simpledialog
import math
from PIL import ImageTk,Image,ImageGrab
import time
from PIL import Image, ImageDraw, ImageFont
from tkinter import IntVar,StringVar

# selected_effect = tk.StringVar()

main_application = tk.Tk()
selected_effect = tk.StringVar()
main_application.geometry('800x600')
main_application.title('Light Text Editor')


# Constructing icon path dynamically
icon_path = os.path.join('C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main', 'icons2', 'icon.ico')

if os.path.exists(icon_path):
    main_application.iconbitmap(icon_path)
    
############################################## main menu ###################################################
# -------------------------------------&&&&&&&& End main menu &&&&&&&&&&& ----------------------------------
main_menu = tk.Menu()


#file icons
new_icon = tk.PhotoImage(file=os.path.join('C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main', 'icons2', 'new.png'))
open_icon = tk.PhotoImage(file=os.path.join('C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main', 'icons2', 'open.png'))
save_icon = tk.PhotoImage(file=os.path.join('C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main', 'icons2', 'save.png'))
save_as_icon = tk.PhotoImage(file=os.path.join('C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main', 'icons2', 'save_as.png'))
exit_icon = tk.PhotoImage(file=os.path.join('C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main', 'icons2', 'exit.png'))
page_setup_icon = tk.PhotoImage(file=os.path.join('C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main', 'icons2', 'page_setup.png'))


file = tk.Menu(main_menu, tearoff=False)
page_setup_menu = tk.Menu(main_menu, tearoff=False)
header_footer_menu = tk.Menu(main_menu, tearoff=False)
header_tag = 'header'
footer_tag = 'footer'



#####edit
#edit icons
copy_icon = tk.PhotoImage(file=os.path.join('C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main', 'icons2', 'copy.png'))
paste_icon = tk.PhotoImage(file=os.path.join('C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main', 'icons2', 'paste.png'))
cut_icon = tk.PhotoImage(file=os.path.join('C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main', 'icons2', 'cut.png'))
clear_all_icon = tk.PhotoImage(file=os.path.join('C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main', 'icons2', 'clear_all.png'))
find_icon = tk.PhotoImage(file=os.path.join('C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main', 'icons2', 'find.png'))
print_icon = tk.PhotoImage(file=os.path.join('C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main\\icons2', 'print_icon.png'))

edit = tk.Menu(main_menu, tearoff=False)


######## view icons
tool_bar_icon = tk.PhotoImage(file=os.path.join('C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main', 'icons2', 'tool_bar.png'))
status_bar_icon = tk.PhotoImage(file=os.path.join('C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main', 'icons2', 'status_bar.png'))

view = tk.Menu(main_menu, tearoff=False)


######## color theme
light_default_icon = tk.PhotoImage(file=os.path.join('C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main', 'icons2', 'light_default.png'))
light_plus_icon = tk.PhotoImage(file=os.path.join('C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main', 'icons2', 'light_plus.png'))
dark_icon = tk.PhotoImage(file=os.path.join('C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main', 'icons2', 'dark.png'))
red_icon = tk.PhotoImage(file=os.path.join('C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main', 'icons2', 'red.png'))
monokai_icon = tk.PhotoImage(file=os.path.join('C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main', 'icons2', 'monokai.png'))
night_blue_icon = tk.PhotoImage(file=os.path.join('C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main', 'icons2', 'night_blue.png'))

color_theme = tk.Menu(main_menu, tearoff=False)

theme_choice = tk.StringVar()
color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)

color_dict = {
    'Light Default ' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' :('#ededed', '#6b9dc2')
}


# cascade
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color Theme', menu=color_theme)




############################################## toolbar  ###################################################


tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)

## font box
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0, column=0, padx=5)

# Define the default page size and margins
page_width = 600
page_height = 800
left_margin = 50
right_margin = 50

## size box
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width=14, textvariable = size_var, state='readonly')
font_size['values'] = tuple(range(8,81))
font_size.current(4)
font_size.grid(row=0, column=1, padx=5)

## bold button
bold_icon = tk.PhotoImage(file=os.path.join('C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main', 'icons2', 'bold.png'))
bold_btn = ttk.Button(tool_bar, image=bold_icon)

bold_btn.grid(row=0, column=2, padx=5)

## italic button
italic_icon = tk.PhotoImage(file=os.path.join('C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main', 'icons2', 'italic.png'))
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

## underline button
underline_icon = tk.PhotoImage(file=os.path.join('C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main', 'icons2', 'underline.png'))
underline_btn = ttk.Button(tool_bar, image = underline_icon)
underline_btn.grid(row = 0, column=4, padx=5)

## font color button
font_color_icon = tk.PhotoImage(file=os.path.join('C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main', 'icons2', 'font_color.png'))
font_color_btn = ttk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid(row=0, column=5,padx=5)

## align left
align_left_icon = tk.PhotoImage(file='C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main\\icons2\\align_left.png')

align_left_btn = ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=5)

## align center
align_center_icon = tk.PhotoImage(file=os.path.join('C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main', 'icons2', 'align_center.png'))
align_center_btn = ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0, column=7, padx=5)


## align right
align_right_icon = tk.PhotoImage(file=os.path.join('C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main', 'icons2', 'align_right.png'))
align_right_btn = ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=5)

# -------------------------------------&&&&&&&& End toolbar  &&&&&&&&&&& ----------------------------------

############################################## text editor ###################################################

text_editor = tk.Text(main_application)
text_editor.config(wrap='word', relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# font family and font size functionality
current_font_family = 'Arial'
current_font_size = 12

def change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))
def page_setup():
    pass
def change_fontsize(event=None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))


font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_fontsize)

######## buttons functionality

# bold button functionality
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

bold_btn.configure(command=change_bold)


# italic functionlaity
def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

italic_btn.configure(command=change_italic)
## header and footer 

# Function to set header
def set_header():
    header_text = simpledialog.askstring("Header", "Enter header text:")
    if header_text is not None:
        remove_previous_tag(header_tag)
        text_editor.tag_configure(header_tag, font=('Arial', 14, 'bold'), foreground='blue')
        text_editor.insert(1.0, f"\n\n{'-'*20}\n{header_text}\n{'-'*20}\n\n", header_tag)

# Function to set footer
def set_footer():
    footer_text = simpledialog.askstring("Footer", "Enter footer text:")
    if footer_text is not None:
        remove_previous_tag(footer_tag)
        text_editor.tag_configure(footer_tag, font=('Arial', 12, 'italic'), foreground='green')
        text_editor.insert(tk.END, f"\n\n{'-'*20}\n{footer_text}\n{'-'*20}\n\n", footer_tag)

# Remove the previous occurrence of a tag
def remove_previous_tag(tag_name):
    start_index = '1.0'
    end_index = 'end'
    while True:
        start_index = text_editor.search(f'{tag_name}_start', start_index, stopindex=end_index)
        if not start_index:
            break
        end_index = text_editor.search(f'{tag_name}_end', start_index, stopindex=end_index)
        text_editor.tag_remove(tag_name, start_index, end_index)

def apply_text_effect(effect, **kwargs):
    try:
        sel_start = text_editor.index(tk.SEL_FIRST)
        sel_end = text_editor.index(tk.SEL_LAST)
        if sel_start and sel_end:
            selected_text = text_editor.get(sel_start, sel_end)
            if selected_text:
                text_editor.tag_configure(effect, **kwargs)
                text_editor.tag_add(effect, sel_start, sel_end)
    except tk.TclError:
        pass

def remove_text_effect(effect):
    try:
        sel_start = text_editor.index(tk.SEL_FIRST)
        sel_end = text_editor.index(tk.SEL_LAST)
        if sel_start and sel_end:
            text_editor.tag_remove(effect, sel_start, sel_end)
    except tk.TclError:
        pass




# Typography and Text Effects
text_effects_menu = tk.Menu(main_menu, tearoff=False)
text_effects_menu.add_command(label='Bold', command=lambda: text_editor.tag_add('bold', tk.SEL_FIRST, tk.SEL_LAST))
text_effects_menu.add_command(label='Italic', command=lambda: text_editor.tag_add('italic', tk.SEL_FIRST, tk.SEL_LAST))
text_effects_menu.add_command(label='Underline', command=lambda: text_editor.tag_add('underline', tk.SEL_FIRST, tk.SEL_LAST))
text_effects_menu.add_command(label='Color: Red', command=lambda: apply_text_effect('color_red', foreground='red'))
text_effects_menu.add_command(label='Remove Effect', command=lambda: remove_text_effect('color_red'))
text_effects_menu.add_command(label='Reflection', command=lambda: apply_text_effect('reflection', offset=(0, 2), foreground='gray'))
text_effects_menu.add_command(label='Remove Reflection', command=lambda: remove_text_effect('reflection'))

main_menu.add_cascade(label='Text Effects', menu=text_effects_menu)

# Font Size
font_size_menu = tk.Menu(main_menu, tearoff=False)
font_sizes = ['8', '10', '12', '14', '16', '18', '20', '24', '28', '32', '36', '40', '48', '56', '72']
selected_font_size = tk.StringVar(value='12')
for size in font_sizes:
    font_size_menu.add_radiobutton(label=size, variable=selected_font_size, command=lambda: change_font_size())
main_menu.add_cascade(label='Font Size', menu=font_size_menu)

# Function to change font size
def change_font_size():
    new_size = selected_font_size.get()
    text_editor.tag_configure("custom_size", font=('Arial', int(new_size)))
    text_editor.tag_add("custom_size", tk.SEL_FIRST, tk.SEL_LAST)

# Additional Text Effects
text_effects_menu.add_command(label='Color: Red', command=lambda: text_editor.tag_add('color_red', tk.SEL_FIRST, tk.SEL_LAST))
text_effects_menu.add_command(label='Shadow', command=lambda: text_editor.tag_add('shadow', tk.SEL_FIRST, tk.SEL_LAST))
text_effects_menu.add_command(label='Reflection', command=lambda: text_editor.tag_add('reflection', tk.SEL_FIRST, tk.SEL_LAST))
text_effects_menu.add_command(label='Outline', command=lambda: text_editor.tag_add('outline', tk.SEL_FIRST, tk.SEL_LAST))
text_effects_menu.add_command(label='Glow', command=lambda: text_editor.tag_add('glow', tk.SEL_FIRST, tk.SEL_LAST))

# Configure additional text effects
text_editor.tag_configure('color_red', foreground='red')

text_editor.tag_configure('shadow', background='gray')


text_editor.tag_configure('reflection', background='lightgray')
text_editor.tag_configure('outline', relief='solid', borderwidth=1)
text_editor.tag_configure('glow', font=('Arial', 14, 'bold'), foreground='yellow')


# underline functionality
def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

underline_btn.configure(command=change_underline)


## font color functionality
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])


font_color_btn.configure(command=change_font_color)

### align functionality

def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')

align_left_btn.configure(command=align_left)

## center
def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')

align_center_btn.configure(command=align_center)

## right
def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')

align_right_btn.configure(command=align_right)





text_editor.configure(font=('Arial', 12))
# -------------------------------------&&&&&&&& End text editor &&&&&&&&&&& ----------------------------------


##############################################  status bar ###################################################

status_bar = ttk.Label(main_application, text = 'Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed = False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c'))
        status_bar.config(text=f'Characters : {characters} Words : {words}')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>', changed)


# -------------------------------------&&&&&&&& End  status bar &&&&&&&&&&& ----------------------------------


############################################## main menu functinality ###################################################

## variable
url = ''

## new functionality
def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0, tk.END)

## file commands
file.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator='Ctrl+N', command=new_file)

## open functionality

def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))

file.add_command(label='Open', image=open_icon, compound=tk.LEFT, accelerator='Ctrl+O', command=open_file)
################################3
def openPaintWindow():
    paint_window = Tk()
    # Add your paint window UI components here
    paint_window.mainloop()
# save file



def save_file(event=None):
    global url
    try:
        if url:
            content = text_editor.get(1.0, tk.END)
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
                # Open the saved file in the default text editor
                subprocess.Popen(['xdg-open', url])
        else:
            url = filedialog.asksaveasfilename(defaultextension='.ch', filetypes=(('Custom File', '*.ch'), ('Text File', '*.txt'), ('All files', '*.*')))
            if url:
                with open(url, 'w', encoding='utf-8') as fw:
                    content = text_editor.get(1.0, tk.END)
                    fw.write(content)
                    # Open the saved file in the default text editor
                    subprocess.Popen(['xdg-open', url])
    except Exception as e:
        print("Error:", e)

def save_as(event=None):
    global url
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfilename(defaultextension='.ch', filetypes=(('Custom File', '*.ch'), ('Text File', '*.txt'), ('All files', '*.*')))
        if url:
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
                # Open the saved file in the default text editor
                subprocess.Popen(['xdg-open', url])
    except Exception as e:
        print("Error:", e)
file.add_command(label='Save As', compound=tk.LEFT, accelerator='Ctrl+Alt+S', command=save_as)





## page setup functionality.
def show_page_setup():
    def apply_page_setup():
        # Get user selections
        page_size = page_size_var.get()
        margin = margin_var.get()

        # Set text widget margins based on user selections
        if margin == "Normal":
            text_widget.config(padx=20, pady=20)
        elif margin == "Narrow":
            text_widget.config(padx=10, pady=10)
        elif margin == "Wide":
            text_widget.config(padx=30, pady=30)
        elif margin == "Custom":
            # Implement custom margin logic here
            pass

        # Display message
        messagebox.showinfo("Page Setup", f"Page setup options applied!\nPage Size: {page_size}\nMargin: {margin}")

    page_setup_dialog = tk.Toplevel(main_application)
    page_setup_dialog.title("Page Setup")
    page_setup_dialog.geometry('400x300')
            # Implement custom margin logic here
    page_size_var = tk.StringVar(value="A4")
    page_size_label = tk.Label(page_setup_dialog, text="Page Size:")
    page_size_label.grid(row=0, column=0, padx=10, pady=5)
    page_size_options = ['A4', 'Letter', 'Custom']
    page_size_dropdown = ttk.Combobox(page_setup_dialog, textvariable=page_size_var, values=page_size_options)
    page_size_dropdown.grid(row=0, column=1, padx=10, pady=5)

    # Margins
    margin_var = tk.StringVar(value="Normal")
    margin_label = tk.Label(page_setup_dialog, text="Margins:")
    margin_label.grid(row=1, column=0, padx=10, pady=5)
    margin_options = ['Normal', 'Narrow', 'Wide', 'Custom']
    margin_dropdown = ttk.Combobox(page_setup_dialog, textvariable=margin_var, values=margin_options)
    margin_dropdown.grid(row=1, column=1, padx=10, pady=5)

    # Orientation
    orientation_var = tk.StringVar(value="Portrait")
    orientation_label = tk.Label(page_setup_dialog, text="Orientation:")
    orientation_label.grid(row=2, column=0, padx=10, pady=5)
    orientation_options = ['Portrait', 'Landscape']
    orientation_dropdown = ttk.Combobox(page_setup_dialog, textvariable=orientation_var, values=orientation_options)
    orientation_dropdown.grid(row=2, column=1, padx=10, pady=5)

    # Apply to whole document
    apply_var = tk.BooleanVar()
    apply_var.set(True)
    apply_check = tk.Checkbutton(page_setup_dialog, text="Apply to Whole Document", variable=apply_var)
    apply_check.grid(row=3, column=0, columnspan=2, pady=10)

    # Apply and Cancel buttons
    def apply_page_setup():
        # Implement logic to apply page setup options here
        messagebox.showinfo("Page Setup", "Page setup options applied!")
     # Text widget
    text_widget = tk.Text(page_setup_dialog, width=40, height=10)
    text_widget.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    apply_button = tk.Button(page_setup_dialog, text="Apply", command=apply_page_setup)
    apply_button.grid(row=4, column=0, pady=5)

    cancel_button = tk.Button(page_setup_dialog, text="Cancel", command=page_setup_dialog.destroy)
    cancel_button.grid(row=4, column=1, pady=5)

# Add the Page Setup menu item
main_menu.add_cascade(label='Page Setup', menu=page_setup_menu)
page_setup_menu.add_command(label='Page Setup Options', image=page_setup_icon, compound=tk.LEFT, command=show_page_setup)

###################################################################################################333
# stroke size options 
options = [1,2,3,4,5,10]

stroke_size = IntVar()
stroke_size.set(1)

stroke_color = StringVar()
stroke_color.set("black")

previousColor = StringVar()
previousColor.set("white")

previousColor2 = StringVar()
previousColor2.set("white")

# variables for pencil 
prevPoint = [0,0]
currentPoint = [0,0] 

# variable for text
textValue = StringVar()

# --------------------- functions -------------------------

def usePencil():
    stroke_color.set("black")
    canvas["cursor"] = "arrow"

def useEraser():
    stroke_color.set("white")
    DOTBOX = "dotbox_cursor"

    canvas["cursor"] = DOTBOX
    # DOTBOX = "dotbox"
    DOTBOX = "dotbox_cursor"

# Your functions and other code follow...



def selectColor():
    selectedColor = colorchooser.askcolor("blue" , title="Select Color")
    if selectedColor[1] == None :
        stroke_color.set("black")
    else:
        stroke_color.set(selectedColor[1])
        previousColor2.set(previousColor.get())
        previousColor.set(selectedColor[1])

        previousColorButton["bg"] = previousColor.get()
        previousColor2Button["bg"] = previousColor2.get()

def paint(event):
    global prevPoint
    global currentPoint
    x = event.x
    y = event.y
    currentPoint = [x,y]
    # canvas.create_oval(x , y , x +5 , y + 5 , fill="black")

    if prevPoint != [0,0] : 
        canvas.create_polygon(prevPoint[0] , prevPoint[1] , currentPoint[0] , currentPoint[1],fill=stroke_color.get() , outline=stroke_color.get() , width=stroke_size.get())        

    prevPoint = currentPoint

    if event.type == "5" :
        prevPoint = [0,0]

def paintRight(event):
    x = event.x
    y = event.y
    canvas.create_arc(x,y,x+stroke_size.get() , y+stroke_size.get() , fill=stroke_color.get() , outline=stroke_color.get() , width=stroke_size.get())
    

# 
#         messagebox.showinfo("Paint app: " , "Error occured")
def saveImage():
    try:
        fileLocation = filedialog.asksaveasfilename(defaultextension="jpg")
        print("File location:", fileLocation)  # Debug message
        if not fileLocation:  # If user cancels file dialog
            return
        x = root.winfo_rootx()
        y = root.winfo_rooty() + 100
        print("Bounding box coordinates:", x, y)  # Debug message
        img = ImageGrab.grab(bbox=(x, y, x + 1100, y + 500))
        print("Image size:", img.size)  # Debug message
        img.save(fileLocation)
        print("Image saved successfully")  # Debug message
        showImage = messagebox.askyesno("Paint App", "Do you want to open image?")
        if showImage:
            img.show()
    except Exception as e:
        print("Error occurred:", e)  # Debug message
        messagebox.showinfo("Paint app:", "Error occurred")


 
def clear():
    if messagebox.askokcancel("Paint app" , "Do you want to clear everything?"):
        canvas.delete('all')

def createNew():
    if messagebox.askyesno("Paint app" , "Do you want to save before you clear everything?"):
        saveImage()
    clear()

def help():
    helpText = "1. Draw by holding right button of mouse to create dotted lines.\n2.Click scroll well to put text on Canvas.\n3. Click on Select Color Option select specific color\n4. Click on Clear to clear entire Canvas"
    messagebox.showinfo("Help" , helpText)

def settings():
    messagebox.showwarning("Settings" , "Not Available")

def about():
    messagebox.showinfo("About" , "This paint app is best!")
 

def writeText(event):
    canvas.create_text(event.x , event.y , text=textValue.get())
# ------------------- User Interface -------------------
root = Tk()
# Frame - 1 : Tools 

frame1 = Frame(root, height=100, width=1100)
frame1.grid(row=0, column=0, sticky="nw")


# toolsFrame 

toolsFrame = Frame(frame1 , height=100 , width=100, relief=SUNKEN , borderwidth=3)
toolsFrame.grid(row=0 , column=0 )

pencilButton = Button(toolsFrame , text="Pencil" , width=10 , command=usePencil)
pencilButton.grid(row=0 , column=0)
eraserButton = Button(toolsFrame , text="Eraser" , width=10 , command=useEraser)
eraserButton.grid(row=1 , column=0)
toolsLabel = Label(toolsFrame , text="Tools", width=10)
toolsLabel.grid(row=3 , column=0)

# sizeFrame 

sizeFrame = Frame(frame1 , height=100 , width=100, relief=SUNKEN , borderwidth=3 )
sizeFrame.grid(row=0 , column=1 )

defaultButton = Button(sizeFrame , text="Default" , width=10 , command=usePencil)
defaultButton.grid(row=0 , column=0)
# sizeList = OptionMenu(sizeFrame , stroke_size , *options)
sizeList = OptionMenu(sizeFrame, stroke_size, *options)

sizeList.grid(row=1 , column=0)
sizeLabel = Label(sizeFrame , text="Size", width=10)
sizeLabel.grid(row=2 , column=0)

# colorBoxFrame

colorBoxFrame = Frame(frame1 , height=100 , width=100 ,relief=SUNKEN , borderwidth=3 )
colorBoxFrame.grid(row = 0 , column=2)

colorBoxButton = Button(colorBoxFrame , text="Select Color" , width=10 , command=selectColor)
colorBoxButton.grid(row=0 , column=0)
previousColorButton = Button(colorBoxFrame , text="Previous" , width=10 , command=lambda:stroke_color.set(previousColor.get()))
previousColorButton.grid(row=1 , column=0)
previousColor2Button = Button(colorBoxFrame , text="Previous2" , width=10 , command=lambda:stroke_color.set(previousColor2.get()))
previousColor2Button.grid(row=2 , column=0)

# colorsFrame

colorsFrame = Frame(frame1, height=100 , width=100, relief=SUNKEN , borderwidth=3)
colorsFrame.grid(row = 0 , column=3)

redButton = Button(colorsFrame , text="Red" , bg="red" , width=10 , command=lambda: stroke_color.set("red"))
redButton.grid(row=0 , column=0)
greenButton = Button(colorsFrame , text="Green" , bg="green" , width=10 , command=lambda: stroke_color.set("green"))
greenButton.grid(row=1 , column=0)
blueButton = Button(colorsFrame , text="Blue" , bg="blue" , width=10 , command=lambda: stroke_color.set("blue"))
blueButton.grid(row=2 , column=0)
yellowButton = Button(colorsFrame , text="Yellow" , bg="yellow" , width=10 , command=lambda: stroke_color.set("yellow"))
yellowButton.grid(row=0 , column=1)
orangeButton = Button(colorsFrame , text="Orange" , bg="orange" , width=10 , command=lambda: stroke_color.set("orange"))
orangeButton.grid(row=1 , column=1)
purpleButton = Button(colorsFrame , text="Purple" , bg="purple" , width=10 , command=lambda: stroke_color.set("purple"))
purpleButton.grid(row=2 , column=1)

# saveImageFrame

saveImageFrame = Frame(frame1, height=100 , width=100, relief=SUNKEN , borderwidth=3)
saveImageFrame.grid(row = 0 , column=4)

saveImageButton = Button(saveImageFrame , text="Save" , bg="white" , width=10 , command=saveImage)
saveImageButton.grid(row=0 , column=0)
newImageButton = Button(saveImageFrame , text="New" , bg="white" , width=10 , command=createNew)
newImageButton.grid(row=1 , column=0)
clearImageButton = Button(saveImageFrame , text="Clear" , bg="white" , width=10 , command=clear)
clearImageButton.grid(row=2 , column=0)

# helpSettingFrame

helpSettingFrame = Frame(frame1, height=100 , width=100, relief=SUNKEN , borderwidth=3)
helpSettingFrame.grid(row = 0 , column=5)

helpButton = Button(helpSettingFrame , text="Help" , bg="white" , width=10 , command=help)
helpButton.grid(row=0 , column=0)
settingButton = Button(helpSettingFrame , text="Settings" , bg="white" , width=10 , command=settings)
settingButton.grid(row=1 , column=0)
aboutButton = Button(helpSettingFrame , text="About" , bg="white" , width=10 , command=about)
aboutButton.grid(row=2 , column=0)

# textFrame

textFrame = Frame(frame1, height=100 , width=200, relief=SUNKEN , borderwidth=3)
textFrame.grid(row = 0 , column=6)

textTitleButton = Label(textFrame , text="Write you Text here:" , bg="white" , width=20 )
textTitleButton.grid(row=0 , column=0)
entryButton = Entry(textFrame, textvariable=textValue, bg="white" , width=20 )
entryButton.grid(row=1 , column=0)
clearButton = Button(textFrame , text="Clear" , bg="white" , width=20 , command=lambda:textValue.set(""))
clearButton.grid(row=2 , column=0)

# noteFrame

noteFrame = Frame(frame1, height=100 , width=200, relief=SUNKEN , borderwidth=3)
noteFrame.grid(row = 0 , column=7)

textTitleButton = Text(noteFrame, bg="white" , width=40 , height=4 )
textTitleButton.grid(row=0 , column=0)

# Frame - 2 - Canvas

frame2 = Frame(root , height=500 , width=1100 , bg="yellow")
frame2.grid(row=1 , column=0)

canvas = Canvas(frame2 , height=500 , width=1100 , bg="white" )
canvas.grid(row=0 , column=0)
canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonRelease-1>", paint)
canvas.bind("<B3-Motion>" , paintRight)
canvas.bind("<Button-2>", writeText)

root.resizable(False , False)
# root.mainloop()
# root = Tk()
## exit functionality

def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return
    file.add_command(label='Exit', image=exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q', command=exit_func)
 # print functionality 
def print_file(event=None):
    try:
        print_text = text_editor.get(1.0, tk.END)

        # Create an image with the text content
        img = Image.new('RGB', (800, 600), color='white')
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        draw.text((10, 10), print_text, font=font, fill='black')

        # Save the image to a temporary file in your provided directory
        temp_image_path = os.path.join('C:\\Users\\Hp\\Desktop\\notepad\\light_notpad-main\\icons2', 'printed_image.png')
        img.save(temp_image_path)
        

        # Open the image with the default image viewer
        os.system(f'start {temp_image_path}')

    except Exception as e:
        messagebox.showerror("Print Error", f"An error occurred while trying to print: {str(e)}")



        
############ find functionality

def find_func(event=None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)

    ## frame
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    ## labels
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text= 'Replace')

    ## entry
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    ## button
    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text= 'Replace', command=replace)

    ## label grid
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    ## entry grid
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    ## button grid
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()

## edit commands
edit.add_command(label='Copy', image=copy_icon, compound=tk.LEFT, accelerator='Ctrl+C', command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste', image=paste_icon, compound=tk.LEFT, accelerator='Ctrl+V', command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator='Ctrl+X', command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear All', image=clear_all_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+X', command= lambda:text_editor.delete(1.0, tk.END))
edit.add_command(label='Find', image=find_icon, compound=tk.LEFT, accelerator='Ctrl+F', command = find_func)
file.add_command(label='Print', image=print_icon, compound=tk.LEFT, accelerator='Ctrl+P', command=print_file)
file.add_command(label='Page Setup', image=page_setup_icon, compound=tk.LEFT, accelerator='Ctrl+Shift+P', command=page_setup)
main_menu.add_command(label='Set Header', command=set_header)
main_menu.add_command(label='Set Footer', command=set_footer)
## view check button

show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

# 

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else :
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True


def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else :
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True


view.add_checkbutton(label='Tool Bar',onvalue=True, offvalue=0,variable = show_toolbar, image=tool_bar_icon, compound=tk.LEFT, command=hide_toolbar)
view.add_checkbutton(label='Status Bar',onvalue=1, offvalue=False,variable = show_statusbar, image=status_bar_icon, compound=tk.LEFT, command=hide_statusbar)


## color theme
def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color)
count = 0
for i in color_dict:
    color_theme.add_radiobutton(label = i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT, command=change_theme)
    count += 1


   
# -------------------------------------&&&&&&&& End main menu  functinality&&&&&&&&&&& ----------------------------------

main_application.config(menu=main_menu)

#### bind shortcut keys
main_application.bind("<Control-n>", new_file)
main_application.bind("<Control-o>", open_file)
main_application.bind("<Control-s>", save_file)
main_application.bind("<Control-Alt-s>", save_as)
main_application.bind("<Control-q>", exit_func)
main_application.bind("<Control-f>", find_func)
main_application.bind("<Control-p>", print_file)
main_application.bind("<Control-Shift-p>", page_setup)


root.mainloop()
root = Tk()
main_application.config(menu=main_menu)
# paint_app = PaintApp(root)
main_application.mainloop()


