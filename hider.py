import os

def hidercode():
    file_path = os.path.join(os.path.expanduser("~"), "Pictures", "My Wallpaper.jpg")
    if os.path.isfile(file_path):
        print("Error 1000x00019 Please enable BIOS")
        return
    else:
        print("---")

