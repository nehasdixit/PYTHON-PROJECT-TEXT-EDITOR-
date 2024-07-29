@@ -0,0 +1,4 @@
from tkinter import filedialog
def saving():
    filename = filedialog.asksaveasfilename(filetypes=(("Text files","*.txt"),("PDF files","*.pdf")))
    return filename
