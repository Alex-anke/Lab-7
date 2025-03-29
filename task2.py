import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

def get_nasa_apod(api_key):
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("url"), data.get("title")
    return None, None

def update_image():
    img_url, title = get_nasa_apod(API_KEY)
    if img_url and img_url.endswith(('.jpg', '.png', '.jpeg')):
        response = requests.get(img_url)
        img_data = Image.open(BytesIO(response.content))
        img_data = img_data.resize((600, 400))
        img = ImageTk.PhotoImage(img_data)
        label.config(image=img)
        label.image = img
        title_label.config(text=title)

if __name__ == "__main__":
    API_KEY = "acIAxXCXJlslXMebqc0SVtbfGZEZYMYSUclezta9"
    root = tk.Tk()
    root.title("NASA Фото дня")
    root.geometry("800x600")
    title_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
    title_label.pack(pady=10)
    label = tk.Label(root)
    label.pack(pady=10)
    btn = tk.Button(root, text="Обновить фото", command=update_image)
    btn.pack(pady=10)
    update_image()
    root.mainloop()