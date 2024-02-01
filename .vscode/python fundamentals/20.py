def casrint(car):
    print(f"Your car name is {car['name']} and it's speed is {car['speed']} and milege is {car['milege']}")



cars = [
    {"name":"bmw","speed":"120km/h","milege":"10km/h"},
    {"name":"audi","speed":"150km/h","milege":"7km/h"},
    {"name":"neno","speed":"80km/h","milege":"40km/h"},
]
for i in range(len(cars)):
    casrint(cars[i])
