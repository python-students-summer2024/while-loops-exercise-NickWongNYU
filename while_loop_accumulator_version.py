def get_starting_number():

    Flag = True
    while Flag:
        num = input("How many bottles of beer on the wall? ")
        if not num.isdigit():
            print("Please enter a valid number.")
            Flag = True
        elif int(num) < 1:
            print("Number of bottles must be at least 1.")
            Flag = True
        else:
            Flag = False
            return int(num)
            

def sing(num):
    counter=num
    while counter > 0:
        if counter ==2:
            print(f"{counter} bottles of beer on the wall, {counter} bottles of beer.")
            print(f"Take one down, pass it around, {counter-1} bottle of beer on the wall.\n")
            counter -= 1
        elif counter==1:
            print(f"{counter} bottle of beer on the wall, {counter} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!\n")
            counter-=1
        else:
            print(f"{counter} bottles of beer on the wall, {counter} bottles of beer.")
            print(f"Take one down, pass it around, {counter-1} bottles of beer on the wall.\n")
            counter-=1
