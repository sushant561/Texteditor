import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('Text Editor')

# ----------------------- Main Menu -----------------------
main_menu = tk.Menu(main_application)

# File menu
new_icon = tk.PhotoImage(file = "icons2/new.png")
open_icon = tk.PhotoImage(file = "icons2/open.png")
save_icon = tk.PhotoImage(file = "icons2/save.png")
save_as_icon = tk.PhotoImage(file = "icons2/save_as.png")
exit_icon = tk.PhotoImage(file = "icons2/exit.png")

file = tk.Menu(main_menu, tearoff = 0)
file.add_command(label = "New", image = new_icon, compound = tk.LEFT, accelerator = "Ctrl+N")
file.add_command(label = "Open", image = open_icon, compound = tk.LEFT, accelerator = "Ctrl+O")
file.add_command(label = "Save", image = save_icon, compound = tk.LEFT, accelerator = "Ctrl+S")
file.add_command(label = "Save As", image = save_as_icon, compound = tk.LEFT, accelerator = 'Ctrl+Alt+S')
file.add_command(label = "Exit", image = exit_icon, compound = tk.LEFT, accelerator = "Ctrl+Q")

#Edit menu
copy_icon = tk.PhotoImage(file = "icons2/copy.png")
paste_icon = tk.PhotoImage(file = "icons2/paste.png")
cut_icon = tk.PhotoImage(file = "icons2/cut.png")
clear_all_icon = tk.PhotoImage(file = 'icons2/clear_all.png')
find_icon = tk.PhotoImage(file = 'icons2/find.png')

edit = tk.Menu(main_menu, tearoff = 0)
edit.add_command(label = "Copy", image = copy_icon, compound = tk.LEFT, accelerator = "Ctrl+C")
edit.add_command(label = "Paste", image = paste_icon, compound = tk.LEFT, accelerator = "Ctrl+Y")
edit.add_command(label = "Cut", image = cut_icon, compound = tk.LEFT, accelerator = 'Ctrl+X')
edit.add_command(label = "Clear All", image = clear_all_icon, compound = tk.LEFT, accelerator = "Ctrl+Alt+X")
edit.add_command(label = "Find", image = find_icon, compound = tk.LEFT, accelerator = "Ctrl+F")

#view menu
tool_bar_icon = tk.PhotoImage(file = "icons2/tool_bar.png")
status_bar_icon = tk.PhotoImage(file = "icons2/status_bar.png")

view = tk.Menu(main_menu, tearoff = 0)
view.add_checkbutton(label = "Tool Bar", image = tool_bar_icon, compound = tk.LEFT)
view.add_checkbutton(label = "Status Bar", image = status_bar_icon, compound = tk.LEFT)

#color menu
light_default_icon = tk.PhotoImage(file = "icons2/light_default.png")
light_plus_icon = tk.PhotoImage(file = "icons2/light_plus.png")
dark_icon = tk.PhotoImage(file = "icons2/dark.png")
red_icon = tk.PhotoImage(file = "icons2/red.png")
monokai_icon = tk.PhotoImage(file = "icons2/monokai.png")
night_blue_icon = tk.PhotoImage(file = "icons2/night_blue.png")

color_theme = tk.Menu(main_menu, tearoff = 0)
color_theme.add_checkbutton(label = "Light Default", image = light_default_icon, compound = tk.LEFT)
color_theme.add_checkbutton(label = "Light Plus", image = light_plus_icon, compound = tk.LEFT)
color_theme.add_checkbutton(label = "Dark", image = dark_icon, compound = tk.LEFT)
color_theme.add_checkbutton(label = "Red", image = red_icon, compound = tk.LEFT)
color_theme.add_checkbutton(label = "Monokai", image = monokai_icon, compound = tk.LEFT)
color_theme.add_checkbutton(label = "Night Blue", image = night_blue_icon, compound = tk.LEFT)

#cascade
main_menu.add_cascade(label = "File", menu = file)
main_menu.add_cascade(label = "Edit", menu = edit)
main_menu.add_cascade(label = "View", menu = view)
main_menu.add_cascade(label = "Color", menu = color_theme)

# ----------------------- Main Menu End -----------------------

# ----------------------- Toolbar -----------------------
# ----------------------- Toolbar End -----------------------

# ----------------------- text editor coding -----------------------
# ----------------------- text editor coding End -----------------------

# ----------------------- main statusbar coding -----------------------
# ----------------------- main statusbar conding End -----------------------

# ----------------------- Main Menu function -----------------------
# ----------------------- Main Menu function End -----------------------



main_application.config(menu = main_menu)
main_application.mainloop()