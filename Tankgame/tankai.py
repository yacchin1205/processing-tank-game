class Operation:
    def __init__(self):
        self.key_drive = False
        self.key_turn_left = False
        self.key_turn_right = False
        self.key_reverse = False
        self.key_aim_left = False
        self.key_aim_right = False
        self.key_shoot = False
        self.key_build = False

    def applyTo(self, tank):
        for attr in dir(self):
            if not attr.startswith('key_'):
                continue
            setattr(tank, attr, getattr(self, attr))

# AI Manager
class Manager:
    def __init__(self):
        self.logs = []

    def reset(self):
        self.logs = []

    def log(self, world, heroes, enemies, bullets):
        self.logs.append((world.copy(), [h.copy() for h in heroes], [e.copy() for e in enemies], [b.copy() for b in bullets]))

    def get_frames(self):
        count = 0
        while len(self.logs) == 0 or (any([not t.dead for t in self.logs[-1][1]]) and any([not t.dead for t in self.logs[-1][2]])):
            count += 1
            yield count

# Tank AI - Nothing to do
class TankAI:
    def __init__(self, name='Unknown'):
        self.name = name

    def perform(self, env):
        return [Operation() for h in env.heroes]
