places = input()

places_equals = [place for place in places.split("=") if (place.isalpha() and len(place) >= 3 and place[0].isupper()) ]
places_slashes = [place for place in places.split("/") if (place.isalpha() and len(place) >= 3 and place[0].isupper())]

valid_destinations = places_equals + places_slashes
print(f"Destinations: " + ", ".join(valid_destinations))
# calculate travel points
travel_points = 0
for destination in valid_destinations:
    travel_points += len(destination)
print(f"Travel Points: {travel_points}")
