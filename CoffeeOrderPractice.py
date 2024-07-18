print("Thank you for choosing Ejay's Coffee!")
size = input()  # What size coffee do you want? S, M, or L
add_syrup = input()  # Do you want coffee syrup? Y or N
extra_shot = input()  # Do you want extra shot of espresso? Y or N

# Initialize the bill
bill = 0

# Calculate the bill based on pizza size
if size == "S":
    bill = 80
elif size == "M":
    bill = 100
elif size == "L":
    bill = 115

# Add pepperoni cost
if add_syrup == "Y":
    if size == "S":
        bill += 10
    else:
        bill += 15

# Add extra cheese cost
if extra_shot == "Y":
    bill += 20

# Print the final bill
print(f"Your final bill is: ${bill}")
