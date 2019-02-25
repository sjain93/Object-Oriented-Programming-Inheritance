class System:
    bodies = []

    def __init__(self, name):
        self.name = name

    def add(self, body_variable):
        self.body = body_variable
        #such as earth that has been initialised through Body class
        System.bodies.append(self.body)

    def total_mass(self):
        tot_mass = 0
        for body in bodies:
            tot_mass += body.mass
        return tot_mass

class Body: #not explcitly initialised

    def __init__(self, body_name, body_mass):
        self.body_name = body_name
        self.body_mass = float(body_mass)

class Planet(Body):

    def __init__(self, p_body_name, p_body_mass, day, year):
        super().__init__(p_body_name, p_body_mass)
        self.day = float(day)
        self.year = float(year)

class Star(Body):

    def __init__(self, s_body_name, s_body_mass, type):
        super().__init__(s_body_name, s_body_mass)
        self.type = str(type)

class Moon(Body):

    def __init__(self, m_body_name, m_body_mass, orbit_month, planet):
        super().__init__(m_body_name, m_body_mass)
        self.month = float(orbit_month)
        self.planet = None
        for body in System.bodies:
            if body.body_name == planet:
                self.planet = body


sol = System("sol_system")
earth = Planet("Earth", 5.972, 1, 365)
# earth = Body("Earth", 5.972)
# print(earth)
sun = Star("Sun", 100, 0)

sol.add(earth)
sol.add(sun)

moon = Moon("Moon", 2, 3, "Earth")
print(moon.planet.body_mass)
print(earth.year)
#
sol.add(moon)
print(System.bodies)
for body in System.bodies:
    print(body.body_name)
