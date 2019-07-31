import random
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--manual", "-m", help="play the monty hall problem out yourself n number of times", action="store_true")
parser.add_argument("--number", "-n", help="the number of times you play")
parser.add_argument("--goat", "-g", help="place the goat in door 1,2,3 for all n times; 0 for random")

args = parser.parse_args()

def generate_doors(args):
    doors = [False,False,False]
    if args.goat and int(args.goat) > 0:
        doors[int(args.goat) - 1] = True
    else:
        doors[0] = True
        random.shuffle(doors)
    for i in range(0,len(doors)):
        if doors[i]:
            prize = i+1
    return doors, prize

def find_goat(doors, choice):
    goats = []
    for door in range(0,len(doors)):
        if not doors[door] and door != choice:
            goats.append(door+1)
           
    goat = random.choice(goats)
    goats.remove(goat)
    if len(goats) > 0:
        return goat, goats[0]
    else:
        return goat, None

if args.manual:
    for i in range(0, int(args.number)):
        d, prize_door = generate_doors(args)
        print(d, prize_door)
        first_choice = int(input("Please select a door number: 1, 2 or 3\n"))
        print("Your first choice is door number: ", first_choice)
        goat_door, other_door = find_goat(d, first_choice)
        print("Just so you know, door number " + str(goat_door) + " contains a goat.")
        if other_door == None:
            switch = input("Would you like to switch to door number " + str(prize_door) + "? y or n\n")
        else:
            switch = input("Would you like to switch to door number " + str(other_door) + "? y or n\n")

        if switch[0] == 'y':
            second_choice = other_door
        elif switch[0] == 'n':
            second_choice = first_choice

        if d[second_choice-1]:
            print("Congratulations you've won!")
        else:
            print("I'm sorry, the prize was contained behind door number " + str(prize_door))

