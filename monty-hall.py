import random
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--manual", "-m", help="play the monty hall problem out yourself n number of times", action="store_true")
parser.add_argument("--number", "-n", help="the number of times you play")
parser.add_argument("--goat", "-g", help="place the goat in door 1,2,3 for all n times; 0 for random")
parser.add_argument("--switch", "-s", help="do you automatically switch y or n; only does something for non-manual mode", action="store_true")

args = parser.parse_args()

def generate_doors(args):
    doors = {1:False,2:False,3:False}
    if args.goat and int(args.goat) > 0:
        doors[int(args.goat)] = True
    else:
        t = random.randint(1,3)
        doors[t] = True

    for i in range(1,len(doors)+1):
        if doors[i]:
            prize = i
    return doors, prize

def find_goat(doors, choice):
    d = doors.copy()
    d.pop(choice)
    dl = list(d.keys())

    #randomly decides which door to reveal, unless the randomly chosen door is the prize then reveal the other door
    r = bool(random.getrandbits(1))
    if r:
        if d[dl[0]]:
            return dl[1], dl[0]
        else:
            return dl[0], dl[1]
    else:
        if d[dl[1]]:
            return dl[0], dl[1]
        else:
            return dl[1], dl[0]

wins = 0
losses = 0
if args.manual:
    for i in range(0, int(args.number)):
        print("game number " + str(i+1))
        d, prize_door = generate_doors(args)
        print(d, prize_door)
        first_choice = int(input("Please select a door number: 1, 2 or 3\n"))

        goat_door, other_door = find_goat(d, first_choice)
        print("Just so you know, door number " + str(goat_door) + " contains a goat.")

        switch = input("Would you like to switch to door number " + str(other_door) + "? y or n\n")

        if switch[0] == 'y':
            second_choice = other_door
        elif switch[0] == 'n':
            second_choice = first_choice

        print(d)
        if d[second_choice]:
            print("Congratulations you've won the prize!")
            wins += 1
        else:
            print("I'm sorry, the prize was contained behind door number " + str(prize_door))
            losses += 1
else:
    yn = ['y','n']
    for i in range(0, int(args.number)):
        print("game number " + str(i+1))
        d, prize_door = generate_doors(args)
#        print(d, prize_door)
        first_choice = random.randint(1,3)

        goat_door, other_door = find_goat(d, first_choice)
#        print("Just so you know, door number " + str(goat_door) + " contains a goat.")

        if args.switch:
            switch = 'y'
        else:
            switch = random.choice(yn)

        if switch[0] == 'y':
            second_choice = other_door
        elif switch[0] == 'n':
            second_choice = first_choice

        if d[second_choice]:
            print("Congratulations you've won the prize!")
            wins += 1
        else:
            print("I'm sorry, the prize was contained behind door number " + str(prize_door))
            losses += 1

print("Your win/loss ratio is " + str(wins) + '/' + str(losses))
print("Your percentage of wins is " + str((wins/int(args.number))*100))
