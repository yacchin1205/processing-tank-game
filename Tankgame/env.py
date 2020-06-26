import math

OBSTACLE_SIZE = 3

def is_observable(world, myself, target):
    dx = target.real_x - myself.real_x
    dy = target.real_y - myself.real_y
    rad = math.atan2(dy, dx)
    length = math.sqrt(dx ** 2 + dy ** 2)
    if length <= world.cell_size:
        return True
    obstacles = 0
    for i in range(1, math.ceil(length / world.cell_size)):
        tx = myself.real_x + math.cos(rad) * i * world.cell_size
        ty = myself.real_y + math.sin(rad) * i * world.cell_size
        for tdy_ in range(0, OBSTACLE_SIZE):
            tdy = (tdy_ - OBSTACLE_SIZE // 2) * world.cell_size
            for tdx_ in range(0, OBSTACLE_SIZE):
                tdx = (tdx_ - OBSTACLE_SIZE // 2) * world.cell_size
                yi = min(int((ty + tdy) / world.cell_size), len(world.grid) - 1)
                xi = min(int((tx + tdx) / world.cell_size), len(world.grid[0]) - 1)
                if world.grid[yi][xi] == 1:
                    obstacles += 1
        if obstacles >= OBSTACLE_SIZE * 3:
            # Obstacle found
            return False
    return True


class WrappedWorld:
    def __init__(self, world):
        self.cell_size = world.cell_size
        self.grid_width = world.grid_width
        self.grid_height = world.grid_height
        self.grid = [row.copy() for row in world.grid]

class WrappedTank:
    def __init__(self, id, tank):
        self.id = id
        self.x = tank.x
        self.y = tank.y
        self.dead = tank.dead
        self.body_rot = tank.body_rot
        self.gun_rot = tank.gun_rot

class WrappedBullet:
    def __init__(self, bullet):
        self.x = bullet.x
        self.y = bullet.y

class Environment:
    def __init__(self, world, myself, heroes, enemies, bullets):
        self.world = WrappedWorld(world)
        self.myself = WrappedTank([i for i, h in enumerate(heroes) if h == myself][0], myself)
        self.buddies = [WrappedTank(i, h) for i, h in enumerate(heroes)
                        if myself != h and is_observable(self.world, myself, h)]
        self.enemies = [WrappedTank(i, e) for i, e in enumerate(enemies)
                        if is_observable(self.world, myself, e)]
        self.bullets = [WrappedBullet(b) for b in bullets]
