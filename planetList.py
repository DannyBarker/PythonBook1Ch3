planet_list = ["Mercury", "Mars"]
planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Uranus", "Neptune"])
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")
planet_list.append("Pluto")
rocky_planets = planet_list[0:4]
del planet_list[8]

spacecraft = [
   ("Cassini", "Saturn"),
   ("Voyager 2", "Saturn"),
   ("Voyager 2", "Mars"),
   ("Viking", "Mars"),
   ("Opportunity", "Mars"),
]

for planet in planet_list:
    for vehicle in spacecraft:
        if planet == vehicle[1]:
            print(f'{vehicle[0]} has visited {planet}')
