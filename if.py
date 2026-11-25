#Traffic Lights

color = input("traffic light color (red, yellow, green): ").lower()
if color == "red" or color == "r":
    print("Stop! The light is red.")
elif color == "yellow" or color == "y":
    print("Caution! The light is yellow. Prepare to stop.")
elif color == "green" or color == "g":
    print("Go! The light is green.")
else:
    print("Invalid color! Please enter red, yellow, or green.")
