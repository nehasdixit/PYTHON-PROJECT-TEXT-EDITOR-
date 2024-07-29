@@ -0,0 +1,9 @@
from tkinter import filedialog
def opening():
        global opened
        global textpath
        filename=filedialog.askopenfilename(filetypes=(("Text files","*.txt"),("PDF files","*.pdf")))
        opened=True
        textpath=filename
        testpath1='C:\\nehan\OneDrive\Desktop'
        return filename
