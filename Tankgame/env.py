def is_observable(world, heroes, enemy):
    for hero in heroes:
        dx = enemy.x - hero.x
        dy = enemy.y - hero.y
        observable = True
        if abs(dx) > abs(dy):
            a = dy / dx
            for x in range(int(min(enemy.x, hero.x)), int(max(enemy.x, hero.x))):
                y = a * (x - hero.x) + hero.y
                if world.grid[min(int(y / world.cell_size), len(world.grid) - 1)][min(int(x / world.cell_size), len(world.grid[0]) - 1)] == 1:
                    observable = False
                    break
        else:
            a = dx / dy
            for y in range(int(min(enemy.y, hero.y)), int(max(enemy.y, hero.y))):
                x = a * (y - hero.x) + hero.y
                if world.grid[min(int(y / world.cell_size), len(world.grid) - 1)][min(int(x / world.cell_size), len(world.grid[0]) - 1)] == 1:
                    observable = False
                    break
        if observable:
            return True
    return False


class WrappedWorld:
    def __init__(self, world):
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
                        if is_observable(world, heroes, e)]
        self.bullets = [WrappedBullet(b) for b in bullets]
