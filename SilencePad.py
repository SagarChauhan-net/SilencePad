# Modules used to create the software.....

import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

# Gobale Variables........
application_title_name = "SilencePad text editor"
application_default_resolution = "800x600"
application_default_font = "Barkentina 1"
application_default_font_size = 15
application_default_font_size_index = 7
application_default_background_color = "#2d2d2d"
application_default_foreground_color = "#c4c4c4"


# Setting the Environment....
main_application = tk.Tk()
main_application.geometry(application_default_resolution)
main_application.title(application_title_name)
main_application.wm_iconbitmap("icon.ico")


#________________________________    Main Menu    ______________________________

# Creating main menu object....
main_menu = tk.Menu()


# .... File Menu STARTS ....

# Creating file menu object.....
file_menu = tk.Menu(main_menu, tearoff=False)

# File menu icons
# Setting all the icons for file menu....
new_icon = tk.PhotoImage(file="icons/new.png")
open_icon = tk.PhotoImage(file="icons/open.png")
save_icon = tk.PhotoImage(file="icons/save.png")
save_as_icon = tk.PhotoImage(file="icons/save_as.png")
exit_icon = tk.PhotoImage(file="icons/exit.png")

# .... File Menu ENDS ....


# ... Edit Menu STARTS ...

# Creating object for the edit menu...
edit_menu = tk.Menu(main_menu, tearoff=False)

# Edit Menu Icons...
copy_icon = tk.PhotoImage(file="icons/copy.png")
paste_icon = tk.PhotoImage(file="icons/paste.png")
cut_icon = tk.PhotoImage(file="icons/cut.png")
clear_all_icon = tk.PhotoImage(file="icons/clear_all.png")
find_icon = tk.PhotoImage(file="icons/find.png")

# ... Edit Menu ENDS ...


# ... View Menu STARTS ...

# Creating View menu Object...
view_menu = tk.Menu(main_menu, tearoff=False)

# View Menu Icons...
tool_bar_icon = tk.PhotoImage(file="icons/tool_bar.png")
status_bar_icon = tk.PhotoImage(file="icons/status_bar.png")

# ... View Menu ENDS ...

# ... Color Theme STARTS ...

# Creating color theme object...
color_theme_menu = tk.Menu(main_menu, tearoff=False)

# Color theme Icons....
light_default_icon = tk.PhotoImage(file="icons/light_default.png")
light_plus_icon = tk.PhotoImage(file="icons/light_plus.png")
dark_icon = tk.PhotoImage(file="icons/dark.png")
red_icon = tk.PhotoImage(file="icons/red.png")
monokai_icon = tk.PhotoImage(file="icons/monokai.png")
night_blue_icon = tk.PhotoImage(file="icons/night_blue.png")

# Writing Some Logic for color theme....

# Creating a varibale to track the theme choice...
theme_choice = tk.StringVar()

# Creating a tuple to keep track of the theme ICONS and easily assine them....
color_theme_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon,
                     monokai_icon, night_blue_icon)

# Creating a Dictionary to store the color of the text and the backgroud in certain cases...
color_theme_dict = {
    "Light Default" : ('#000000', '#ffffff'),
    "Light Plus" : ('#474747', '#e0e0e0'),
    "Dark" : ('#c4c4c4', '#2d2d2d'),
    "Red" : ('#2d2d2d', '#ffe8e8'),
    "Monokai" : ('#d3b774', '#474747'),
    "Night Blue" : ('#ededed', '#6b9dc2')
}

# ... Color Theme ENDS ...

# Cascade - adding these menu to the main menu on the screen
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit", menu=edit_menu)
main_menu.add_cascade(label="View", menu=view_menu)
main_menu.add_cascade(label="Color Theme", menu=color_theme_menu)

#-------------------------------- End main menu --------------------------------


#________________________________   toolbar   __________________________________

# Creating the label to put the toolbar on it...
tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)

# .... Font box STARTS ....

# Creating a tuple to get all the font families...
font_tuple = tk.font.families()
# Creating a varibale to get the selected font...
font_family = tk.StringVar()
# Creating a comboBox for font...
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='readonly')
# Setting the values of font tuple to the font box,
# Means giving all the font families to the comboBox....
font_box['values'] = font_tuple
# Setting the default value...
font_box.current(font_tuple.index(application_default_font))
font_box.grid(row=0, column=0, padx=5)

# .... Font Box ENDS ....


# .... Size Box STARTS ....

