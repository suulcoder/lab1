
import sys
import os

import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from error import *
errorslist = []

def open_file():
    file_path = askopenfile(initialdir = "./input", mode='r', filetypes=[('COOL Files', '*cl'), ("all files", "*.*")])
    if file_path is not None:
        content = file_path.read()
        text_area_code.insert(tk.INSERT, content, "\n")
        runbtn.config(state="normal")

def run():
    with open('./executable.cl', 'w') as f:
        fetched_content = text_area_code.get('1.0', 'end-1c')
        f.write(fetched_content)
    run_main.set(True)
    os.system("make all")
    runbtn.wait_variable(run_main)

    

if __name__ == '__main__':
    window = tk.Tk()
    window.title('Analizador Semántico')
    window.state('zoomed')


    run_main = BooleanVar()

    # Definition of UI elements
    adharbtn = Button(
        window,
        text ='Choose File',
        command = lambda:open_file()
    )
    runbtn = Button(
        window,
        text ='Run',
        state="disabled",
        command = run
    )
    
    text_area_code = tk.Text(window, width=80, height=30, font=("Calibri", 14), foreground="purple")
    adharbtn.grid(row=0, column=0, columnspan=10)
    runbtn.grid(row=0, column=11, columnspan=10)
    text_area_code.grid(column=0, row=1, columnspan=20, rowspan=50)
    window.mainloop()
