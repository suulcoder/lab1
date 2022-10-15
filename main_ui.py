
import sys
import os

import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from error import *
errorslist = []

class numberLines(tk.Text):
    def __init__(self, master, text_widget, **kwargs):
        super().__init__(master, **kwargs)

        self.text_widget = text_widget
        self.text_widget.bind('<FocusIn>', self.on_key_press)

        self.insert(1.0, '1')
        self.configure(state='disabled')

    def on_key_press(self, event=None):
        final_index = str(self.text_widget.index(tk.END))
        num_of_lines = final_index.split('.')[0]
        line_numbers_string = "\n".join(str(no + 1) for no in range(int(num_of_lines)))
        width = len(str(num_of_lines))

        self.configure(state='normal', width=width+1 if int(num_of_lines) < 10 else width)
        self.delete(1.0, tk.END)
        self.insert(1.0, line_numbers_string)
        self.configure(state='disabled')



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
    os.system("bash runner.sh")
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
    l = numberLines(window, text_area_code, width=2, height=38, font=("Times New Roman", 15), foreground="gray", highlightthickness=0)
    adharbtn.grid(row=0, column=0, columnspan=10)
    runbtn.grid(row=0, column=11, columnspan=10)
    text_area_code.grid(column=0, row=1, columnspan=20, rowspan=50)
    l.grid(column=0, row=1, padx=(0, 279))
    window.mainloop()
