from tweak_af import tv

while True:
    value = tv(42)

    if value == 0:
        print("Nobody touched my tralala!")
    elif value == 42:
        print("Someone touched my tralala and hit the spot!")
        exit(0)
    else:
        print("Someone touched my tralala!")
