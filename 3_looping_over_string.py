# Example Practice:
# Ask the user for a word.
# Use a for loop to print each letter on a new line.

# Challenge:
# Count how many vowels are in the word.

word = str(input("ok: "))
the = len(word)
numbr = list(range(0,the+1))

print(word, the)

for i in numbr:
    print(word[i])
    i +=1
    if i >= len(word):
        break

nv = word.find("a") + word.find("e") + word.find("i") + word.find("o") + word.find("u") + word.find("A") + word.find("I") + word.find("E") + word.find("O") + word.find("U")

# print(f"# of vowels: {nv}")
