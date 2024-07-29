@@ -0,0 +1,5 @@
import tkinter as tk
def file_inp(file,text):
        workfile=open(file)
        data=workfile.read()
        text.insert(tk.END,data)
