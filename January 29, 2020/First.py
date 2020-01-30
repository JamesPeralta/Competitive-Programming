trips = int(input())

locations = {}
for i in range(0, trips):
    num_of_locations = int(input())
    for j in range(0, num_of_locations):
        city = input()
        data = locations.get(city, 0)
        locations[city] = data + 1

    print(len(locations.keys()))
    locations = {}
