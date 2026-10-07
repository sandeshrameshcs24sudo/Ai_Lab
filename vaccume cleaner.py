# Vacuum Cleaner Agent

room_A = "DIRTY"
room_B = "DIRTY"

current_position = "A"

while room_A == "DIRTY" or room_B == "DIRTY":

    # If current room is dirty, clean it
    if current_position == "A" and room_A == "DIRTY":
        print("Room A is dirty")
        print("Sucking dirt from Room A")
        room_A = "CLEAN"

    elif current_position == "B" and room_B == "DIRTY":
        print("Room B is dirty")
        print("Sucking dirt from Room B")
        room_B = "CLEAN"

    # If current room is clean, move to the other room
    elif current_position == "A":
        if room_B == "DIRTY":
            print("Room A is clean")
            print("Moving to Room B")
            current_position = "B"

    elif current_position == "B":
        if room_A == "DIRTY":
            print("Room B is clean")
            print("Moving to Room A")
            current_position = "A"

    print("Room A:", room_A)
    print("Room B:", room_B)
    print()

print("Both rooms are clean")
print("Goal Achieved!")
