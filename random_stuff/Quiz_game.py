print("Welcome to my computer quiz! ")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

score = 0 
print("Okay! let's play :)")

answer = input("Who is cason's boyfriend? ")

if answer.lower() == "athul":
    print("You're right!!")
    score += 1
else:
    print("W R O N G! DUMB FK!!!")

answer = input("What does GPU stand for? ")

if answer == "graphics processing unit":
    print("You're right!!")
    score += 1
else:
    print("W R O N G! DUMB FK!!!")

answer = input("What does Athul like? ")

if answer == "Big black cock":
    print("You're right!!")
    score += 1
else:
    print("How did you get this wrong???????")


print("You got " + str(score) + " question right!")
print("You got " + str((score / 4) * 100) + "%.")

print(f'You got {score} question right!')