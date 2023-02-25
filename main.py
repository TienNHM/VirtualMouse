import easygui
import os
import webbrowser

from mouse import VirtualMouse
from mouse_v2 import VirtualMouseV2

msg = "Choose function"
title="Virtual Mouse"
choices = ["Web info", "Game", "Virtual Mouse", "Exit"]
webinfo_url = "https://digital-tranformation.vercel.app"
game_url = "https://youth-quiz.vercel.app/game"

while True:
    reply = easygui.buttonbox(msg, title,  choices=choices)

    if reply == "Virtual Mouse":
        VirtualMouseV2()
    elif reply == "Web info":
        webbrowser.open(webinfo_url)
    elif reply == "Game":
        webbrowser.open(game_url)
    else:
        # os._exit(0)
        break