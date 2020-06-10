def is_observable(world, heroes, enemy):
    for i, hero in enumerate(heroes):
        hero_label = world.grid_label[min(int(hero.real_y / world.cell_size), len(world.grid) - 1)][min(int(hero.real_x / world.cell_size), len(world.grid[0]) - 1)]
        enemy_label = world.grid_label[min(int(enemy.real_y / world.cell_size), len(world.grid) - 1)][min(int(enemy.real_x / world.cell_size), len(world.grid[0]) - 1)]
        if hero_label == enemy_label:
            return True
    return False

def flood_fill(grid, empty_label, start_label):
    next_label = start_label
    while True:
        empty = None
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == empty_label:
                    empty = (x, y)
                    break
            if empty is not None:
                break
        if empty is None:
            # finished
            break
        x, y = empty
        _flood_fill(grid, x, y, empty_label, next_label)
        next_label += 1
    return grid

def _flood_fill(grid, x, y, empty_label, label):
    grid[y][x] = label
    targets = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    for x_, y_ in targets:
        if x_ < 0 or y_ < 0 or x_ >= len(grid[0]) or y_ >= len(grid):
            continue
        if grid[y_][x_] != empty_label:
            continue
        grid[y_][x_] = label
        _flood_fill(grid, x_, y_, empty_label, label)


class WrappedWorld:
    def __init__(self, world):
        self.cell_size = world.cell_size
        self.grid_width = world.grid_width
        self.grid_height = world.grid_height
        self.grid = [row.copy() for row in world.grid]
        self.grid_label = flood_fill([row.copy() for row in world.grid], 0, 2)

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
