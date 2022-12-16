#----------------------------Write a Python program that accepts a word from the user and reverse it.---------------------

input_word = input("Enter your word:-")
reverse= ""
for i in input_word:
    reverse=i+reverse
print("Your reversed word is:-",reverse)
