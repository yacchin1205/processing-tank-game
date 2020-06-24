def is_observable(world, heroes, enemy):
    return True


class WrappedWorld:
    def __init__(self, world):
        self.cell_size = world.cell_size
        self.grid_width = world.grid_width
        self.grid_height = world.grid_height
        self.grid = [row.copy() for row in world.grid]

class WrappedTank:
    def __init__(self, id, tank, is_hero):
        self.id = id
        self.x = tank.x
        self.y = tank.y
        self.dead = tank.dead
        if is_hero:
            self.body_rot = tank.body_rot
            self.gun_rot = tank.gun_rot

class WrappedBullet:
    def __init__(self, bullet):
        self.x = bullet.x
        self.y = bullet.y

class Environment:
    def __init__(self, world, heroes, enemies, bullets):
        self.world = WrappedWorld(world)
        self.heroes = [WrappedTank(i, h, True) for i, h in enumerate(heroes)]
        self.enemies = [WrappedTank(i, e, False) for i, e in enumerate(enemies)
                        if is_observable(self.world, heroes, e)]
        self.bullets = [WrappedBullet(b) for b in bullets]