# Creating a variable to get the current font size...
size_var = tk.IntVar()
# Creating a comboBox for the font size...
font_size = ttk.Combobox(tool_bar, width=14, textvariable=size_var, state="readonly")
# Setting the values in the comboBox from the tuple....
font_size["values"] = tuple(range(8,101))
# Setting the default in the comboBox....
font_size.current(application_default_font_size_index)
font_size.grid(row=0, column=1, padx=5)

# .... Size Box ENDS ....

# Bold Button
bold_icon = tk.PhotoImage(file="icons/bold.png")
bold_button = ttk.Button(tool_bar, image=bold_icon)
bold_button.grid(row=0, column=2, padx=5)

# Italic Button
italic_icon = tk.PhotoImage(file="icons/italic.png")
italic_button = ttk.Button(tool_bar, image=italic_icon)
italic_button.grid(row=0, column=3, padx=5)

# Underline Button
underline_icon = tk.PhotoImage(file="icons/underline.png")
underline_button = ttk.Button(tool_bar, image=underline_icon)
underline_button.grid(row=0, column=4, padx=5)

# Font color Button
font_color_icon = tk.PhotoImage(file="icons/font_color.png")
font_color_button = ttk.Button(tool_bar, image=font_color_icon)
font_color_button.grid(row=0, column=5, padx=5)

# align left Button
align_left_icon = tk.PhotoImage(file="icons/align_left.png")
align_left_button = ttk.Button(tool_bar, image=align_left_icon)
align_left_button.grid(row=0, column=6, padx=5)

# align center Button
align_center_icon = tk.PhotoImage(file="icons/align_center.png")
align_center_button = ttk.Button(tool_bar, image=align_center_icon)
align_center_button.grid(row=0, column=7, padx=5)

# align right Button
align_right_icon = tk.PhotoImage(file="icons/align_right.png")
align_right_button = ttk.Button(tool_bar, image=align_right_icon)
align_right_button.grid(row=0, column=8, padx=5)

#-------------------------------- End toolbar ----------------------------------


#________________________________ Text Editor Starts ___________________________

# Creating the Text editing area in the main application....
text_editor = tk.Text(main_application)
text_editor.config(wrap="word", relief=tk.FLAT)

# Creating the scroll bar in the main application for the text editor...
scroll_bar = tk.Scrollbar(main_application)
# Setting the cursor active on the text editor...
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# font family and font size functionallity....
current_font_family = application_default_font
current_font_size = application_default_font_size

# Function to change the FONT FAMILY....
def change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family, current_font_size))

# Function to change the FONT SIZE....
def change_fontsize(event=None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family, current_font_size))

font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_fontsize)

# ........ Buttons Functionality .........


# Bold Button functionality....

# Function will going to change the text in the editor to BOLD....
def change_bold():
    text_property = tk.font.Font(font=text_editor["font"])
    if text_property.actual()["weight"] == "normal":
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()["weight"] == "bold":
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))
bold_button.configure(command=change_bold)


# Italic Button Functionality......

# Function will going to change the text in the editor to italic....
def change_italic():
    text_property = tk.font.Font(font=text_editor["font"])
    if text_property.actual()["slant"] == "roman":
        text_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()["slant"] == "italic":
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))
italic_button.configure(command=change_italic)


# underline Button Functionality.....

# Function will going to underline the text in the editor....
def change_underline():
    text_property = tk.font.Font(font=text_editor["font"])
    if text_property.actual()["underline"] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()["underline"] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))
underline_button.configure(command=change_underline)


# font color Functionality.....

# Function will going to change the color of the font....
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])
font_color_button.configure(command=change_font_color)


# align Functionality....

# Left
def align_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')
align_left_button.configure(command=align_left)

# Center
def align_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')
align_center_button.configure(command=align_center)

# Right
def align_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')
align_right_button.configure(command=align_right)


text_editor.configure(font=(application_default_font, application_default_font_size))
text_editor.config(background=application_default_background_color, fg=application_default_foreground_color)
#-------------------------------- Text Editor Ends   ---------------------------


#________________________________  status bar _____________________________

status_bar = ttk.Label(main_application, text="Status Bar")
status_bar.pack(side=tk.BOTTOM)

# Variable to keep track if any changes are made to the text in document.....
text_changed = False

# This function Updates the status bar.....
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, "end-1c").replace(' ', ''))
        status_bar.config(text=f"Characters : {characters} Words : {words}")
    text_editor.edit_modified(False)
text_editor.bind("<<Modified>>", changed)


#-------------------------------- End status bar --------------------------


