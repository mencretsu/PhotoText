import pytesseract
import os

folder_path = 'YOUR PATH HERE'
found = 0
#your teseract path
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    text = pytesseract.image_to_string(file_path)
    if "'highlight'>" in text:
        os.remove(file_path)
        found += 1
        print(f"{found} Found !")
print(f"Done !\nTotal found: {found}")
