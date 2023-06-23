label splashscreen:
    if renpy.file("intro.webm"): ## You heard of renpy.file()?
        image splash intro = Movie(play="intro.webm")
    else:
        image splash intro = "placeholder.png"
    if persistent.seen_splash:
        scene black
        show text _("Dusty Records") with dissolve 
        with Pause(1.2)
        return
    scene black with Pause(1.2)
    show splash intro
    show text _("ClGames Presents") with dissolve 
    with Pause(1.2)
    show text _("Dusty Records") with dissolve 
    with Pause(3)
    $ persistent.seen_splash = True
    return