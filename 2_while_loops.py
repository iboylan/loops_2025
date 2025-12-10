# Given:
colors = ["red", "blue", "green", "yellow", "purple"]

# Challenge:
# Use a while loop to print each color UNTIL you find "yellow".
# Do NOT print "yellow" — stop before it.

for color in colors:
    if color == "yellow":
        break
    print(color)