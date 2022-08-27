import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from main_ui import errorslist

# errorslist = []
def printError(error, line=None, start_index=None):
    # window = tk.Tk()
    # window.title('Errores')
    # window.geometry('50x50')
    # text_area_error = tk.Text(window, width=40, height=30, font=("Times New Roman", 15), foreground="black")
    # text_area_error.grid(column=0, row=1, columnspan=10, rowspan=50, padx=(35, 0))
    
    if(line!=None and start_index!=None):
        
        print('\nSemantic Error: ' + error + ' (at line ' + str(line) + ':' + str(start_index) + ')\n')
        errorslist.append('\nSemantic Error: ' + error + ' (at line ' + str(line) + ':' + str(start_index) + ')\n')
        # text_area_error.insert(tk.INSERT, '\nSemantic Error: ' + error + ' (at line ' + str(line) + ':' + str(start_index) + ')\n')
    elif(line!=None):
        print('\nSemantic Error: ' + error + ' (at line ' + str(line) + ')\n')
        errorslist.append('\nSemantic Error: ' + error + ' (at line ' + str(line) + ')\n')
        # text_area_error.insert(tk.INSERT, '\nSemantic Error: ' + error + ' (at line ' + str(line) + ')\n')
    else:
        print('\nSemantic Error: ' + error + '\n')
        errorslist.append('\nSemantic Error: ' + error + '\n')
        # text_area_error.insert(tk.INSERT,'\nSemantic Error: ' + error + '\n')
    print('Hlolaaaaaa-',len(errorslist))
    # window.mainloop()
    