from PIL import Image

def run_pillow():
    img = Image.new("RGB", (100, 100), color="blue")
    print("Створено синє зображення розміром:", img.size)