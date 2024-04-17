from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")
_USER_NUMBER = 1


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title('STONE STEALER')
window.iconbitmap('single-stone.ico')
window.geometry("980x650")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=650,
    width=980,
    bd=0,
    highlightthickness=0,
    relief="ridge")

canvas.place(x=0, y=0)
background_image = PhotoImage(
    file=relative_to_assets("background.png"))
image_1 = canvas.create_image(
    490.0,
    327.760009765625,
    image=background_image)

Stone1 = PhotoImage(file=relative_to_assets("Stone1.png"))
Stone2 = PhotoImage(file=relative_to_assets("Stone1.png"))
Stone3 = PhotoImage(file=relative_to_assets("Stone1.png"))
Stone4 = PhotoImage(file=relative_to_assets("Stone1.png"))
Stone5 = PhotoImage(file=relative_to_assets("Stone1.png"))
Stone6 = PhotoImage(file=relative_to_assets("Stone1.png"))
Stone7 = PhotoImage(file=relative_to_assets("Stone1.png"))
Stone8 = PhotoImage(file=relative_to_assets("Stone1.png"))

_HOLDER = [Stone1, Stone2, Stone3, Stone4, Stone5, Stone6, Stone7, Stone8]

image_2 = None
image_3 = None
image_4 = None
image_5 = None
image_6 = None
image_7 = None
image_8 = None
image_9 = None
image_13 = None


def put_stones():
    global image_10, image_11, image_12, _HOLDER, image_2, image_3, image_4
    global image_5, image_6, image_7, image_8, image_9
    global Stone1, Stone2, Stone3, Stone4, Stone5, Stone6, Stone7, Stone8
    canvas.update()
    canvas.update_idletasks()
    image_2 = canvas.create_image(201.48297119140625, 239.19998168945312,
                                  image=_HOLDER[0])
    image_3 = canvas.create_image(401.4830322265625, 239.19998168945312,
                                  image=_HOLDER[1])
    image_4 = canvas.create_image(602.4829711914062, 239.19998168945312,
                                  image=_HOLDER[2])
    image_5 = canvas.create_image(801.4829711914062, 239.19998168945312,
                                  image=_HOLDER[3])
    image_6 = canvas.create_image(200.072998046875, 357.6700134277344,
                                  image=_HOLDER[4])
    image_7 = canvas.create_image(400.072998046875, 357.6700134277344,
                                  image=_HOLDER[5])
    image_8 = canvas.create_image(600.072998046875, 357.6700134277344,
                                  image=_HOLDER[6])
    image_9 = canvas.create_image(800.072998046875, 357.6700134277344,
                                  image=_HOLDER[7])
    canvas.update_idletasks()


def restart_stones():
    global _USER_NUMBER
    _USER_NUMBER = 1
    global image_13, image_11, image_12, image_10
    canvas.itemconfig(image_10, state='normal')
    canvas.itemconfig(image_11, state='normal')
    canvas.itemconfig(image_12, state='hidden')
    canvas.itemconfig(image_13, state='hidden')
    global _HOLDER
    global Stone1, Stone2, Stone3, Stone4, Stone5, Stone6, Stone7, Stone8
    global image_2, image_3, image_4, image_5, image_6, image_7, image_8
    global image_9
    _HOLDER.clear()
    _HOLDER = [Stone1, Stone2, Stone3, Stone4, Stone5, Stone6, Stone7, Stone8]
    image_2 = canvas.create_image(201.48297119140625, 239.19998168945312,
                                  image=_HOLDER[0])
    image_3 = canvas.create_image(401.4830322265625, 239.19998168945312,
                                  image=_HOLDER[1])
    image_4 = canvas.create_image(602.4829711914062, 239.19998168945312,
                                  image=_HOLDER[2])
    image_5 = canvas.create_image(801.4829711914062, 239.19998168945312,
                                  image=_HOLDER[3])
    image_6 = canvas.create_image(200.072998046875, 357.6700134277344,
                                  image=_HOLDER[4])
    image_7 = canvas.create_image(400.072998046875, 357.6700134277344,
                                  image=_HOLDER[5])
    image_8 = canvas.create_image(600.072998046875, 357.6700134277344,
                                  image=_HOLDER[6])
    image_9 = canvas.create_image(800.072998046875, 357.6700134277344,
                                  image=_HOLDER[7])


