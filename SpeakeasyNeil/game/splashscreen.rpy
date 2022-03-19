label splashscreen:
    show screen splash
    show screen disclaim
    $ renpy.pause()
    hide screen splash
    call screen confirm(message="Have you read, and understand the disclaimer text below?\n\nThis project is a non-profit with the goal of preservation of Lovestruck©, property of Voltage Entertainment USA Inc.", yes_action=Return(), no_action=Quit(confirm=False))
    hide screen disclaim
    return

screen splash:
    frame:        
        background "splash.png"
screen disclaim:
    text "This project is a non-profit with the goal of " yalign 0.95 color("#00FF00")
    text "preservation of Lovestruck©, property of Voltage Entertainment USA Inc." size 40 yalign 1.0 color("#00FF00")