#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington State Ferry fare based on age and whether the person has a vehicle. Assume the following rates:
#* Adults (19-64): $10 without a vehicle, $20 with a vehicle.
#* Seniors (65+): $5 without a vehicle, $15 with a vehicle.
#* Children (0-18): Free.

age = ""
vehicle = ""
fare = ""

def ferry_fare(age, vehicle):
    if age < 18:
        return print("Free fare")
    elif 65 > age > 18 and vehicle == "Y":
        return print("Your fare is $20")
    elif 65 > age > 18 and vehicle == "N":
        return print("Your fare is $10")
    elif 65 < age and vehicle == "Y":
        return print("Your fare is $15")
    elif 65 < age and vehicle == "N":
        return print("Your fare is $5")

print(ferry_fare(int(input("What is your age? ")), input("Do you have a vehicle? Y or N: ")))
