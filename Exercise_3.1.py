#  Jeff Bohn
#  SWDV-210  Exercise 3-1
#  8/27/2024

print("\nThe Miles Per Gallon Program")

while True:
    milesDriven = float(input("\nEnter Miles Driven: \t\t"))
    gallonsUsed = float(input("Enter Gallons of Gas Used: \t"))
    gallonPrice = float(input("Enter Cost per Gallon: \t\t"))

    if milesDriven > 0 and gallonsUsed > 0 and gallonPrice > 0:
        print(f"\nMiles per Gallon: \t\t {milesDriven / gallonsUsed}")
        print(f"Total Gas Cost: \t\t${gallonPrice * gallonsUsed}")
        print(
            f"Cost per Mile: \t\t\t${round( gallonPrice / (milesDriven / gallonsUsed) , 4)}"
        )
        result = input("\nGet Entries for Another Trip (y or n)?")
        if result == "y":
            continue
        else:
            break
    else:
        print("Values must be more than ZERO, try again!")
        continue
