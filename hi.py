


import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os
from tkinter import PhotoImage
from tkinter import Entry
from tkinter import Canvas,HORIZONTAL
from tkinter import RIDGE,ACTIVE,Tk
from tkinter import GROOVE
from tkinter import END
from tkinter import StringVar
from tkinter import  Scale,Menu,Frame
from tkinter import IntVar,LEFT
from tkinter import LabelFrame 
from tkinter import DISABLED
from tkinter import Label
from tkinter import NORMAL
from tkinter import RAISED
from tkinter import SUNKEN
from tkinter import  Listbox
from tkinter import Toplevel
from tkinter import  Button
from tkinter import time
from tkinter import Checkbutton
from PIL import ImageGrab,ROUND
from tkinter import simpledialog,ImageTk



from PIL import Image, ImageDraw, ImageFont
# selected_effect = tk.StringVar()

main_application = tk.Tk()
selected_effect = tk.StringVar()
main_application.geometry('800x600')
main_application.title('Light Text Editor')
# main_application.wm_iconbitmap(r'C:\Users\Hp\Desktop\notepad\light_notpad-main\icons2\icon.ico')
# main_application = tk.Tk()
# main_application.geometry('800x600')
# main_application.title('Light Text Editor')

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
# main_menu.add_cascade(label='Header/Footer', menu=header_footer_menu) 
# main_menu.add_cascade(label='Page Setup', menu=page_setup_menu)

                
           
            

    

class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Text Editor")

        self.text_editor = tk.Text(self.root)
        self.text_editor.pack(fill=tk.BOTH, expand=True)

        self.bold_btn = tk.Button(self.root, text="Bold", command=self.change_bold)
        self.bold_btn.pack(side=tk.LEFT, padx=5)

        self.italic_btn = tk.Button(self.root, text="Italic", command=self.change_italic)
        self.italic_btn.pack(side=tk.LEFT, padx=5)

        self.header_btn = tk.Button(self.root, text="Set Header", command=self.set_header)
        self.header_btn.pack(side=tk.LEFT, padx=5)

        self.footer_btn = tk.Button(self.root, text="Set Footer", command=self.set_footer)
        self.footer_btn.pack(side=tk.LEFT, padx=5)


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
##############################################

            
            
       


    
    
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
# Function to apply text effects
# def apply_text_effect():
#     try:
#         selected_text = text_editor.get(tk.SEL_FIRST, tk.SEL_LAST)
#         if selected_text:
#             text_editor.tag_add('shadow', tk.SEL_FIRST, tk.SEL_LAST)
#     except tk.TclError:
#         pass
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
# text_editor.tag_configure('shadow', offset=(2, 2), foreground='gray')
# text_editor.tag_configure('shadow', offset=(50, 50), foreground='gray')
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

## save file

def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return

file.add_command(label='Save', image=save_icon, compound=tk.LEFT, accelerator='Ctrl+S', command = save_file)


## save as functionality
def save_as(event=None):
    global url
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
        url.write(content)
        url.close()
    except:
        return


