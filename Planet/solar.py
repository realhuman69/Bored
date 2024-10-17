import pygame
import numpy as np

# Constants
G = 6.67430e-11  # Gravitational constant
AU = 1.496e11  # Astronomical Unit (m)
TIME_STEP = 36000  # 1 hour

class Body:
    def __init__(self, name, mass, position, velocity, color):
        self.name = name
        self.mass = mass
        self.position = np.array(position, dtype='float64')
        self.velocity = np.array(velocity, dtype='float64')
        self.acceleration = np.zeros(2)
        self.color = color

    def update_position(self, dt):
        self.position += self.velocity * dt

    def update_velocity(self, dt):
        self.velocity += self.acceleration * dt

    def apply_force(self, force):
        self.acceleration = force / self.mass

def gravitational_force(body1, body2):
    dist_vector = body2.position - body1.position
    distance = np.linalg.norm(dist_vector)
    force_magnitude = (G * body1.mass * body2.mass) / distance**2
    force_direction = dist_vector / distance
    return force_magnitude * force_direction

def update_system(bodies, dt):
    forces = {body: np.zeros(2) for body in bodies}

    # Calculate gravitational forces
    for i, body1 in enumerate(bodies):
        for body2 in bodies[i+1:]:
            force = gravitational_force(body1, body2)
            forces[body1] += force
            forces[body2] -= force

    # Apply forces and update positions/velocities
    for body in bodies:
        body.apply_force(forces[body])
        body.update_velocity(dt)
        body.update_position(dt)

def draw_bodies(screen, bodies):
    for body in bodies:
        x, y = int(body.position[0] / AU * 50 + 600), int(body.position[1] / AU * 50 + 450)
        pygame.draw.circle(screen, body.color, (x, y), 5)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1200, 900))
clock = pygame.time.Clock()

# Create bodies (Sun and planets)
sun = Body("Sun", 1.989e30, [0, 0], [0, 0], (255, 255, 0))  # Sun
mercury = Body("Mercury", 3.285e23, [0.387 * AU, 0], [0, 47360], (169, 169, 169))  # Mercury
venus = Body("Venus", 4.867e24, [0.723 * AU, 0], [0, 35020], (255, 215, 0))  # Venus
earth = Body("Earth", 5.972e24, [AU, 0], [0, 29780], (0, 0, 255))  # Earth
mars = Body("Mars", 6.39e23, [1.524 * AU, 0], [0, 24100], (255, 0, 0))  # Mars
jupiter = Body("Jupiter", 1.898e27, [5.203 * AU, 0], [0, 13070], (255, 165, 0))  # Jupiter
saturn = Body("Saturn", 5.683e26, [9.537 * AU, 0], [0, 9690], (210, 180, 140))  # Saturn
uranus = Body("Uranus", 8.681e25, [19.191 * AU, 0], [0, 6810], (0, 255, 255))  # Uranus
neptune = Body("Neptune", 1.024e26, [30.07 * AU, 0], [0, 5430], (0, 0, 128))  # Neptune

bodies = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update_system(bodies, TIME_STEP)
    draw_bodies(screen, bodies)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
