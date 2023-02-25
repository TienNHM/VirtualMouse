import easygui
import os
import webbrowser

from mouse import VirtualMouse

msg = "Choose function"
title="Virtual Mouse"
choices = ["Game", "Virtual Mouse", "Exit"]
game_url = "https://youth-quiz.vercel.app/game"

while True:
    reply = easygui.buttonbox(msg, title,  choices=choices)

    if reply == "Virtual Mouse":
        VirtualMouse()
    elif reply == "Game":
        webbrowser.open(game_url)
    else:
        # os._exit(0)
        break