#________________________________ Main menu functinatily________________________

# This variable will going to have the path for the file....
url = ""


# File menu Commands


# New Functionality...
# This function empty outs the url variable and delete all the text on the editor window....
def new_file(event=None):
    global url
    url = ""
    text_editor.delete(1.0, tk.END)

file_menu.add_command(label="New", image=new_icon, compound=tk.LEFT,
                      accelerator="Ctrl+N",command=new_file)


# Open Functionality...
# This function opens up a new file....
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select File",
                                     filetypes=(("Text File", '*.txt'), ("All Files", '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))

file_menu.add_command(label="Open", image=open_icon,
                      compound=tk.LEFT, accelerator="Ctrl+O", command=open_file)


# Save Functionality....
def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                     filetypes=(("Text File", '*.txt'), ("All Files", '*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return

file_menu.add_command(label="Save", image=save_icon,
                      compound=tk.LEFT, accelerator="Ctrl+S", command=save_file)


# Save as Functionality...
def save_as(event=None):
    global url
    try:
        content = text_editor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                   filetypes=(("Text File", '*.txt'), ("All Files", '*.*')))
        url.write(content)
        url.close()
    except:
        return

file_menu.add_command(label="Save As", image=save_as_icon,
                      compound=tk.LEFT, accelerator="Ctrl+Alt+S", command=save_as)


# Exit functionality...
def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel("Warning", 'Do you want to save the file ?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                                   filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return

file_menu.add_command(label="Exit", image=exit_icon,
                      compound=tk.LEFT, accelerator="Ctrl+Q", command=exit_func)


# Edit menu Commands....

# Copy Functionality...
edit_menu.add_command(label="Copy", image=copy_icon,
                      compound=tk.LEFT, accelerator="Ctrl+C",
                      command=lambda:text_editor.event_generate("<Control c>"))


# Paste Functionality...
edit_menu.add_command(label="Paste", image=paste_icon,
                      compound=tk.LEFT, accelerator="Ctrl+V",
                      command=lambda:text_editor.event_generate("<Control v>"))


# Cut Functionality...
edit_menu.add_command(label="Cut", image=cut_icon,
                      compound=tk.LEFT, accelerator="Ctrl+X",
                      command=lambda:text_editor.event_generate("<Control x>"))


# Clear all Functionality...
edit_menu.add_command(label="Clear All", image=clear_all_icon,
                      compound=tk.LEFT, accelerator="Ctrl+Alt+X",
                      command=lambda:text_editor.delete(1.0, tk.END))


# Find Functionality...
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

    # Frame
    find_frame = ttk.LabelFrame(find_dialogue, text="Find/Replace")
    find_frame.pack(pady=20)

    # Labels
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text='Replace')

    # Entry
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    # Button
    find_button = ttk.Button(find_frame, text="Find", command=find)
    replace_button = ttk.Button(find_frame, text="Replace", command=replace)

    # Label grid
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    # Entry grid
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    # Button grid
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()


edit_menu.add_command(label="Find", image=find_icon,
                      compound=tk.LEFT, accelerator="Crtl+F", command=find_func)



# View Menu Commands (Check Buttons)...
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
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
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True

view_menu.add_checkbutton(label="Tool Bar",onvalue=True, offvalue=0,variable=show_toolbar,
                          image=tool_bar_icon, compound=tk.LEFT, command=hide_toolbar)
view_menu.add_checkbutton(label="Status Bar", onvalue=1, offvalue=False,variable=show_statusbar,
                          image=status_bar_icon, compound=tk.LEFT, command=hide_statusbar)


# For Color Theme Menu...

# Color Theme Menu Radio Button...
# Creating a loop to create the radio button of the theme.....
# This Loop will going to take in the value from the Tuple and Dictionary and then create the radio button with them...

def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_theme_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color)

count = 0

for i in color_theme_dict:
    color_theme_menu.add_radiobutton(label=i, image=color_theme_icons[count],
                                     variable=theme_choice, compound=tk.LEFT,
                                     command=change_theme)
    count += 1


#-------------------------------- End Main Menu Functinatily ------------------------


main_application.config(menu=main_menu)

### bind shortcut keys
main_application.bind("<Control-n>", new_file)
main_application.bind("<Control-o>", open_file)
main_application.bind("<Control-s>", save_file)
main_application.bind("<Control-Alt-s>", save_as)
main_application.bind("<Control-q>", exit_func)
main_application.bind("<Control-f>", find_func)

main_application.mainloop()