file.add_command(label='Save As', image=new_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+S', command=save_as)
## page setup functionality.
def show_page_setup():
    page_setup_dialog = tk.Toplevel(main_application)
    page_setup_dialog.title("Page Setup")
    page_setup_dialog.geometry('400x300')

    # Page size
    page_size_var = tk.StringVar(value="A4")
    page_size_label = tk.Label(page_setup_dialog, text="Page Size:")
    page_size_label.grid(row=0, column=0, padx=10, pady=5)
    page_size_options = ['A4', 'Letter', 'Custom']
    page_size_dropdown = ttk.Combobox(page_setup_dialog, textvariable=page_size_var, values=page_size_options)
    page_size_dropdown.grid(row=0, column=1, padx=10, pady=5)

    # Margins
    margins_label = tk.Label(page_setup_dialog, text="Margins:")
    margins_label.grid(row=1, column=0, padx=10, pady=5)
    margin_var = tk.StringVar(value="Normal")
    margins_options = ['Normal', 'Narrow', 'Wide', 'Custom']
    margins_dropdown = ttk.Combobox(page_setup_dialog, textvariable=margin_var, values=margins_options)
    margins_dropdown.grid(row=1, column=1, padx=10, pady=5)

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

    apply_button = tk.Button(page_setup_dialog, text="Apply", command=apply_page_setup)
    apply_button.grid(row=4, column=0, pady=5)

    cancel_button = tk.Button(page_setup_dialog, text="Cancel", command=page_setup_dialog.destroy)
    cancel_button.grid(row=4, column=1, pady=5)

# Add the Page Setup menu item
main_menu.add_cascade(label='Page Setup', menu=page_setup_menu)
page_setup_menu.add_command(label='Page Setup Options', image=page_setup_icon, compound=tk.LEFT, command=show_page_setup)


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
###################################################################################################################3
class Sketch:
    def __init__(self, root):
        #Take window,Window title and Canvas Control
        self.window = root
        self.window.title("Sketch With Sam" + "-----" + "New Window")
        self.make_canvas = Canvas(self.window, width=1080, height=667, bg="white", relief=RIDGE, bd=8)
        self.make_canvas.place(x=0, y=0)

        #All things initialize with NULL
        self.my_menu = None
        self.file_menu = None
        self.edit_menu = None
        self.color_menu = None
        self.option_menu = None
        self.help_menu = None
        self.coord = None
        self.status = None
        self.controller_set = None
        self.line_img = None
        self.make_line = None
        self.das_img = None
        self.pencil_img = None
        self.circle_img = None
        self.selection_img = None
        self.rectangle_img = None
        self.eraser_img = None
        self.text_img = None
        self.delete_seg = None
        self.parallelogram_img = None
        self.traingle_img = None
        self.pentagon_img = None
        self.hexagon_img = None
        self.arrow_img = None
        self.right_angled_traingle_img = None
        self.rounded_rec_img = None
        self.arrow_left_img = None
        self.color_frame = None
        self.choosing_color = None
        self.F = None
        self.O = None
        self.color = None
        self.permanent_color = None
        self.segment_1 = None
        self.eraser = None
        self.segment_2 = None
        self.top = None
        self.text_collection = None
        self.make_width_frame = None
        self.shape_outline_width_label = None
        self.eraser_width_label = None
        self.eraser_controller = None
        self.color_box = None
        self.color_box_img = None
        self.notation_box = None
        # Coordinate controller value initialization
        self.old_x = None
        self.old_y = None
        self.new_x = None
        self.new_y = None

        #All initialize Buttons
        self.pencil = Button(self.window)
        self.circle = Button(self.window)
        self.selection_btn = Button(self.window)
        self.rec = Button(self.window)
        self.straight_line = Button(self.window)
        self.bent_line = Button(self.window)
        self.dashed_text_btn = Button(self.window)
        self.parallelogram_btn = Button(self.window)
        self.traingle_btn = Button(self.window)
        self.pentagon_btn = Button(self.window)
        self.hexagon_btn = Button(self.window)
        self.arr_btn = Button(self.window)
        self.text_btn = Button(self.window)
        self.right_angled_traingle_btn = Button(self.window)
        self.arr_left_btn = Button(self.window)
        self.rounded_rec_btn = Button(self.window)

        #All initialize lists
        self.img_container = []
        self.cut_copy_img = []
        self.undo_container = []
        self.temp = []
        self.color_container = []
        self.menu_img_container = []
        self.about_img = []

        #All scale initialization under Text button
        self.font_size = Scale(self.top)
        self.font_size.set(20)

        #Input variable initialization
        self.fill_information = IntVar()
        self.outline_information = IntVar()
        self.input_take = StringVar()
        self.fill_information.set(0)
        self.outline_information.set(0)
        self.input_take.set(" ")

        #By default set color
        self.fill_color = "#FFFFFF"
        self.fill_color_line = "black"
        self.outline_color_line = "black"
        self.text_fg = "black"
        self.color_container_box = "black"

        #Some value initialization
        self.color_circle_width_maintainer = 15
        self.img_counter = -1
        self.width_controller_scale = 0
        self.counter = -1
        self.width_maintainer = 2
        self.erase_width_maintainer = 5
        self.active_coloring = 2

        #Some default function call
        self.control(1)#Make sure that canvas will available to use of pencil by default
        self.controller()
        self.make_menu()
        self.make_status_bar()
        self.width_controller()
        self.color_set()
        self.make_canvas.bind("<Control-MouseWheel>",self.zoom_controller)
        self.make_canvas.bind('<Shift-MouseWheel>',self.color_box_width_controller)
        self.make_canvas.bind('<Motion>',self.movement_cursor)

    #Take Control on the functionality
    def control(self,notation):
        if self.temp:
            self.make_canvas.delete(self.temp.pop())
        if self.notation_box:
            if self.notation_box['state'] == DISABLED:
                self.notation_box['state'] = NORMAL
        self.make_canvas.config(cursor="TCROSS")
        self.make_canvas.unbind("<B1-Motion>")
        self.make_canvas.unbind("<ButtonRelease-1>")
        self.make_canvas.unbind("<Button-1>")
        if notation == 1:
            self.make_canvas.bind("<B1-Motion>", self.draw_with_pencil)
        elif notation == 2:
            self.make_canvas.bind("<B1-Motion>", self.circle_ranging)
        elif notation == 3:
            self.make_canvas.bind("<B1-Motion>", self.rectangle_ranging)
        elif notation == 4:
            self.make_canvas.bind("<B1-Motion>", self.bent_line_ranging)
            self.make_canvas.bind("<Shift-B1-Motion>", self.straight_line_ranging)
        elif notation == 5:
            self.make_canvas.config(cursor="dotbox")
            self.make_canvas.bind("<B1-Motion>", self.erasing_setup)
        elif notation == 6:
            self.text_creation_input_take()
        elif notation == 7:
            self.make_canvas.bind('<B1-Motion>', self.traingle_ranging)
        elif notation == 8:
            self.make_canvas.bind('<B1-Motion>', self.parallelogram_ranging)
        elif notation == 9:
            self.make_canvas.bind('<B1-Motion>', self.pentagon_ranging)
        elif notation == 10:
            self.make_canvas.bind('<B1-Motion>', self.hexagon_ranging)
        elif notation == 11:
            self.make_canvas.bind('<B1-Motion>', self.arrow_up_down_ranging)
        elif notation == 12:
            self.make_canvas.bind('<B1-Motion>', self.dashed_line_ranging)
        elif notation == 13:
            self.make_canvas.bind('<B1-Motion>', self.select_region)
            self.window.bind('<Delete>', self.delete_selected_region)
        elif notation == 14:
            self.make_canvas.config(cursor="circle")
            self.color_container_box = colorchooser.askcolor()[1]
            self.make_canvas.bind('<B1-Motion>', self.color_boxer)
        elif notation == 15:
            self.make_canvas.bind('<B1-Motion>', self.arrow_left_right_ranging)
        elif notation == 16:
            self.make_canvas.bind('<B1-Motion>',self.rounded_rectangle_ranging)
        elif notation == 17:
            self.make_canvas.bind('<B1-Motion>',self.right_angled_traingle_ranging)
        elif notation == 18 or notation == 19:
            if notation == 18:
               take = messagebox.askyesno("Clear Conformation","Are you sure to Clear?")
            else:
                take = messagebox.askyesno("New Window Conformation", "Are you really want to open new Window?")
                self.window.title("Sketch With Sam" + "-----" + "New Window")
            if take is True:
               self.make_canvas.delete("all")
               self.clear()
        elif notation == 20:
            take = messagebox.askyesno("Exit Conformation", "Are you sure to Exit?")
            if take is True:
                self.window.destroy()
        elif notation == 21:
            take = colorchooser.askcolor()[1]
            if take:
                self.make_canvas['bg'] = take
                self.make_canvas.update()
        elif notation == 22:
            messagebox.showinfo("Movement Direction","At first click on the shape or line number from indexing box\n\n1. Right Arrow---->  Right Movement\n\n2. Left Arrow----> Left Movement\n\n3. Up Arrow---->Up Movement\n\n4. Down Arrow--->Down Movement\n\n5. Space Button--->Stop Movement")

    #Controller box setup
    def controller(self):
        self.controller_set = LabelFrame(self.window,text="Controller",bg="orange",fg="blue",width=250,height=684,relief=RAISED,bd=10, font=("Arial", 10, "bold"))
        self.controller_set.place(x=1100,y=0)

        self.notation_box = Listbox(self.controller_set, width=5, height=11, font=("Arial", 10, "bold"), fg="yellow",
                                    bg="brown", relief=SUNKEN, bd=5)
        self.notation_box.place(x=180, y=305)

        self.segment_1 = Label(self.controller_set,text="Shapes and lines",bg="#FF6347",fg="brown",font=("Arial", 12, "bold"),relief=GROOVE,bd=1,padx=10,pady=1)
        self.segment_1.place(x=40,y=3)

        self.line_img = ImageTk.PhotoImage(Image.open("Pictures/line.jpg").resize((20, 20), Image.ANTIALIAS))
        self.straight_line = Button(self.controller_set, image=self.line_img, fg="red", bg="white",
                                    font=("Arial", 10, "bold"), relief=RAISED, bd=3, command=lambda: self.control(4))
        self.straight_line.place(x=10, y=40)

        self.das_img = ImageTk.PhotoImage(Image.open("Pictures/dashed_line.png").resize((20, 20), Image.ANTIALIAS))
        self.dashed_text_btn = Button(self.controller_set, image=self.das_img, fg="red", bg="white",
                                      font=("Arial", 10, "bold"), relief=RAISED, bd=3, command=lambda: self.control(12))
        self.dashed_text_btn.place(x=70, y=40)

        self.rectangle_img = ImageTk.PhotoImage(Image.open("Pictures/rectangle.jpg").resize((20, 20), Image.ANTIALIAS))
        self.rec = Button(self.controller_set, image=self.rectangle_img, fg="red", bg="white", font=("Arial", 10, "bold"),relief=RAISED, bd=3, command=lambda: self.control(3))
        self.rec.place(x=130,y=40)

        self.parallelogram_img = ImageTk.PhotoImage(Image.open("Pictures/parallelogram.png").resize((20, 20), Image.ANTIALIAS))
        self.parallelogram_btn = Button(self.controller_set, image=self.parallelogram_img, fg="red", bg="white",
                                        font=("Arial", 10, "bold"), relief=RAISED, bd=3,
                                        command=lambda: self.control(8))
        self.parallelogram_btn.place(x=190, y=40)

        self.traingle_img = ImageTk.PhotoImage(Image.open("Pictures/traingle.jpg").resize((20, 20), Image.ANTIALIAS))
        self.traingle_btn = Button(self.controller_set, image=self.traingle_img, fg="red", bg="white",
                                   font=("Arial", 10, "bold"), relief=RAISED, bd=3, command=lambda: self.control(7))
        self.traingle_btn.place(x=10, y=100)

        self.pentagon_img = ImageTk.PhotoImage(Image.open("Pictures/pentagon.png").resize((20, 20), Image.ANTIALIAS))
        self.pentagon_btn = Button(self.controller_set, image=self.pentagon_img, fg="red", bg="white",
                                   font=("Arial", 10, "bold"), relief=RAISED, bd=3, command=lambda: self.control(9))
        self.pentagon_btn.place(x=70, y=100)

        self.hexagon_img = ImageTk.PhotoImage(Image.open("Pictures/hexagon.png").resize((20, 20), Image.ANTIALIAS))
        self.hexagon_btn = Button(self.controller_set, image=self.hexagon_img, fg="red", bg="white",
                                   font=("Arial", 10, "bold"), relief=RAISED, bd=3, command=lambda: self.control(10))
        self.hexagon_btn.place(x=130, y=100)

        self.arrow_img = ImageTk.PhotoImage(Image.open("Pictures/arrow.png").resize((20, 20), Image.ANTIALIAS))
        self.arr_btn = Button(self.controller_set, image=self.arrow_img, fg="red", bg="white",
                                  font=("Arial", 10, "bold"), relief=RAISED, bd=3, command=lambda: self.control(11))
        self.arr_btn.place(x=190, y=100)

        self.circle_img = ImageTk.PhotoImage(Image.open("Pictures/circle.png").resize((20, 20), Image.ANTIALIAS))
        self.circle = Button(self.controller_set, image=self.circle_img, bg="white", fg="red",
                             font=("Arial", 10, "bold"), relief=RAISED, bd=3, command=lambda: self.control(2))
        self.circle.place(x=10, y=160)

        self.right_angled_traingle_img = ImageTk.PhotoImage(Image.open("Pictures/right_angled_traingle.png").resize((20, 20), Image.ANTIALIAS))
        self.right_angled_traingle_btn = Button(self.controller_set, image=self.right_angled_traingle_img, fg="red", bg="white",
                                      font=("Arial", 10, "bold"), relief=RAISED, bd=3, command=lambda: self.control(17))
        self.right_angled_traingle_btn.place(x=70, y=160)

        self.rounded_rec_img = ImageTk.PhotoImage(Image.open("Pictures/rounded_rectangle.png").resize((20, 20), Image.ANTIALIAS))
        self.rounded_rec_btn = Button(self.controller_set, image=self.rounded_rec_img, fg="red", bg="white",
                                  font=("Arial", 10, "bold"), relief=RAISED, bd=3, command=lambda: self.control(16))
        self.rounded_rec_btn.place(x=130, y=160)

        self.arrow_left_img = ImageTk.PhotoImage(Image.open("Pictures/left_arrow.png").resize((20, 20), Image.ANTIALIAS))
        self.arr_left_btn = Button(self.controller_set, image=self.arrow_left_img, fg="red", bg="white",
                              font=("Arial", 10, "bold"), relief=RAISED, bd=3, command=lambda: self.control(15))
        self.arr_left_btn.place(x=190, y=160)

        self.segment_2 = Label(self.controller_set, text="Tools Collection", bg="#FF6347", fg="brown",
                               font=("Arial", 12, "bold"), relief=GROOVE, bd=1, padx=10, pady=1)
        self.segment_2.place(x=40, y=210)

        self.pencil_img = ImageTk.PhotoImage(Image.open("Pictures/pencil.png").resize((17, 17), Image.ANTIALIAS))
        self.pencil = Button(self.controller_set, image=self.pencil_img, bg="white", fg="red",
                             font=("Arial", 10, "bold"), relief=RAISED, bd=3, command=lambda: self.control(1))
        self.pencil.place(x=10, y=250)

        self.eraser_img = ImageTk.PhotoImage(Image.open("Pictures/eraser.png").resize((17, 17), Image.ANTIALIAS))
        self.eraser = Button(self.controller_set, image=self.eraser_img, fg="red", bg="white", font=("Arial", 10, "bold"),relief=RAISED, bd=3, command=lambda: self.control(5))
        self.eraser.place(x=60,y=250)

        self.text_img = ImageTk.PhotoImage(Image.open("Pictures/text_pic.png").resize((17, 17), Image.ANTIALIAS))
        self.text_btn = Button(self.controller_set, image=self.text_img, fg="red", bg="white",
                             font=("Arial", 10, "bold"), relief=RAISED, bd=3, command=lambda: self.control(6))
        self.text_btn.place(x=110, y=250)

        self.selection_img = ImageTk.PhotoImage(Image.open("Pictures/selection_box.png").resize((17, 17), Image.ANTIALIAS))
        self.selection_btn = Button(self.controller_set, image=self.selection_img, fg="red", bg="white",
                             font=("Arial", 10, "bold"), relief=RAISED, bd=3, command=lambda: self.control(13))
        self.selection_btn.place(x=160, y=250)

        self.color_box_img = ImageTk.PhotoImage(Image.open("Pictures/color_conatiner.png").resize((17, 17), Image.ANTIALIAS))
        self.color_box = Button(self.controller_set, image=self.color_box_img, fg="red", bg="white",
                             font=("Arial", 10, "bold"), relief=RAISED, bd=3,command=lambda: self.control(14))
        self.color_box.place(x=200, y=250)

        #Movement keyboard setup
        self.window.bind('<space>', self.movement)
        self.window.bind('<Left>', self.movement)
        self.window.bind('<Right>', self.movement)
        self.window.bind('<Up>', self.movement)
        self.window.bind('<Down>', self.movement)

    #Menu setup
    def make_menu(self):
        self.my_menu = Menu(self.window)
        self.window.config(menu=self.my_menu)
        menu_img = ["new_img.jpg", "open_img.jpg", "save_img.png", "exit_img.png", "undo_img.jpg", "clear_img.png", "cut_img.png", "copy_img.jpg", "paste_img.jpg","screenshot_img.jpg", "bgcolor_img.jpg", "fill_outline_img.png", "zoom_in_img.png", "zoom_out_img.png", "colorpen_img.png", "movement_img.png","about_img.jpg"]
        for i in range(17):
            self.menu_img_container.append(i)
            self.menu_img_container[i] = ImageTk.PhotoImage(
                Image.open("Pictures/" + menu_img[i]).resize((30, 30), Image.ANTIALIAS))

        self.file_menu = Menu(self.my_menu,tearoff=False)
        self.my_menu.add_cascade(label="File",menu=self.file_menu)
        self.file_menu.add_command(label="New",accelerator="(Ctrl+N)",command=lambda: self.control(19),image=self.menu_img_container[0],compound=LEFT,background="green",foreground="yellow",font=("Arial",10,"bold"),activebackground="yellow",activeforeground="green")
        self.file_menu.add_command(label="Open",accelerator="(Ctrl+O)",command=lambda: self.open_file(False),image=self.menu_img_container[1],compound=LEFT,background="green",foreground="yellow",font=("Arial",10,"bold"),activebackground="yellow",activeforeground="green")
        self.file_menu.add_command(label="Save",accelerator="(Ctrl+S)",command=lambda: self.save_file(False),state=DISABLED,image=self.menu_img_container[2],compound=LEFT,background="green",foreground="yellow",font=("Arial",10,"bold"),activebackground="yellow",activeforeground="green")
        self.file_menu.add_command(label="Exit",command=lambda: self.control(20),image=self.menu_img_container[3],compound=LEFT,background="green",foreground="yellow",font=("Arial",10,"bold"),activebackground="yellow",activeforeground="green")
        self.window.bind('<Control-Key-n>', lambda e:self.control(19))
        self.window.bind('<Control-Key-o>', self.open_file)
        self.window.bind('<Control-Key-s>', self.save_file)

        self.edit_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=lambda: self.undo(False),accelerator="(Ctrl+Z)",state=DISABLED,image=self.menu_img_container[4],compound=LEFT,background="green",foreground="yellow",font=("Arial",10,"bold"),activebackground="yellow",activeforeground="green")
        self.edit_menu.add_command(label="Clear", command=lambda: self.control(18),state=DISABLED,image=self.menu_img_container[5],compound=LEFT,background="green",foreground="yellow",font=("Arial",10,"bold"),activebackground="yellow",activeforeground="green")
        self.edit_menu.add_command(label="Cut", command=lambda: self.cut(False), accelerator="(Ctrl+X)",state=DISABLED,image=self.menu_img_container[6],compound=LEFT,background="green",foreground="yellow",font=("Arial",10,"bold"),activebackground="yellow",activeforeground="green")
        self.edit_menu.add_command(label="Copy", command=lambda: self.copy(0),accelerator="(Ctrl+C)",state=DISABLED,image=self.menu_img_container[7],compound=LEFT,background="green",foreground="yellow",font=("Arial",10,"bold"),activebackground="yellow",activeforeground="green")
        self.edit_menu.add_command(label="Paste", command=lambda: self.paste(False),accelerator="(Ctrl+V)",state=DISABLED,image=self.menu_img_container[8],compound=LEFT,background="green",foreground="yellow",font=("Arial",10,"bold"),activebackground="yellow",activeforeground="green")
        self.edit_menu.add_command(label="Screen Shot", command=lambda: self.screen_shot_taking(False),accelerator="(Ctrl+Alt+C)",state=DISABLED,image=self.menu_img_container[9],compound=LEFT,background="green",foreground="yellow",font=("Arial",10,"bold"),activebackground="yellow",activeforeground="green")
        self.window.bind("<Control-Key-z>",self.undo)
        self.window.bind("<Control-Key-x>", self.cut)
        self.window.bind("<Control-Key-c>",self.copy)
        self.window.bind("<Control-Key-v>", self.paste)
        self.window.bind("<Control-Alt-Key-c>",self.screen_shot_taking)

        self.color_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Color", menu=self.color_menu)
        self.color_menu.add_command(label="Change Background Color",command=lambda: self.control(21),image=self.menu_img_container[10],compound=LEFT,background="green",foreground="yellow",font=("Arial",10,"bold"),activebackground="yellow",activeforeground="green")
        self.color_menu.add_command(label="Change Permanent Fill and Outline Color", command=self.set_permanent_choose_color,image=self.menu_img_container[11],compound=LEFT,background="green",foreground="yellow",font=("Arial",10,"bold"),activebackground="yellow",activeforeground="green")

        self.option_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Option", menu=self.option_menu)
        self.option_menu.add_command(label="Zoom in",accelerator="(Ctrl+Scroll up)",command=lambda: self.zoom_controller(1),image=self.menu_img_container[12],compound=LEFT,background="green",foreground="yellow",font=("Arial",10,"bold"),activebackground="yellow",activeforeground="green")
        self.option_menu.add_command(label="Zoom out", accelerator="(Ctrl+Scroll down)",command=lambda: self.zoom_controller(0),image=self.menu_img_container[13],compound=LEFT,background="green",foreground="yellow",font=("Arial",10,"bold"),activebackground="yellow",activeforeground="green")
        self.option_menu.add_separator(background="green")
        self.option_menu.add_command(label="Color Pen Width Increase", accelerator="(Shift+Scroll up)", command=lambda: self.color_box_width_controller(1),image=self.menu_img_container[14],compound=LEFT,background="green",foreground="yellow",font=("Arial",10,"bold"),activebackground="yellow",activeforeground="green")
        self.option_menu.add_command(label="Color Pen Width Decrease", accelerator="(Shift+Scroll down)", command=lambda: self.color_box_width_controller(0),image=self.menu_img_container[14],compound=LEFT,background="green",foreground="yellow",font=("Arial",10,"bold"),activebackground="yellow",activeforeground="green")
        self.option_menu.add_separator(background="green")
        self.option_menu.add_command(label="Movement", state=DISABLED, command=lambda: self.control(22),image=self.menu_img_container[15],compound=LEFT,background="green",foreground="yellow",font=("Arial",10,"bold"),activebackground="yellow",activeforeground="green")

        self.help_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About",command=self.about,image=self.menu_img_container[16],compound=LEFT,background="green",foreground="yellow",font=("Arial",10,"bold"),activebackground="yellow",activeforeground="green")
        self.help_menu.add_command(label="Tips", command=self.tips, image=self.menu_img_container[16], compound=LEFT, background="green", foreground="yellow", font=("Arial", 10, "bold"), activebackground="yellow", activeforeground="green")

    def movement_cursor(self, e):#For cursor position by movement
        self.coord.config(text=str(e.x) + "," + str(e.y) + "px")

    def make_status_bar(self):#Make status bar
        self.status = Label(self.window, text="Sketch With Passion", fg="#292929", bg="#707070", font=("Arial", 12, "bold"))
        self.status.place(x=1150, y=685)

        self.coord = Label(self.window, text="", fg="#292929", bg="#707070", font=("Arial", 9, "bold"))
        self.coord.place(x=20, y=687)

    def open_file(self,e):#For open a file
        self.status['text'] = "Open a File"
        if self.notation_box['state'] == DISABLED:
            self.notation_box['state'] = NORMAL
        self.make_canvas.unbind("<B1-Motion>")
        self.make_canvas.unbind("<ButtonRelease-1>")
        self.make_canvas.unbind("<Button-1>")

        image_mine = filedialog.askopenfilename(initialdir="\Desktop", title="Select an image",filetypes=(("JPEG Images", "*.jpg"), ("All images", "*.*")))

        if image_mine:
            self.img_container.append(ImageTk.PhotoImage(Image.open(image_mine)))
            self.img_counter+=1
            take = self.make_canvas.create_image(100, 200, image=self.img_container[self.img_counter])
            self.undo_container.append(take)
            self.notation_box.insert(END,len(self.undo_container)-1)
            self.reset()
        self.control(1)

    def save_file(self,e):#for save a file
        self.status['text'] = "Save current file"
        self.status.place(x=1150, y=685)
        file = filedialog.asksaveasfilename(initialdir="Saved_file",filetypes=[("PNG File","*.png")])
        if file:
            x = self.window.winfo_rootx() + self.make_canvas.winfo_x()+10
            y = self.window.winfo_rooty() + self.make_canvas.winfo_y()+10
            x1 = x + self.make_canvas.winfo_width()-20
            y1 = y + self.make_canvas.winfo_height()-20
            ImageGrab.grab().crop((x,y,x1,y1)).save(file+'.png')
            self.window.title("Sketch With Sam" + "-----" + file + ".png")

    def undo(self,e):#For undo
        self.status['text'] = "Undo"
        self.status.place(x=1200, y=685)
        if self.notation_box:
            if self.notation_box['state'] == DISABLED:
                self.notation_box['state'] = NORMAL
            self.notation_box.delete(END)
        if self.undo_container:
            take = self.undo_container.pop()
            if type(take) == list:
                for x in take:
                    self.make_canvas.delete(x)
            else:
                self.make_canvas.delete(take)
        if len(self.undo_container) == 0:
            self.clear()

    def clear(self):#For clear the canvas
        self.undo_container.clear()
        self.notation_box.delete(0, END)
        self.file_menu.entryconfig("Save", state=DISABLED)
        self.edit_menu.entryconfig("Undo", state=DISABLED)
        self.edit_menu.entryconfig("Clear", state=DISABLED)
        self.edit_menu.entryconfig("Cut", state=DISABLED)
        self.edit_menu.entryconfig("Copy", state=DISABLED)
        self.edit_menu.entryconfig("Paste", state=DISABLED)
        self.edit_menu.entryconfig("Screen Shot", state=DISABLED)
        self.option_menu.entryconfig("Movement", state=DISABLED)
        self.temp.clear()
        self.img_container.clear()
        self.cut_copy_img.clear()
        self.img_counter = -1
        self.counter = -1

    def cut(self,e):#Cut the selected region
        self.copy(1)
        self.delete_selected_region(False)
        self.status['text'] = "Selected region cut successfully"
        self.status.place(x=1120, y=685)

    def copy(self,e):#Copy the selected region
        try:
            if e!=1:
               self.make_canvas.delete(self.temp.pop())
               self.status['text'] = "Selected region copied"
               self.status.place(x=1140, y=685)
            else:
               self.make_canvas.itemconfig(self.temp[len(self.temp)-1],outline="white")
            time.sleep(0.0001)
            self.make_canvas.update()
            x1 = self.window.winfo_rootx() + self.make_canvas.winfo_x()
            y1 = self.window.winfo_rooty() + self.make_canvas.winfo_y()
            ImageGrab.grab().crop((x1 + self.old_x, y1 + self.old_y, x1 + self.new_x, y1 + self.new_y)).save("cutting.png")
            self.counter += 1
            self.reset()

        except:
            if e == 1:
                messagebox.showerror("Cut Error","Select a region by selector tool under 'Tools Collection', then cut the selected region")
                print("Cut error")
            else:
                messagebox.showerror("Copy Error","Select a region by selector tool under 'Tools Collection', then copy the selected region")
                print("Copy error")

    def paste(self,e):#Paste the region keep in clipboard
        try:
            if self.notation_box['state'] == DISABLED:
                self.notation_box['state'] = NORMAL
            self.cut_copy_img.append(ImageTk.PhotoImage(Image.open("cutting.png")))
            take = self.make_canvas.create_image(100, 200, image=self.cut_copy_img[self.counter])
            self.undo_container.append(take)
            self.notation_box.insert(END, len(self.undo_container) - 1)
            self.status['text'] = "Paste on the screen"
        except:
            print("Paste Error")

    def select_region(self,e):#For select a region
        try:
            self.status['text'] = "Select a particular region"
            if self.old_x and self.old_y:
               take = self.make_canvas.create_rectangle(self.old_x,self.old_y,e.x,e.y)
               self.temp.append(take)
               def select_region_final(e):
                   for x in self.temp:
                       self.make_canvas.delete(x)
                   self.new_x = e.x
                   self.new_y = e.y
                   self.delete_seg = self.make_canvas.create_rectangle(self.old_x, self.old_y, self.new_x, self.new_y)
                   self.temp.append(self.delete_seg)
               self.make_canvas.bind('<ButtonRelease-1>',select_region_final)
            else:
                self.old_x = e.x
                self.old_y = e.y
        except:
            print("Select region error")

    def delete_selected_region(self,e):#For delete selected region
        self.make_canvas.itemconfig(self.delete_seg,fill="white",width=0.00001,outline="white")
        self.reset()

    def screen_shot_taking(self, e):#For take screen shot
        try:
            self.make_canvas.delete(self.temp.pop())
            time.sleep(0.0000001)
            self.window.update()
            x1 = self.window.winfo_rootx() + self.make_canvas.winfo_x()
            y1 = self.window.winfo_rooty() + self.make_canvas.winfo_y()
            file = filedialog.asksaveasfilename(initialdir="Screen_shots",title="Screen shot save",filetypes=[("PNG File", "*.png")])
            if file:
               ImageGrab.grab().crop((x1 + self.old_x, y1 + self.old_y, x1 + self.new_x, y1 + self.new_y)).save(file+".png")
            self.reset()
            self.status['text'] = "Screen Shot Taken and Saved"
            self.status.place(x=1100,y=685)
        except:
            print("Screen shot Error")
            messagebox.showerror("Selection Error","At first select a region by selector under 'Tools Collection', then take screen shot")

    def zoom_controller(self,e):#For Zoom in and Zoom out
        self.status['text'] = "Zoom Controller"
        self.status.place(x=1160, y=685)
        try:
            if e.delta > 0:
               self.make_canvas.scale("all",e.x,e.y,1.1,1.1)
            elif e.delta<0:
               self.make_canvas.scale("all", e.x, e.y, 0.9, 0.9)
        except:
            if e == 1:
                self.make_canvas.scale("all", 550, 350, 1.1, 1.1)
            else:
                self.make_canvas.scale("all", 550, 350, 0.9, 0.9)

    def color_boxer(self,e):#Colorbox under 'Tools Collection for pen color'
        self.status['text'] = "Draw with the color pen"
        self.status.place(x=1130,y=685)
        if self.old_x and self.old_y:
            take = self.make_canvas.create_line(self.old_x, self.old_y, e.x, e.y, fill=self.color_container_box,
                                                width=self.color_circle_width_maintainer, smooth=True, capstyle=ROUND)
            self.temp.append(take)

        self.old_x = e.x
        self.old_y = e.y
        def color_input(e):
            self.undo_container.append(self.temp)
            self.notation_box.insert(END, len(self.undo_container) - 1)
            self.reset()
        self.make_canvas.bind("<ButtonRelease-1>", color_input)

    def color_box_width_controller(self,e):#Color box width maintain by keyboard event or mouse event
        try:
            print(e)
            if e.delta>0:
                self.color_circle_width_maintainer += 3
            else:
                self.color_circle_width_maintainer -= 3
        except:
            if e == 1:
                self.color_circle_width_maintainer += 3
            else:
                self.color_circle_width_maintainer -= 3

    def reset(self):#Reset
        self.status['text'] = "Sketch With Passion"
        self.status.place(x=1140, y=685)
        if self.notation_box:
            self.file_menu.entryconfig("Save", state=NORMAL)
            self.edit_menu.entryconfig("Undo",state=NORMAL)
            self.edit_menu.entryconfig("Clear", state=NORMAL)
            self.edit_menu.entryconfig("Cut", state=NORMAL)
            self.edit_menu.entryconfig("Copy", state=NORMAL)
            self.edit_menu.entryconfig("Paste", state=NORMAL)
            self.edit_menu.entryconfig("Screen Shot", state=NORMAL)
            self.option_menu.entryconfig("Movement", state=NORMAL)
            if self.notation_box['state'] == DISABLED:
                self.notation_box['state'] = NORMAL
        self.new_x = None
        self.new_y = None
        self.old_x = None
        self.old_y = None
        self.temp=[]

    def draw_with_pencil(self,e):#Draw with pencil
        self.status['text'] = "Draw with the Pencil"
        self.status.place(x=1130, y=685)
        if self.old_x and self.old_y:
           take =self.make_canvas.create_line(self.old_x,self.old_y,e.x,e.y,fill=self.fill_color_line,
                                            width=self.width_maintainer,smooth=True,capstyle=ROUND)
           self.temp.append(take)

        self.old_x = e.x
        self.old_y = e.y

        def push_value(e):
            self.undo_container.append(self.temp)
            self.notation_box.insert(END, len(self.undo_container) - 1)
            self.reset()

        self.make_canvas.bind("<ButtonRelease-1>", push_value)

    def erasing_setup(self,e):#For eraser
        self.status['text'] = "Erasing"
        self.status.place(x=1180, y=685)
        if self.old_x and self.old_y:
           take =self.make_canvas.create_rectangle(self.old_x,self.old_y,e.x,e.y,width=self.erase_width_maintainer,fill="white",outline="white")
           self.temp.append(take)

        self.old_x = e.x
        self.old_y = e.y

        def real_erasing(e):
            self.undo_container.append(self.temp)
            self.notation_box.insert(END, len(self.undo_container) - 1)
            self.reset()

        self.make_canvas.bind("<ButtonRelease-1>", real_erasing)

    def text_creation_input_take(self):#Text Creation
        def message_show():
            messagebox.showinfo("Done","Click on targeting position on the main window to input text")
        self.status['text'] = "Make your own Text"
        self.status.place(x=1130, y=685)
        self.top = Toplevel()
        self.top.title("Text here")
        self.top.geometry("400x500")
        self.top.wm_iconbitmap("Icons/main_logo.ico")
        self.top.config(bg="brown")
        label_1 = Label(self.top,text="Enter the text",font=("Arial",25,"bold"),fg="#00FFFF",bg="brown")
        label_1.pack(pady=20)
        entry_take = Entry(self.top,width=20,font=("Arial",20,"bold","italic"),bg="chocolate",fg="green",textvar=self.input_take,relief=SUNKEN,bd=10)
        entry_take.pack(pady=10)
        entry_take.focus()
        ok_btn = Button(self.top, text="OK", fg="red", bg="black",width=10,
                             font=("Arial", 15, "bold"), relief=RAISED, bd=5, command=message_show)
        ok_btn.pack(pady=20)

        self.text_collection = Listbox(self.top,width=17,height=9,font=("Arial",13,"bold"),bg="chocolate",fg="yellow",relief=SUNKEN,bd=8)
        self.text_collection.place(x=10,y=280)

        text_list = ["Arial","Courier New","Cosmic Sans MS","Fixedsys","MS Sans Serif","System","Verdana","Times New Roman","Symbol"]

        for x in text_list:
            self.text_collection.insert(END,x)

        self.text_collection.activate(0)
        self.text_collection.selection_set(0)

        def color_choose():#For text color set
            self.text_fg = colorchooser.askcolor()[1]


        color_chooser = Button(self.top, text="Text Color", fg="yellow", bg="chocolate",
                              font=("Arial", 15, "bold"), relief=RAISED, bd=5, command=color_choose)
        color_chooser.place(x=200,y=280)

        self.font_size = Scale(self.top,from_=1,to=100,orient=HORIZONTAL,bg="green",fg="yellow",font=("Arial",10,"bold"),activebackground="red")
        self.font_size.place(x=200,y=433)

        def text_creation(e):#For make text on the screen by click
            take = self.make_canvas.create_text(e.x, e.y, text=self.input_take.get(), font=(self.text_collection.get(ACTIVE), self.font_size.get(), "bold", "italic"), fill=self.text_fg)
            self.undo_container.append(take)
            self.notation_box.insert(END, len(self.undo_container) - 1)
            self.input_take.set(" ")
            self.top.destroy()

        self.make_canvas.bind("<Button-1>", text_creation)

    def circle_ranging(self,e):#Make Circle
        self.status['text'] = "Draw Circle"
        self.status.place(x=1200, y=685)
        if self.old_x and self.old_y:
            take = self.make_canvas.create_oval(self.old_x, self.old_y, e.x, e.y, width=self.width_maintainer,outline=self.outline_color_line,fill=self.fill_color)
            self.temp.append(take)
        else:
            self.old_x = e.x
            self.old_y = e.y

        def circle_make(e):
            for x in self.temp:
                self.make_canvas.delete(x)

            try:
                take = self.make_canvas.create_oval(self.old_x, self.old_y, e.x, e.y, width=self.width_maintainer,
                                                    fill=self.fill_color, outline=self.outline_color_line)
                self.undo_container.append(take)
                self.notation_box.insert(END, len(self.undo_container) - 1)
                self.reset()
            except:
                print("Error: click only not motion")

        self.make_canvas.bind('<ButtonRelease-1>',circle_make)

    def rectangle_ranging(self,e):#Rectangle Make
        self.status['text'] = "Draw Rectangle"
        self.status.place(x=1200, y=685)
        if self.old_x and self.old_y:
            take = self.make_canvas.create_rectangle(self.old_x, self.old_y, e.x, e.y, width=self.width_maintainer,fill=self.fill_color,outline=self.outline_color_line)
            self.temp.append(take)
        else:
            self.old_x = e.x
            self.old_y = e.y

        def rectangle_make(e):
            for x in self.temp:
                self.make_canvas.delete(x)
            try:
                take = self.make_canvas.create_rectangle(self.old_x, self.old_y, e.x, e.y, width=self.width_maintainer,
                                                         fill=self.fill_color, outline=self.outline_color_line)
                self.undo_container.append(take)
                self.notation_box.insert(END, len(self.undo_container) - 1)
                self.reset()
            except:
                print("Error: click only not motion")

        self.make_canvas.bind('<ButtonRelease-1>',rectangle_make)

    def straight_line_ranging(self,e):#Straight line make
        self.status['text'] = "Draw Straight line"
        self.status.place(x=1160, y=685)
        if self.old_x and self.old_y:
            if e.x-self.old_x>e.y-self.old_y:
               take = self.make_canvas.create_line(self.old_x, self.old_y, e.x, self.old_y, width=self.width_maintainer,fill=self.fill_color_line)
               self.temp.append(take)
            else:
               take = self.make_canvas.create_line(self.old_x, self.old_y, self.old_x, e.y, width=self.width_maintainer,fill=self.fill_color_line)
               self.temp.append(take)
        else:
            self.old_x=e.x
            self.old_y=e.y

        def straight_line_make(e):
            for x in self.temp:
                self.make_canvas.delete(x)

            try:
                if e.x - self.old_x > e.y - self.old_y:
                    take = self.make_canvas.create_line(self.old_x, self.old_y, e.x, self.old_y,
                                                        width=self.width_maintainer, fill=self.fill_color_line)
                else:
                    take = self.make_canvas.create_line(self.old_x, self.old_y, self.old_x, e.y,
                                                        width=self.width_maintainer, fill=self.fill_color_line)
                self.undo_container.append(take)
                self.notation_box.insert(END, len(self.undo_container) - 1)
                self.reset()
            except:
                print("Error: click only not motion")

        self.make_canvas.bind('<Shift-ButtonRelease-1>',straight_line_make)

    def bent_line_ranging(self,e):#Bent line make
        self.status['text'] = "Draw bent line"
        self.status.place(x=1160, y=685)
        if self.old_x and self.old_y:
            take = self.make_canvas.create_line(self.old_x, self.old_y, e.x, e.y, width=self.width_maintainer, fill=self.fill_color_line)
            self.temp.append(take)
        else:
            self.old_y=e.y
            self.old_x=e.x

        def bent_line_make(e):
            for x in self.temp:
                self.make_canvas.delete(x)
            try:
                take = self.make_canvas.create_line(self.old_x, self.old_y, e.x, e.y, width=self.width_maintainer,
                                                    fill=self.fill_color_line, capstyle=ROUND)
                self.undo_container.append(take)
                self.notation_box.insert(END, len(self.undo_container) - 1)
                self.reset()
            except:
                print("Error: click only not motion")

        self.make_canvas.bind('<ButtonRelease-1>',bent_line_make)

    def dashed_line_ranging(self,e):#Dash line make
        self.status['text'] = "Draw Dash line"
        self.status.place(x=1160, y=685)
        if self.old_x and self.old_y:
            take = self.make_canvas.create_line(self.old_x, self.old_y, e.x, e.y, width=self.width_maintainer, fill=self.fill_color_line, dash=(10,1))
            self.temp.append(take)
        else:
            self.old_y=e.y
            self.old_x=e.x

        def dashed_line_make(e):
            for x in self.temp:
                self.make_canvas.delete(x)
            try:
                take = self.make_canvas.create_line(self.old_x, self.old_y, e.x, e.y, width=self.width_maintainer,
                                                    fill=self.fill_color_line, capstyle=ROUND, dash=(10, 1))
                self.undo_container.append(take)
                self.notation_box.insert(END, len(self.undo_container) - 1)
                self.reset()
            except:
                print("Error: click only not motion")

        self.make_canvas.bind('<ButtonRelease-1>',dashed_line_make)

    def traingle_ranging(self, e):#Traingle make
        self.status['text'] = "Draw Traingle"
        self.status.place(x=1160, y=685)
        if self.old_x and self.old_y:
            take = self.make_canvas.create_polygon(self.old_x, self.old_y, self.old_x-(e.x-self.old_x), e.y, e.x, e.y,width=self.width_maintainer, fill=self.fill_color,outline=self.outline_color_line)
            self.temp.append(take)
        else:
            self.old_x=e.x
            self.old_y=e.y

        def traingle_make(e):
            for x in self.temp:
                self.make_canvas.delete(x)
            try:
                take = self.make_canvas.create_polygon(self.old_x, self.old_y, self.old_x - (e.x - self.old_x), e.y, e.x,
                                                       e.y, width=self.width_maintainer, fill=self.fill_color,
                                                       outline=self.outline_color_line)
                self.undo_container.append(take)
                self.notation_box.insert(END, len(self.undo_container) - 1)
                self.reset()
            except:
                print("Error: click only not motion")

        self.make_canvas.bind('<ButtonRelease-1>', traingle_make)

    def parallelogram_ranging(self, e):#Parallelogram make
        self.status['text'] = "Draw a Parallelogram"
        self.status.place(x=1130, y=685)
        if self.old_x and self.old_y:
            points = [self.old_x,self.old_y,int(self.old_x)+30,e.y,e.x,e.y,int(e.x)-30,self.old_y]
            take = self.make_canvas.create_polygon(points,width=1, fill=self.fill_color,outline=self.outline_color_line)
            self.temp.append(take)
        else:
            self.old_x=e.x
            self.old_y=e.y

        def parallelogram_make(e):
            for x in self.temp:
                self.make_canvas.delete(x)
            try:
                points = [self.old_x, self.old_y, int(self.old_x) + 30, e.y, e.x, e.y, int(e.x) - 30, self.old_y]
                take = self.make_canvas.create_polygon(points, width=self.width_maintainer, fill=self.fill_color,
                                                       outline=self.outline_color_line)
                self.undo_container.append(take)
                self.notation_box.insert(END, len(self.undo_container) - 1)
                self.reset()
            except:
                print("Error: click only not motion")

        self.make_canvas.bind('<ButtonRelease-1>', parallelogram_make)

    def pentagon_ranging(self, e):#pentagon make
        self.status['text'] = "Draw Pentagon"
        self.status.place(x=1160, y=685)
        if self.old_x and self.old_y:
            points = [self.old_x, self.old_y, int(self.old_x), e.y, e.x, e.y, int(e.x), self.old_y, (self.old_x+e.x)/2,self.old_y-20]
            take = self.make_canvas.create_polygon(points,width=self.width_maintainer, fill=self.fill_color,outline=self.outline_color_line)
            self.temp.append(take)
        else:
            self.old_x=e.x
            self.old_y=e.y

        def pentagon_make(e):
            for x in self.temp:
                self.make_canvas.delete(x)
            try:
                points = [self.old_x, self.old_y, int(self.old_x), e.y, e.x, e.y, int(e.x), self.old_y,
                          (self.old_x + e.x) / 2, self.old_y - 20]
                take = self.make_canvas.create_polygon(points, width=self.width_maintainer, fill=self.fill_color,
                                                       outline=self.outline_color_line)
                self.undo_container.append(take)
                self.notation_box.insert(END, len(self.undo_container) - 1)
                self.reset()
            except:
                print("Error: click only not motion")

        self.make_canvas.bind('<ButtonRelease-1>', pentagon_make)

    def hexagon_ranging(self, e):#Hexagon make
        self.status['text'] = "Draw Hexagon"
        self.status.place(x=1160, y=685)
        if self.old_x and self.old_y:
            points = [self.old_x, self.old_y, int(self.old_x), e.y, (int(self.old_x)+int(e.x))/2, int(e.y)+50, e.x, e.y, int(e.x), self.old_y, (self.old_x+e.x)/2,self.old_y-50]
            take = self.make_canvas.create_polygon(points,width=self.width_maintainer, fill=self.fill_color,outline=self.outline_color_line)
            self.temp.append(take)
        else:
            self.old_x=e.x
            self.old_y=e.y

        def hexagon_make(e):
            for x in self.temp:
                self.make_canvas.delete(x)
            try:
                points = [self.old_x, self.old_y, int(self.old_x), e.y, (int(self.old_x) + int(e.x)) / 2, int(e.y) + 50,
                          e.x, e.y, int(e.x), self.old_y, (self.old_x + e.x) / 2, self.old_y - 50]
                take = self.make_canvas.create_polygon(points, width=self.width_maintainer, fill=self.fill_color,
                                                       outline=self.outline_color_line)
                self.undo_container.append(take)
                self.notation_box.insert(END, len(self.undo_container) - 1)
                self.reset()
            except:
                print("Error: click only not motion")

        self.make_canvas.bind('<ButtonRelease-1>', hexagon_make)


    def arrow_up_down_ranging(self, e):#Arrow up or down make
        self.status['text'] = "Draw Arrow"
        self.status.place(x=1160, y=685)
        if self.old_x and self.old_y:
            points = [self.old_x, self.old_y, (int(self.old_x)+int(self.old_x+e.x)/2)/2, self.old_y, (int(self.old_x)+int(self.old_x+e.x)/2)/2, int(e.y), ((int(self.old_x+e.x)/2)+int(e.x))/2, e.y, ((int(self.old_x+e.x)/2)+int(e.x))/2,self.old_y,  int(e.x),self.old_y,  int(self.old_x+e.x)/2, self.old_y+(int((self.old_y-e.y))/2)]
            take = self.make_canvas.create_polygon(points,width=self.width_maintainer, fill=self.fill_color,outline=self.outline_color_line)
            self.temp.append(take)
        else:
            self.old_x=e.x
            self.old_y=e.y

        def arrow_up_down_make(e):
            for x in self.temp:
                self.make_canvas.delete(x)
            try:
                points = [self.old_x, self.old_y, (int(self.old_x) + int(self.old_x + e.x) / 2) / 2, self.old_y,
                          (int(self.old_x) + int(self.old_x + e.x) / 2) / 2, int(e.y),
                          ((int(self.old_x + e.x) / 2) + int(e.x)) / 2, e.y, ((int(self.old_x + e.x) / 2) + int(e.x)) / 2,
                          self.old_y, int(e.x), self.old_y, int(self.old_x + e.x) / 2,
                          self.old_y + (int((self.old_y - e.y)) / 2)]
                take = self.make_canvas.create_polygon(points, width=self.width_maintainer, fill=self.fill_color,
                                                       outline=self.outline_color_line)
                self.undo_container.append(take)
                self.notation_box.insert(END, len(self.undo_container) - 1)
                self.reset()
            except:
                print("Error: click only not motion")

        self.make_canvas.bind('<ButtonRelease-1>', arrow_up_down_make)

    def right_angled_traingle_ranging(self,e):#Right angled traingle make
        self.status['text'] = "Draw Right Angled Traingle"
        self.status.place(x=1120, y=685)
        if self.old_x and self.old_y:
            points = [self.old_x,self.old_y, self.old_x,e.y, e.x,e.y]
            take = self.make_canvas.create_polygon(points,width=self.width_maintainer, fill=self.fill_color,outline=self.outline_color_line)
            self.temp.append(take)
        else:
            self.old_x=e.x
            self.old_y=e.y

        def right_angled_traingle_make(e):
            for x in self.temp:
                self.make_canvas.delete(x)
            try:
                points = [self.old_x,self.old_y, self.old_x,e.y, e.x,e.y]
                take = self.make_canvas.create_polygon(points, width=self.width_maintainer, fill=self.fill_color,
                                                       outline=self.outline_color_line)
                self.undo_container.append(take)
                self.notation_box.insert(END, len(self.undo_container) - 1)
                self.reset()
            except:
                print("Error: click only not motion")

        self.make_canvas.bind('<ButtonRelease-1>', right_angled_traingle_make)

    def rounded_rectangle_ranging(self,e):#Rounded rectangle make
        self.status['text'] = "Draw Rounded Rectangle"
        self.status.place(x=1120, y=685)
        if self.old_x and self.old_y:
            points = [self.old_x,self.old_y, int(self.old_x)+3,int(self.old_y)-5, int(self.old_x)+7,int(self.old_y)-7, int(self.old_x)+11,int(self.old_y)-9, int(self.old_x)+13,int(self.old_y)-9, e.x,int(self.old_y)-9, int(e.x)+5,int(self.old_y)-7, int(e.x)+8,int(self.old_y)-5, int(e.x)+11,self.old_y, int(e.x)+11,e.y, int(e.x)+8,int(e.y)+5, int(e.x)+5,int(e.y)+7, e.x,int(e.y)+8, int(self.old_x)+13,int(e.y)+8, int(self.old_x)+11,int(e.y)+7, int(self.old_x)+7,int(e.y)+5, int(self.old_x)+3,int(e.y)+3, int(self.old_x),int(e.y)-2]
            take = self.make_canvas.create_polygon(points,width=self.width_maintainer, fill=self.fill_color,outline=self.outline_color_line)
            self.temp.append(take)
        else:
            self.old_x=e.x
            self.old_y=e.y

        def rounded_rectangle_make(e):
            for x in self.temp:
                self.make_canvas.delete(x)
            try:
                points = [self.old_x,self.old_y, int(self.old_x)+3,int(self.old_y)-5, int(self.old_x)+7,int(self.old_y)-7, int(self.old_x)+11,int(self.old_y)-9, int(self.old_x)+13,int(self.old_y)-9, e.x,int(self.old_y)-9, int(e.x)+5,int(self.old_y)-7, int(e.x)+8,int(self.old_y)-5, int(e.x)+11,self.old_y, int(e.x)+11,e.y, int(e.x)+8,int(e.y)+5, int(e.x)+5,int(e.y)+7, e.x,int(e.y)+8, int(self.old_x)+13,int(e.y)+8, int(self.old_x)+11,int(e.y)+7, int(self.old_x)+7,int(e.y)+5, int(self.old_x)+3,int(e.y)+3, int(self.old_x),int(e.y)-2]
                take = self.make_canvas.create_polygon(points, width=self.width_maintainer, fill=self.fill_color,
                                                       outline=self.outline_color_line)
                self.undo_container.append(take)
                self.notation_box.insert(END, len(self.undo_container) - 1)
                self.reset()
            except:
                print("Error: click only not motion")

        self.make_canvas.bind('<ButtonRelease-1>', rounded_rectangle_make)

    def arrow_left_right_ranging(self, e):#Arrow left or right make
        self.status['text'] = "Draw Arrow"
        self.status.place(x=1160, y=685)
        if self.old_x and self.old_y:
            m = (self.old_x + e.x)/2
            points = [self.old_x, self.old_y, int(m), self.old_y+20, int(m), self.old_y+10, e.x, int(self.old_y)+10, e.x, int(self.old_y)-10, int(m), int(self.old_y)-10, int(m), int(self.old_y)-20]
            take = self.make_canvas.create_polygon(points,width=self.width_maintainer, fill=self.fill_color,outline=self.outline_color_line)
            self.temp.append(take)
        else:
            self.old_x=e.x
            self.old_y=e.y

        def arrow_left_right_make(e):
            for x in self.temp:
                self.make_canvas.delete(x)
            try:
                points = [self.old_x, self.old_y, int(m), self.old_y+20, int(m), self.old_y+10, e.x, int(self.old_y)+10, e.x, int(self.old_y)-10, int(m), int(self.old_y)-10, int(m), int(self.old_y)-20]
                take = self.make_canvas.create_polygon(points, width=self.width_maintainer, fill=self.fill_color,
                                                       outline=self.outline_color_line)
                self.undo_container.append(take)
                self.notation_box.insert(END, len(self.undo_container) - 1)
                self.reset()
            except:
                print("Error: click only not motion")

        self.make_canvas.bind('<ButtonRelease-1>', arrow_left_right_make)

    def movement(self,e):#Movement of any widget by selecting indexing number
        try:
            self.status['text'] = "Movement"
            self.status.place(x=1180, y=685)
            take = self.notation_box.get(ACTIVE)
            self.notation_box.config(state=DISABLED)
            take = self.undo_container[take]
            if e.keycode == 32:
                self.notation_box.config(state=NORMAL)
            if e.keycode == 37:
                if type(take) == list:
                    for x in take:
                        self.make_canvas.move(x, -8, 0)
                else:
                    self.make_canvas.move(take, -8, 0)
            if e.keycode == 38:
                if type(take) == list:
                    for x in take:
                        self.make_canvas.move(x, 0, -8)
                else:
                    self.make_canvas.move(take, 0, -8)
            if e.keycode == 39:
                if type(take) == list:
                    for x in take:
                        self.make_canvas.move(x, 8, 0)
                else:
                    self.make_canvas.move(take, 8, 0)
            if e.keycode == 40:
                if type(take) == list:
                    for x in take:
                        self.make_canvas.move(x, 0, 8)
                else:
                    self.make_canvas.move(take, 0, 8)
        except:
            print("Error: Nothing selected from indexing box")

    def width_controller(self):#Width Controller box
        self.make_width_frame = Frame(self.controller_set,relief=GROOVE,bd=5,width=10,height=10,bg="chocolate")
        self.make_width_frame.place(x=10,y=305)

        def shape_outline_width_controller(e):  # Shape Border Width Controller
            self.width_maintainer = e

        def eraser_width_controller(e):  # Eraser width Controller
            self.erase_width_maintainer = e

        self.shape_outline_width_label = Label(self.make_width_frame,text="Outline Width",font=("Arial",12,"bold"),bg="chocolate",fg="yellow",padx=20)
        self.shape_outline_width_label.pack(pady=4)

        self.width_controller_scale = Scale(self.make_width_frame,orient=HORIZONTAL,from_=0,to=100,bg="green",fg="yellow",font=("Arial",8,"bold"),relief=RAISED,bd=3,command=shape_outline_width_controller,activebackground="red")
        self.width_controller_scale.set(self.width_maintainer)
        self.width_controller_scale.pack(pady=7)

        self.eraser_width_label = Label(self.make_width_frame, text="Eraser Width", font=("Arial", 12, "bold"),
                                               bg="chocolate", fg="yellow", padx=20)
        self.eraser_width_label.pack(pady=4)

        self.eraser_controller = Scale(self.make_width_frame, orient=HORIZONTAL, from_=0, to=100, bg="green",activebackground="red",
                                      fg="yellow", font=("Arial", 8, "bold"), relief=RAISED, bd=3, command=eraser_width_controller)
        self.eraser_controller.set(self.erase_width_maintainer)
        self.eraser_controller.pack(pady=7)

    def color_set(self):#Color set from colorbox
        self.color_frame = Frame(self.controller_set, relief=GROOVE, bd=5, width=10, height=10, bg="orange")
        self.color_frame.place(x=10, y=525)

        color_storage = ["red_image.png", "brown_image.png", "blue_img.png", "grey_img.png", "yellow_img.png","green_img.png", "orange_img.png", "black_img.png", "white_img.png", "pink_img.png","indigo_img.png", "violet_img.png", "light_green.png", "olive_img.png", "choose_color.png"]

        for i in range(15):
            self.color_container.append(i)
            self.color_container[i] = ImageTk.PhotoImage(Image.open("Pictures/" + color_storage[i]).resize((15, 15), Image.ANTIALIAS))

        self.color = Button(self.color_frame, image=self.color_container[0], relief=RAISED, bd=2, bg="black",command=lambda: self.check(0,self.active_coloring))
        self.color.grid(row=0, column=0, padx=5, pady=8)

        self.color = Button(self.color_frame, image=self.color_container[1], relief=RAISED, bd=2, bg="black",
                            command=lambda: self.check(1,self.active_coloring))
        self.color.grid(row=0, column=1, padx=5, pady=8)

        self.color = Button(self.color_frame, image=self.color_container[2], relief=RAISED, bd=2, bg="black",
                            command=lambda: self.check(2,self.active_coloring))
        self.color.grid(row=0, column=2, padx=5, pady=8)

        self.color = Button(self.color_frame, image=self.color_container[3], relief=RAISED, bd=2, bg="black",
                            command=lambda: self.check(3,self.active_coloring))
        self.color.grid(row=0, column=3, padx=5, pady=8)

        self.color = Button(self.color_frame, image=self.color_container[4], relief=RAISED, bd=2, bg="black",
                            command=lambda: self.check(4,self.active_coloring))
        self.color.grid(row=0, column=4, padx=5, pady=8)

        self.color = Button(self.color_frame, image=self.color_container[5], relief=RAISED, bd=2, bg="black",
                            command=lambda: self.check(5,self.active_coloring))
        self.color.grid(row=1, column=0, padx=5, pady=8)

        self.color = Button(self.color_frame, image=self.color_container[6], relief=RAISED, bd=2, bg="black",
                            command=lambda: self.check(6,self.active_coloring))
        self.color.grid(row=1, column=1, padx=5, pady=8)

        self.color = Button(self.color_frame, image=self.color_container[7], relief=RAISED, bd=2, bg="black",
                            command=lambda: self.check(7,self.active_coloring))
        self.color.grid(row=1, column=2, padx=5, pady=8)

        self.color = Button(self.color_frame, image=self.color_container[8], relief=RAISED, bd=2, bg="black",
                            command=lambda: self.check(8,self.active_coloring))
        self.color.grid(row=1, column=3, padx=5, pady=8)

        self.color = Button(self.color_frame, image=self.color_container[9], relief=RAISED, bd=2, bg="black",
                            command=lambda: self.check(9,self.active_coloring))
        self.color.grid(row=1, column=4, padx=5, pady=8)

        self.color = Button(self.color_frame, image=self.color_container[10], relief=RAISED, bd=2, bg="black",
                            command=lambda: self.check(10,self.active_coloring))
        self.color.grid(row=2, column=0, padx=5, pady=8)

        self.color = Button(self.color_frame, image=self.color_container[11], relief=RAISED, bd=2, bg="black",
                            command=lambda: self.check(11,self.active_coloring))
        self.color.grid(row=2, column=1, padx=5, pady=8)

        self.color = Button(self.color_frame, image=self.color_container[12], relief=RAISED, bd=2, bg="black",
                            command=lambda: self.check(12,self.active_coloring))
        self.color.grid(row=2, column=2, padx=5, pady=8)

        self.color = Button(self.color_frame, image=self.color_container[13], relief=RAISED, bd=2, bg="black",
                            command=lambda: self.check(13,self.active_coloring))
        self.color.grid(row=2, column=3, padx=5, pady=8)

        self.color = Button(self.color_frame, image=self.color_container[14], relief=RAISED, bd=2, bg="black",
                            command=lambda: self.check(14,self.active_coloring))
        self.color.grid(row=2, column=4, padx=5, pady=8)


        self.F = Button(self.color_frame, text="F", relief=RAISED, bd=2, bg="#262626", width=4, height=1, fg="#00FF00",
                            command=lambda: self.activate_coloring(1))
        self.F.grid(row=0, column=5,padx=6)

        self.O = Button(self.color_frame, text="O", relief=RAISED, bd=2, bg="#262626",width=4, height=1, fg="#00FF00",
                        command=lambda: self.activate_coloring(2))
        self.O.grid(row=1, column=5, padx=6)

        self.permanent_color = Button(self.color_frame, text="P", relief=RAISED, bd=2, bg="#262626", width=4, height=1, fg="#00FF00",
                                      command=self.set_permanent_choose_color)
        self.permanent_color.grid(row=2, column=5)

    def set_permanent_choose_color(self):#Set permanent color: border and background
        self.status['text'] = "Set Permanent Fill and Outline Color"
        self.status.place(x=1120, y=685)
        top = Toplevel()
        top.config(bg="orange")
        top.geometry("400x200")
        top.wm_iconbitmap("Icons/main_logo.ico")

        def color_set(choice):#take color and set
            take_color = colorchooser.askcolor()[1]
            if choice == 1:
               self.fill_color = take_color
               self.fill_color_line = take_color
               self.fill_information.set(1)
            else:
               self.outline_color_line = take_color
               self.outline_information.set(1)
            self.window.update()

        fill_check = Checkbutton(top,variable=self.fill_information,text="Permanent fill color",font=("Arial",15,"bold"), bg="orange")
        fill_check.place(x=50,y=20)

        self.choosing_color = ImageTk.PhotoImage(Image.open("Pictures/choose_color.png").resize((15, 15), Image.ANTIALIAS))

        fill_colorchooser = Button(top,image =self.choosing_color, bg="black",command=lambda: color_set(1))
        fill_colorchooser.place(x=280,y=28)

        outline_check = Checkbutton(top,variable=self.outline_information, text="Permanent outline color", font=("Arial", 15, "bold"), bg="orange")
        outline_check.place(x=50,y=80)

        outline_colorchooser = Button(top, image=self.choosing_color, bg="black",command=lambda: color_set(2))
        outline_colorchooser.place(x=320, y=90)

        def message():
            messagebox.showinfo("Information","For any kind of line, only Fill(F) available")

        information = Button(top,text="Information",font=("Arial",15,"bold"),bg="black",fg="red",
                             command=message,relief=RAISED, bd=8)
        information.place(x=50,y=140)

        ok = Button(top, text="OK", font=("Arial", 15, "bold"), bg="black", fg="red",
                             command=top.destroy, relief=RAISED, bd=8)
        ok.place(x=280, y=140)

    def activate_coloring(self,notation):#Colro activation
        if notation == 1:
           self.active_coloring = 1
        else:
           self.active_coloring = 2


    def check(self,number,index):#Color set finally in the widget
        try:
            color_list = ["red","#8B4513","blue","grey","yellow","green","orange","black","white","pink","sky blue","violet","#90EE90","#808000"]
            take = self.undo_container[self.notation_box.get(ACTIVE)]

            if number == 14:
                take_color = colorchooser.askcolor()[1]
            else:
                take_color = color_list[number]

            if index == 1:
                if type(take) == list:
                    for x in take:
                        self.make_canvas.itemconfig(x, fill=take_color)
                else:
                    self.make_canvas.itemconfig(self.undo_container[self.notation_box.get(ACTIVE)], fill=take_color)
            else:
                self.make_canvas.itemconfig(self.undo_container[self.notation_box.get(ACTIVE)], outline=take_color)

            self.status['text'] = "Colored"
            self.status.place(x=1180, y=685)
        except:
            if len(self.undo_container) == 0:
                messagebox.showwarning("Nothing present","Sorry, Nothing present to change color")
            else:
                messagebox.showinfo("Problem Raise","For any kind of lines, only fill(F) allowed")

    def about(self):#About under Help menu
        top = Toplevel()
        top.title("About")
        top.geometry("1350x730")
        top.minsize(1350, 730)
        top.wm_iconbitmap("Icons/main_logo.ico")
        top.config(bg="chocolate")
        img_label_all = []
        des_label_all = []
        self.about_img.clear()
        for i in range(5):
            self.about_img.append(i)
            img_label_all.append(i)
            des_label_all.append(i)
        self.about_img[0] = ImageTk.PhotoImage(Image.open("Pictures/Shapes_and_lines_box.png").resize((200,160),Image.ANTIALIAS))
        self.about_img[1] = ImageTk.PhotoImage(Image.open("Pictures/Tools_collection.png").resize((200, 100), Image.ANTIALIAS))
        self.about_img[2] = ImageTk.PhotoImage(Image.open("Pictures/width_controller.png").resize((140, 160), Image.ANTIALIAS))
        self.about_img[3] = ImageTk.PhotoImage(Image.open("Pictures/Notation_box.png").resize((30, 150), Image.ANTIALIAS))
        self.about_img[4] = ImageTk.PhotoImage(Image.open("Pictures/Color_segment.png").resize((200, 140), Image.ANTIALIAS))

        heading = Label(top, text="All about Tools", font=("Arial", 30, "bold", "italic"),fg="brown", bg="chocolate")
        heading.place(x=550, y=10)

        img_label_all[0] = Label(top,image=self.about_img[0],relief=RAISED,bd=3)
        img_label_all[0].place(x=20,y=40)
        des_label_all[0] = Label(top,text="This box contains all shapes and lines",font=("Arial",30,"bold"),fg="yellow",bg="chocolate")
        des_label_all[0].place(x=250,y=100)

        img_label_all[1] = Label(top, image=self.about_img[1], relief=RAISED, bd=3)
        img_label_all[1].place(x=1130, y=200)
        des_label_all[1] = Label(top, text="This box contains all essential tools", font=("Arial", 30, "bold"),fg="yellow", bg="chocolate")
        des_label_all[1].place(x=430, y=220)

        img_label_all[2] = Label(top, image=self.about_img[2], relief=RAISED, bd=3)
        img_label_all[2].place(x=20, y=290)
        des_label_all[2] = Label(top, text="Width controller box", font=("Arial", 30, "bold"),fg="yellow", bg="chocolate")
        des_label_all[2].place(x=200, y=340)

        img_label_all[3] = Label(top, image=self.about_img[3], relief=RAISED, bd=3)
        img_label_all[3].place(x=1250, y=390)
        des_label_all[3] = Label(top, text="Line and Shape Indexing Box", font=("Arial", 30, "bold"), fg="yellow",bg="chocolate")
        des_label_all[3].place(x=660, y=440)

        img_label_all[4] = Label(top, image=self.about_img[4], relief=RAISED, bd=3)
        img_label_all[4].place(x=20, y=560)
        des_label_all[4] = Label(top, text="Coloring Box", font=("Arial", 30, "bold"), fg="yellow",bg="chocolate")
        des_label_all[4].place(x=250, y=600)

    def tips(self):#Tips under Help menu
        top = Toplevel()
        top.title("About")
        top.geometry("1350x500")
        top.minsize(1350,450)
        top.wm_iconbitmap("Icons/main_logo.ico")
        top.config(bg="chocolate")
        self.about_img.clear()
        self.about_img.append(0)

        heading = Label(top, text="Tips of Sketch With Sam", font=("Arial", 30, "bold", "italic"), fg="brown",
                        bg="chocolate")
        heading.place(x=500, y=10)

        self.about_img[0] = ImageTk.PhotoImage(Image.open("Pictures/line.jpg").resize((20, 20), Image.ANTIALIAS))

        tip_label_img = Label(top, text="Shift + ", font=("Arial", 20, "bold"), fg="yellow", bg="chocolate")
        tip_label_img.place(x=20, y=80)
        tip_label = Label(top, image=self.about_img[0], relief=RAISED, bd=3)
        tip_label.place(x=120, y=85)
        tip_label_img = Label(top, text="====>   Make Straight line: Vertical and Horizontal", font=("Arial", 15, "bold"), fg="green", bg="chocolate")
        tip_label_img.place(x=160, y=85)

        f_lb = Label(top, text="F ====>  For Change Background Color of the Selected Shape or Line", font=("Arial", 15, "bold"), fg="green", bg="chocolate")
        f_lb.place(x=120, y=150)

        l_lb = Label(top, text="O ====>  For Change Outline Color of the Selected Sbape", font=("Arial", 15, "bold"), fg="green", bg="chocolate")
        l_lb.place(x=120, y=225)

        p_lb = Label(top, text="P ====>  For Change Background and Outline Color permanently of the upcoming shapes and lines",font=("Arial", 15, "bold"), fg="green", bg="chocolate")
        p_lb.place(x=120, y=290)

        del_lb = Label(top, text="Select a region + Delete button--->Delete the Segment ",font=("Arial", 15, "bold"), fg="green", bg="chocolate")
        del_lb.place(x=120, y=365)

if __name__ == '__main__':
    window = Tk()
    window.geometry("1350x730")
    window.maxsize(1350,712)
    window.minsize(1350, 712)
    window.wm_iconbitmap("Icons/main_logo.ico")
    window.config(bg="#707070")
    Sketch(window)
    window.mainloop()

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


main_application.mainloop()