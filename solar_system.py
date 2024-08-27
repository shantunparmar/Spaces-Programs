import random

class Planet:
    def __init__(self, name, moons=0):
        self.name = name
        self.moons = moons

class StarSystem:
    def __init__(self, name):
        self.name = name
        self.planets = []

    def add_planet(self, planet):
        self.planets.append(planet)

    def generate_system(self, num_planets):
        for i in range(num_planets):
            num_moons = random.randint(0, 5)
            planet_name = f"Planet {i+1}"
            self.add_planet(Planet(planet_name, num_moons))

    def print_system(self):
        print(f"Star System: {self.name}")
        for i, planet in enumerate(self.planets, 1):
            print(f"  Planet {i}: {planet.name} with {planet.moons} moons")

# Create a star system
system = StarSystem("Andromeda")

# Generate a random star system with 5 planets
system.generate_system(5)

# Print the star system
system.print_system()
