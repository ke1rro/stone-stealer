from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import subprocess


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def start_game():
    subprocess.run(['python', r"build\game_interface.py"],
                   bufsize=1)


window = Tk()
window.geometry("980x650")
window.title('STONE STEALER')
window.configure(bg="#FFFFFF")
window.iconbitmap('single-stone.ico')

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=650,
    width=980,
    bd=0,
    highlightthickness=0,
    relief="ridge")

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("background.png"))
image_1 = canvas.create_image(
    492.4699993133545,
    325.13999938964844,
    image=image_image_1)

image_image_2 = PhotoImage(
    file=relative_to_assets("st_near_btn.png"))
image_2 = canvas.create_image(
    418.45001220703125,
    241.3000030517578,
    image=image_image_2)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: start_game(),
    relief="flat"
)

button_1.place(
    x=375.0,
    y=266.0,
    width=250.0,
    height=60.0)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat")
button_2.place(
    x=374.6400146484375,
    y=341.0,
    width=250.0,
    height=60.0)

image_image_3 = PhotoImage(
    file=relative_to_assets("stone_stealer.png"))
image_3 = canvas.create_image(
    489.1699981689453,
    166.97999572753906,
    image=image_image_3)

image_image_4 = PhotoImage(
    file=relative_to_assets("st_right_coner.png"))
image_4 = canvas.create_image(
    748.3900146484375,
    45.029998779296875,
    image=image_image_4)

image_image_5 = PhotoImage(
    file=relative_to_assets("st_right_low_corner.png"))
image_5 = canvas.create_image(
    929.5800170898438,
    604.1900024414062,
    image=image_image_5)

image_image_6 = PhotoImage(
    file=relative_to_assets("st_left_low_corner.png"))
image_6 = canvas.create_image(
    47.193105697631836,
    608.5399780273438,
    image=image_image_6)

window.resizable(False, False)
window.mainloop()
