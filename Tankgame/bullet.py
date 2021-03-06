class Bullet(object):
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

        self.speed = 5
        self._size = 5

        self.removed = False

    def copy(self):
        b = Bullet(self.x, self.y, self.direction)
        b.speed = self.speed
        b._size = self._size
        b.removed = self.removed
        return b

    def update(self):
        self.x += self.speed * cos(radians(self.direction))
        self.y += self.speed * sin(radians(self.direction))

    def render(self):
        fill(255, 0, 0)
        ellipse(self.x, self.y, self._size, self._size)
