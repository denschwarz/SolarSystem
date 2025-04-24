import pygame
import argparse
import math
import celestial_bodies
import physics
import constants

width, height = 1200, 1200
scale = 1.0/(5*10**12)
scale = 1.0/(5*10**11)


def screen_position(pos, focus=(0,0)):
    (x,y) = pos
    (x_focus, y_focus) = focus
    x_rel = x - x_focus
    y_rel = y - y_focus
    screen_x = width/2 + x_rel*scale * width/2
    screen_y = height/2 - y_rel*scale * height/2
    return (screen_x, screen_y)

def screen_radius(radius, isSun):
    additional_factor = 50000 if isSun else 1000000
    screen_radius = radius*scale*additional_factor
    return screen_radius

def draw_canvas(screen, days, mass_sun):
    font = pygame.font.SysFont(None, 30)
    title = f"Solar System"
    text_title = font.render(title, True, (255,255,255),(0,0,0))
    text_title_rect = text_title.get_rect()
    text_title_rect.center = 70, 20
    screen.blit(text_title, text_title_rect)
    day_counter = f"days since start = {days}"
    text_counter = font.render(day_counter, True, (255,255,255),(0,0,0))
    text_counter_rect = text_counter.get_rect()
    text_counter_rect.center = width/2, 20
    screen.blit(text_counter, text_counter_rect)
    sun_mass_string = f"M_sun = {mass_sun/constants.mass_sun:.2f} M_sun"
    text_sun = font.render(sun_mass_string, True, (255,255,255),(0,0,0))
    text_sun_rect = text_sun.get_rect()
    text_sun_rect.center = width-120, 20
    screen.blit(text_sun, text_sun_rect)

def draw_celestial(screen, body, focus_point):
    for pos in body.trail:
        pygame.draw.circle(screen, desaturate_color(body.color, 0.5), screen_position(pos, focus_point), 1 )
    pygame.draw.circle(screen, body.color, screen_position(body.position, focus_point), screen_radius(body.radius, body.isSun) )

def desaturate_color(color, amount=0.5):
    r, g, b = color
    gray = int(0.299 * r + 0.587 * g + 0.114 * b)
    return (
        int(r * (1 - amount) + gray * amount),
        int(g * (1 - amount) + gray * amount),
        int(b * (1 - amount) + gray * amount)
    )

def main(mode=None):
    # Display settings
    pygame.init()
    FPS  = 30
    W, H = width, height
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((W, H))
    counter = pygame.time.get_ticks()

    # let there be light
    sun = celestial_bodies.sun()
    planets = {
        "mercury": celestial_bodies.mercury(),
        "venus":   celestial_bodies.venus(),
        "earth":   celestial_bodies.earth(),
        "mars":    celestial_bodies.mars(),
        "jupiter": celestial_bodies.jupiter(),
        "saturn":  celestial_bodies.saturn(),
        "uranus":  celestial_bodies.uranus(),
        "neptune": celestial_bodies.neptune(),
    }

    running = True
    speed_factor = 10000
    time_current = pygame.time.get_ticks()
    time_start = time_current
    while running:
        # Calculate time based on pygame ticks
        time_old = time_current
        time_current = pygame.time.get_ticks()
        time_delta = (time_current-time_old)*speed_factor
        days = int((time_current-time_start)*speed_factor/(3600*24))

        # Optional modes
        if mode in ["gain"]:
            factor = (1+days/100)
            sun.mass = factor*constants.mass_sun
            sun.radius = factor**(1/3)*constants.radius_sun
        elif mode == "shrink":
            factor = 2*(1- 1.0/(1.0+math.exp(-days/1000)))
            sun.mass = factor*constants.mass_sun
            sun.radius = factor**(1/3)*constants.radius_sun


        # Get acceleration from gravitational force, apply it and move
        for p in planets.keys():
            accelaration = physics.gravity_accelaration(m1=planets[p].mass, m2=sun.mass, pos1=planets[p].position, pos2=sun.position )
            planets[p].accelerate(time_delta, accelaration)
            planets[p].move(time_delta)

        # Set a focus point
        focus_point = sun.position

        # Draw objects
        screen.fill((10, 10, 30))
        draw_canvas(screen, days, sun.mass)
        draw_celestial(screen, sun, focus_point)
        for p in planets.keys():
            draw_celestial(screen, planets[p], focus_point)

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Solar system.")
    parser.add_argument("--mode", type=str, default=None)
    args = parser.parse_args()

    modes = ["gain", "shrink"]

    if args.mode is not None and args.mode not in modes:
        raise ValueError(f"Mode '{args.mode}' is not availabel! Valid options: {modes}")

    main(mode=args.mode)
