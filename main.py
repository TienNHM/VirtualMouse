import easygui
import webbrowser

# from mouse import VirtualMouse
from mouse_v2 import VirtualMouseV2

msg = "Choose function"
title="Virtual Mouse"
choices = ["Web info", "Game", "Virtual Mouse - Cam 0", "Virtual Mouse - Cam 1", "Exit"]
webinfo_url = "https://digital-tranformation.vercel.app"
game_url = "https://youth-quiz.vercel.app/game"

while True:
    reply = easygui.buttonbox(msg, title,  choices=choices)

    if reply == "Virtual Mouse - Cam 0":
        VirtualMouseV2(camNum=0)
    elif reply == "Virtual Mouse - Cam 1":
        VirtualMouseV2(camNum=1)
    elif reply == "Web info":
        webbrowser.open(webinfo_url)
    elif reply == "Game":
        webbrowser.open(game_url)
    else:
        break