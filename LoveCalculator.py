print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

name11 = name1.lower
name22 = name2.lower


# Initialize love score
LoveScore = 0

# Define the words to search for
word_true = "true"
word_love = "love"

# Function to count occurrences of characters in a string
def count_occurrences(word, name):
    count = 0
    for char in word:
        count += name.count(char)
    return count

# Count occurrences for name1
count_true = count_occurrences(word_true, name1)
count_love = count_occurrences(word_love, name1)

# Count occurrences for name2
count_true += count_occurrences(word_true, name2)
count_love += count_occurrences(word_love, name2)

# Calculate love score
LoveScore = int(f"{count_true}{count_love}")

# Determine message based on love score
if LoveScore < 10 or LoveScore > 90:
    print(f"Your score is {LoveScore}, you go together like coke and mentos.")
elif 40 <= LoveScore <= 50:
    print(f"Your score is {LoveScore}, you are alright together.")
else:
    print(f"Your score is {LoveScore}.")
