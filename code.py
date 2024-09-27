import tkinter as tk
from tkinter import filedialog, scrolledtext
import PyPDF2
from tkinter import font

def open_file():
    filename = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if filename:
        filename_label.configure(text=filename)
        outputfile_text.config(state=tk.NORMAL)  # Cho phép chỉnh sửa tạm thời
        outputfile_text.delete("1.0", tk.END)
        reader = PyPDF2.PdfReader(filename)
        for page in reader.pages:
            current_text = page.extract_text()
            outputfile_text.insert(tk.END, current_text)
        outputfile_text.config(state=tk.DISABLED)  # Vô hiệu hóa chỉnh sửa

root = tk.Tk()
root.title("Trình scan PDF")

# Set the window to full screen
root.state('zoomed')

# Set the window icon
icon = tk.PhotoImage(file=r'C:\Users\Admin\Desktop\python\PDF extractor\Icon\icon.png')  
root.iconphoto(False, icon)

# Create a frame for better layout management
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

# Define a custom font
custom_font = font.Font(family="arial", size=12)

# Create and style the filename label
filename_label = tk.Label(frame, text="Chưa có file nào được mở", anchor="center", bg="#f0f0f0", font=("arial", 14), justify="center")
filename_label.pack(fill=tk.X, pady=10)

# Create and style the scrolled text widget
outputfile_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD, font=custom_font, bg="#ffffff", relief=tk.FLAT, state=tk.DISABLED)
outputfile_text.pack(pady=10, fill=tk.BOTH, expand=True)

# Create and style the open file button
openfile_button = tk.Button(frame, text="Mở file PDF", command=open_file, bg="#4CAF50", fg="white", font=("Helvetica", 12), relief=tk.FLAT)
openfile_button.pack(pady=10)

root.mainloop()