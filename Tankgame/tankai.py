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

# Tank AI - Nothing to do
class TankAI:
    def __init__(self, name='Unknown'):
        self.name = name

    def perform(self, env):
        return [Operation() for h in env.heroes]
