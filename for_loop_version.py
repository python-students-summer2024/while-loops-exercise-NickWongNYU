
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
    for i in range (num, 0, -1):
        if i==1:
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!\n")
        elif i==2:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print("Take one down, pass it around, 1 bottle of beer on the wall.\n")

        else:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down, pass it around, {i-1} bottles of beer on the wall.\n")

       


