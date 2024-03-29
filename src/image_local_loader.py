import tkinter as tk
from PIL import Image, ImageTk

class ImageLocalLoader:
    def __init__(self, root):
        self.root = root
        self.label = tk.Canvas(root, bg="black", borderwidth=0, highlightthickness=0)
        self.label.pack(fill=tk.BOTH, expand=True)
        self.photo = None  # Store the PhotoImage object as an instance variable
        self.images = []  # Initialize the images attribute here
        

    def load_image(self, image_path):
        try:
            # Delete previous image if it exists
            # if self.photo:
            #     self.canvas.delete(self.photo)

            # self.canvas.delete("all")
            
            # self.clear_canvas()


            image = Image.open(image_path)

            print("Canvas width:", self.label.winfo_width())
            print("Canvas height:", self.label.winfo_height())

            window_width = self.root.winfo_screenwidth()
            window_height = self.root.winfo_screenheight()

            img_width, img_height = image.size
            new_height = int(window_height)
            new_width = int(img_width * (new_height / img_height))
            image = image.resize((new_width, new_height))

            x = (window_width - image.width) // 2
            y = (window_height - image.height) // 2

            # Create a new PhotoImage object
            self.photo = ImageTk.PhotoImage(image)

            # self.label.create_image(x, y, anchor=tk.NW, image=self.photo)
            self.label.config(x, y, anchor=tk.NW, image=self.photo)
            

            self.label.image = self.photo

        except Exception as e:
            # Handle exceptions
            print(f"An error occurred: {str(e)}")

    def clear_canvas(self):
            # Clear the canvas by deleting all items and removing references to the images
            for image in self.images:
                self.canvas.delete(image)
            self.images.clear()