import os
from PIL import Image
from tkinter import Tk, filedialog, messagebox, Button, Label, OptionMenu, StringVar, Listbox, Frame, ttk
from tkinterdnd2 import TkinterDnD, DND_FILES
import tkinter as tk

class ImageToPDFConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to PDF Converter")

        self.image_files = []
        self.output_pdf = "output.pdf"

        # Frame for drag and drop
        self.drop_frame = Frame(root, bd=2, relief="solid")
        self.drop_frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.drop_label = Label(self.drop_frame, text="Drag and Drop Images Here", font=("Arial", 14))
        self.drop_label.pack(pady=50)

        # Listbox for image preview
        self.listbox = Listbox(root, selectmode="extended")
        self.listbox.pack(pady=10, padx=10, fill="both", expand=True)

        # Button to add images
        self.add_images_button = Button(root, text="Add Images", command=self.add_images)
        self.add_images_button.pack(pady=5)

        # Button to remove selected images
        self.remove_images_button = Button(root, text="Remove Selected Images", command=self.remove_images)
        self.remove_images_button.pack(pady=5)

        # Frame for PDF settings
        self.settings_frame = Frame(root)
        self.settings_frame.pack(pady=10)

        # Orientation selection
        self.orientation_label = Label(self.settings_frame, text="Orientation:")
        self.orientation_label.grid(row=0, column=0, padx=5)
        self.orientation_var = StringVar(value="Portrait")
        self.orientation_menu = OptionMenu(self.settings_frame, self.orientation_var, "Portrait", "Landscape")
        self.orientation_menu.grid(row=0, column=1, padx=5)

        # Button to convert images to PDF
        self.convert_button = Button(root, text="Convert to PDF", command=self.convert_to_pdf)
        self.convert_button.pack(pady=20)

        # Progress bar
        self.progress = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
        self.progress.pack(pady=10)

        # Credit label
        self.credit_label = Label(root, text="Created by iseeface", font=("Arial", 10, "italic"))
        self.credit_label.pack(pady=5)

        # Initialize drag and drop
        self.drop_frame.drop_target_register(DND_FILES)
        self.drop_frame.dnd_bind('<<Drop>>', self.drop_files)

        # Adjust window size
        self.adjust_window_size()
    
    def adjust_window_size(self):
        self.root.update_idletasks()
        width = max(550, self.root.winfo_reqwidth())
        height = max(500, self.root.winfo_reqheight())
        self.root.geometry(f"{width}x{height}")

    def add_images(self):
        files = filedialog.askopenfilenames(
            title="Select Images",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
        )
        if files:
            self.image_files.extend(files)
            self.update_listbox()
            self.adjust_window_size()

    def remove_images(self):
        selected_indices = self.listbox.curselection()
        selected_files = [self.listbox.get(i) for i in selected_indices]
        
        # Remove from list
        self.image_files = [f for f in self.image_files if os.path.basename(f) not in selected_files]
        self.update_listbox()
        self.adjust_window_size()

    def drop_files(self, event):
        files = self.root.tk.splitlist(event.data)  # Fix for drag and drop issue
        self.image_files.extend(files)
        self.update_listbox()
        self.adjust_window_size()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for file in self.image_files:
            self.listbox.insert(tk.END, os.path.basename(file))

    def convert_to_pdf(self):
        if not self.image_files:
            messagebox.showwarning("No Images", "Please add images first.")
            return

        output_pdf = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
            title="Save PDF As"
        )
        if not output_pdf:
            return

        orientation = self.orientation_var.get()
        images = [Image.open(image) for image in self.image_files]
        total_images = len(images)

        self.progress["maximum"] = total_images
        self.progress["value"] = 0
        self.root.update_idletasks()

        # Rotate images if orientation is landscape
        if orientation == "Landscape":
            images = [image.rotate(90, expand=True) for image in images]

        # Save images to PDF with progress bar
        for i, img in enumerate(images):
            if i == 0:
                img.save(output_pdf, save_all=True, append_images=images[1:], resolution=100.0)
            
            self.progress["value"] = i + 1
            self.root.update_idletasks()

        messagebox.showinfo("Success", f"PDF saved as {output_pdf}")
        self.progress["value"] = 0  # Reset progress after completion

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = ImageToPDFConverter(root)
    root.mainloop()
