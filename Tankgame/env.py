class WrappedWorld:
    def __init__(self, world):
        self.grid_width = world.grid_width
        self.grid_height = world.grid_height
        self.grid = [row.copy() for row in world.grid]

class WrappedTank:
    def __init__(self, tank, is_hero):
        self.x = tank.x
        self.y = tank.y
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
        self.heroes = [WrappedTank(h, True) for h in heroes]
        self.enemies = [WrappedTank(e, False) for e in enemies]
        self.bullets = [WrappedBullet(b) for b in bullets]