def take_stone_btn(quantity):
    global _HOLDER
    global _USER_NUMBER
    _USER_NUMBER = 2 if _USER_NUMBER == 1 else 1
    quantity = int(quantity)
    available_stones = sum(1 for img in _HOLDER if img is not None)
    if 1 <= quantity <= 2 and quantity <= available_stones:
        for i in range(quantity):
            for j in range(len(_HOLDER)):
                if _HOLDER[j] is not None:
                    _HOLDER[j] = None
                    print(_HOLDER)
                    canvas.itemconfig([image_2, image_3, image_4, image_5,
                                       image_6, image_7, image_8, image_9][j],
                                      image="")
                    end_game()
                    break
        canvas.update_idletasks()
        return True
    return False


def end_game():
    global _USER_NUMBER
    global image_11, global_12, image_13
    if _USER_NUMBER == 1:
        canvas.update()
        canvas.itemconfig(image_12, state='hidden')
        canvas.itemconfig(image_10, state='normal')
        canvas.itemconfig(image_11, state='normal')
    else:
        canvas.update()
        canvas.itemconfig(image_11, state='hidden')
        canvas.itemconfig(image_10, state='normal')
        canvas.itemconfig(image_12, state='normal')
    if _HOLDER[7] is None:
        canvas.update()
        canvas.itemconfig(image_11, state='hidden')
        canvas.itemconfig(image_12, state='hidden')
        canvas.itemconfig(image_10, state='hidden')
        if _USER_NUMBER == 1:
            canvas.update()
            canvas.itemconfig(image_12, state="normal")
        elif _USER_NUMBER == 2:
            canvas.update()
            canvas.itemconfig(image_11, state="normal")
        print("All items are None")
        canvas.itemconfig(image_13, state="normal")


put_stones()


take_1_btn = PhotoImage(
    file=relative_to_assets("take_1_btn.png"))
button_1 = Button(
    image=take_1_btn,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: take_stone_btn(quantity=1),
    relief="flat")

button_1.place(
    x=120.0,
    y=456.8900146484375,
    width=275.9200134277344,
    height=66.219970703125)

take_2_btn = PhotoImage(
    file=relative_to_assets("take_2_btn.png"))
button_2 = Button(
    image=take_2_btn,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: take_stone_btn(quantity=2),
    relief="flat")

button_2.place(
    x=610.0,
    y=458.0,
    width=275.9200439453125,
    height=66.219970703125)

return_btn = PhotoImage(
    file=relative_to_assets("return_btn.png"))
button_3 = Button(
    image=return_btn,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: window.quit(),
    relief="flat")

button_3.place(
    x=13.6199951171875,
    y=6.1199951171875,
    width=68.66999816894531,
    height=64.83999633789062)

restart_btn = PhotoImage(
    file=relative_to_assets("restart_btn.png"))
button_4 = Button(
    image=restart_btn,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: restart_stones(),
    relief="flat")

button_4.place(
    x=463.1500244140625,
    y=456.8900146484375,
    width=68.67001342773438,
    height=64.8399658203125)

p_turn = PhotoImage(
    file=relative_to_assets("p_turn.png"))
image_10 = canvas.create_image(
    506.20001220703125,
    141.11968994140625,
    image=p_turn,
    state="normal")

num_1 = PhotoImage(
    file=relative_to_assets("num_1.png"))
image_11 = canvas.create_image(
    522.0,
    140.0,
    image=num_1,
    state="normal")

num_2 = PhotoImage(
    file=relative_to_assets("num_2.png"))
image_12 = canvas.create_image(
    522.0,
    141.0,
    image=num_2,
    state="hidden")

p_won = PhotoImage(
  file=relative_to_assets("p_won.png"))
image_13 = canvas.create_image(
  506.0,
  140.0,
  image=p_won,
  state="hidden")

window.resizable(False, False)
window.mainloop()
