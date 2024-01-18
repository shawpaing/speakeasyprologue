style ls_text is text:
    font "SigmarOne-Regular.ttf"

screen button_overlay():
    imagebutton:
        idle "gui/ls/menu_side.png" xpos 1538
        action Show("ls_menu")

screen ls_menu():
    frame:
        modal True
        #imagebutton idle "gui/ls/transparent.png" action Hide("ls_menu") xpos 0.0
        background "gui/ls/sidebar.png" xpos 0.78
        vbox:
            imagebutton idle "gui/ls/edit_name.png" action Hide("ls_menu"), Call("changeName") xpos 285 ypos 15
            text "[fName]" xpos 0.4 ypos 40
            text "[lName]" xpos 0.4 ypos 40
            imagebutton idle "gui/ls/menu_button.png" action ShowMenu("history"), Hide("ls_menu") xpos 0.35 ypos 80
            imagebutton idle "gui/ls/menu_button.png" action Preference("auto-forward", "toggle"), Hide("ls_menu") xpos 0.35 ypos 88
            imagebutton idle "gui/ls/menu_button.png" action Hide("ls_menu"), Skip() alternate Skip(fast=True, confirm=True) xpos 0.35 ypos 96
            imagebutton idle "gui/ls/menu_button.png" action ShowMenu("save"), Hide("ls_menu") xpos 0.35 ypos 104
            imagebutton idle "gui/ls/menu_button.png" action ShowMenu('preferences'), Hide("ls_menu") xpos 0.35 ypos 112
            imagebutton idle "gui/ls/menu_button.png" action MainMenu() xpos 0.35 ypos 120
            text "Log" style "ls_text" xpos 0.75 ypos -520
            text "Autoplay" style "ls_text" xpos 0.55 ypos -453
            text "FFW" style "ls_text" xpos 0.75 ypos -388
            text "Save" style "ls_text" xpos 0.7 ypos -320
            text "Settings" style "ls_text" xpos 0.6 ypos -255
            text "Home" style "ls_text" xpos 0.65 ypos -190

label changeName:
    python:
        fName = renpy.input("What is your first name?")
        lName = renpy.input("What is your last name?")
    return

define dress = ""
screen ls_cards():
    modal True
    hbox:
        imagebutton:
            idle "images/card_free.webp" xpos 0.6 ypos 0.3
            action SetVariable("dress", "normal"), Jump("dress_choice")
        imagebutton:
            idle "images/card_heart.webp" xpos 0.9 ypos 0.3
            action SetVariable("dress", "heart"), Jump("dress_choice")
    hbox:
        add "images/characters/me/me prolp.webp" xpos 0.6 ypos 0.222 zoom 0.7
        add "images/characters/me/me prolf.webp" xpos 0.7 ypos 0.222 zoom 0.7

label next_chapter_menu:
    menu next_ask:
        "Would you like to continue to the next chapter?"
        "Yes":
            if next_chapter == 1:
                jump s1e1
            elif next_chapter == 2:
                jump s1e2
            elif next_chapter == 3:
                jump s1e3
            elif next_chapter == 4:
                jump s1e4
            elif next_chapter == 5:
                jump s1e5
            elif next_chapter == 6:
                jump s1e6
            elif next_chapter == 7:
                jump s1e7
            elif next_chapter == 8:
                jump s1e8
            elif next_chapter == 9:
                jump s1e9
            elif next_chapter == 10:
                jump s1e10
            elif next_chapter == 11:
                jump s1e11
            elif next_chapter == 12:
                jump s1e12
            elif next_chapter == 13:
                jump s1e13
            elif next_chapter == 14:
                jump s1e14
            elif next_chapter == 15:
                jump s1e15
            elif next_chapter == 16:
                jump s1e16