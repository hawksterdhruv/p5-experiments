w = 800
h = 800
order = 2


def hilbert(i):
    k = i % 3
    if k == 0:
        return (0, 0)
    elif k == 1:
        return (0, 1)
    elif k == 2:
        return (1, 1)
    elif k == 3:
        return (1, 0)
    l = i / 4


def setup():
    size(800, 800)
    n = int(pow(2, order))
    grid_size = w / n
    print(n)
    print(grid_size)
    print(n * n)


def draw():
    background(0)
    n = int(pow(2, order))
    # n = int(pow(2, order))
    grid_size = w / n
    noFill()
    # stroke(255)
    # strokeWeight(1)
    noStroke()
    for y in range(n):
        for x in range(n):
            rect(x * grid_size, y * grid_size, grid_size, grid_size)

    stroke(255)
    strokeWeight(1)
    beginShape()

    for i in range(n * n):
        point = hilbert(i)
        vertex(grid_size / 2 + grid_size * point[0], grid_size / 2 + grid_size * point[1])
        # for x in range(n):
        # hilbert()

    endShape()
