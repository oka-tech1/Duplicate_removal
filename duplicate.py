'''tkinter app to remove duplicate strings from a file and appending it to another file'''
import os
import tkinter as tk
from tkinter import messagebox

def remov_dup():
    count = 0
    files = []
    dup= str(entry1.get())
    fname = str(entry2.get())
    #label.configure(text="Filtered Successful")
    path = os.listdir(dup)
    for x in path:
        if fname in x:
            with open(fname, "r") as f:
                for i in f:
                    if i not in files:
                        files.append(i)
    result = (files)                    
    with open("mynew_file", "a") as st:
        for v in result:
            st.write(v)                    
    if fname in x:
        messagebox.showinfo(title="success", message="Filtered Successful")
    
            
root = tk.Tk()
root.geometry("450x250")
root.title("Duplicate Removal App")
root.configure(bg="green")
#################################
label = tk.Label(root, text="Enter the directory path to the file", bg="green", fg="black", font=("arial", 20))
label.pack(pady=10)
entry1 = tk.Entry(root, width=40, font=("arial", 12))
entry1.pack(pady=0)
label2 = tk.Label(root, text="Enter the file name in the directory", bg="green", fg="black", font=("arial", 15))
label2.pack(pady=5)
entry2 = tk.Entry(root, font=("arial", 12))
entry2.pack()
############
btn = tk.Button(root, bg="black", fg="white", text="Remove Duplicates", command=remov_dup, font=("arial", 20))
btn.pack(pady=20)

root.mainloop()



        
