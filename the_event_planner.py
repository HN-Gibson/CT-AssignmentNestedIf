# Task 1: Code Correction 
# You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

attendees = int(input("Enter number of attendees: ")) #added int() to convert the input to a int for use in comparison statements
venue = "large hall" if attendees > 100 else "conference room"

print(venue)

# Task 2: Venue Selection
# Based on the corrected code from Task 1, further enhance your code to recommend additional things like "audio system" or "projector" based on the number of attendees.

# used shorthand if statements within a print() command to provide a quick decision on audio/visuals
print("use audio system" if attendees > 50 else "don't need audio system")
print("use projector" if attendees > 25 else "don't need projector")

# Task 3: Catering Choices
# Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".

# set vegetarian_preference = user input with yes/no question and set an output print() with shorthand if statment to determine what gets printed
vegetarian_preference = input("Do you require vegetarian food options? (yes/no): ")

print ("We recommend Veggie Delight Caterers!" if vegetarian_preference == "yes" else "We recommend Gourmet Meals Caterers!")