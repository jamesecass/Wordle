import os
import tkextrafont
def font():
    font_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "RobotoMono-VariableFont_wght.ttf") # Font (RobotoMono - Bold)
    tkextrafont.Font(file=font_path)