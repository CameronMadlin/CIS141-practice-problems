#5. Write a function called level_up(experience) that takes a player's experience points and returns their new level based on these rules:
#* 0-99 XP → Level 1
#* 100-199 XP → Level 2
#* 200+ XP → Level 3

experiance = 0

def level_up(experiance):
    if experiance < 100:
        print("You are level 1")
    elif 200 > experiance >= 100:
        print("You are level 2")
    elif experiance >= 200:
        print("You are level 3")

level_up(int(input("How much experiance do you have? ")))
