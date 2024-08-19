def click_d4():
    result = randrange(1, 5)
    print(f"You rolled {result}")
    if result == 4:
        print("You are very lucky")
    elif result >= 2:
        print("Not bad")
    else:
        print("Bad luck")