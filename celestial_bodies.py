import math
import constants

# define sun and planets
class celestial_body:
    def __init__(self, mass, radius, initial_position, initial_speed):
        self.mass = mass
        self.position = initial_position
        self.speed = initial_speed
        self.trail = []
        self.color = (255, 255, 255)
        self.radius = radius
        self.isSun = False
        self.trail_limit_reached = False

    def __get_angle(self):
        (x,y) = self.position
        r = math.sqrt(x**2+y**2)
        if x < 0 and y > 0:
            return math.asin( abs(x/r) )
        elif x < 0 and y < 0:
            return math.pi/2 + math.asin( abs(x/r) )
        elif x > 0 and y < 0:
            return math.pi + math.asin( abs(x/r) )
        elif x > 0 and y > 0:
            return 3*math.pi/2 + math.asin( abs(x/r) )
        else:
            return 0

    def move(self, time):
        self.trail.append(self.position)
        if self.trail_limit_reached:
            self.trail.pop(0)
        self.position = (self.position[0]+time*self.speed[0], self.position[1]+time*self.speed[1])
        # check if we want to store more points for the trail
        if not self.trail_limit_reached:
            self.arc = self.__get_angle()
            if self.arc > 1.5*math.pi:
                self.trail_limit_reached = True

    def accelerate(self, time, accelaration):
        self.speed = (self.speed[0]+time*accelaration[0], self.speed[1]+time*accelaration[1])

class sun(celestial_body):
    def __init__(self):
        super().__init__(mass=constants.mass_sun, radius=constants.radius_sun, initial_position=(0,0), initial_speed=(0,0) )
        self.color = (255, 204, 0)
        self.isSun = True

class mercury(celestial_body):
    def __init__(self):
        super().__init__(mass=constants.mass_mercury, radius=constants.radius_mercury, initial_position=(0, constants.dist_sun_mercury), initial_speed=(-constants.speed_mercury, 0) )
        self.color = (169, 169, 169)

class venus(celestial_body):
    def __init__(self):
        super().__init__(mass=constants.mass_venus, radius=constants.radius_venus, initial_position=(0, constants.dist_sun_venus), initial_speed=(-constants.speed_venus, 0) )
        self.color = (218, 165, 32)

class earth(celestial_body):
    def __init__(self):
        super().__init__(mass=constants.mass_earth, radius=constants.radius_earth, initial_position=(0, constants.dist_sun_earth), initial_speed=(-constants.speed_earth, 0) )
        self.color = (80, 120, 255)

class mars(celestial_body):
    def __init__(self):
        super().__init__(mass=constants.mass_mars, radius=constants.radius_mars, initial_position=(0, constants.dist_sun_mars), initial_speed=(-constants.speed_mars, 0) )
        self.color = (178, 34, 34)

class jupiter(celestial_body):
    def __init__(self):
        super().__init__(mass=constants.mass_jupiter, radius=constants.radius_jupiter, initial_position=(0, constants.dist_sun_jupiter), initial_speed=(-constants.speed_jupiter, 0) )
        self.color = (205, 133, 63)

class saturn(celestial_body):
    def __init__(self):
        super().__init__(mass=constants.mass_saturn, radius=constants.radius_saturn, initial_position=(0, constants.dist_sun_saturn), initial_speed=(-constants.speed_saturn, 0) )
        self.color = (210, 180, 140)

class uranus(celestial_body):
    def __init__(self):
        super().__init__(mass=constants.mass_uranus, radius=constants.radius_uranus, initial_position=(0, constants.dist_sun_uranus), initial_speed=(-constants.speed_uranus, 0) )
        self.color = (72, 209, 204)

class neptune(celestial_body):
    def __init__(self):
        super().__init__(mass=constants.mass_neptune, radius=constants.radius_neptune, initial_position=(0, constants.dist_sun_neptune), initial_speed=(-constants.speed_neptune, 0) )
        self.color = (80, 80, 180)
