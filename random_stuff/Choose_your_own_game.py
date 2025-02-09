name = input("Type your name: ")
print("Welcome", name, "to this apocalyse world")

answer = input("You are on a broken concrete street and you come to a crossroad. Where would you go? Right or left? ").lower()

if answer == "left":
    answer = input("You come to a broken store. Do you want to scavenge for food or go home? ").lower()
    if answer == "scavenge":
        print("You walked into the store to scavenge and got ambushed by raiders and died.")
    elif answer == "home":
        print("You walked home and saw a car in front of your house.")
    else:
        print('Not a valid option. You lose.')
        
elif answer == "right":
    print("You walked down the right path and found an abandoned car with supplies. Do you loot the car or leave it alone?")
    if answer == "loot":
        print("You decided to loot and car is rigged with bomb and you died.")

    elif answer == "leave":
        print("You find a child standing beside the car.")
        

    else:
        print("Not a valid option. You lose")

print("thank you for playing")