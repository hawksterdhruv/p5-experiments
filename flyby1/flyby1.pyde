# terrain = []
w = 1200
h = 800
rect_size = 20
rows = h / rect_size
cols = w / rect_size
flying = 0


def setup():
    size(800, 600, P3D)
    background(0)


def draw():
    background(0)
    global flying
    flying -= 0.01
    yoff = flying
    terrain = []
    for y in range(rows):
        terrain.append([])
        xoff = 0
        for x in range(cols):
            terrain[y].append(map(noise(xoff, yoff), 0, 1, -100, 100))
            xoff += 0.1
        yoff += 0.1

    translate(w / 2, h / 2)
    rotateX(PI / 3)
    translate(-w / 2 - 200, -h / 2)
    noFill()
    stroke(255)
    strokeWeight(1)
    # vertex(0,0)
    for x in range(cols - 1):
        beginShape(TRIANGLE_STRIP)

        for y in range(rows - 1):
            # rect(x*rect_size, y*rect_size,rect_size,rect_size)
            x1 = x * rect_size
            y1 = y * rect_size
            x2 = (x + 1) * rect_size
            y2 = (y) * rect_size
            # x3 = (x + 1) * rect_size
            # y3 = (y + 1) * rect_size
            # print((x1, y1), (x2, y2))
            vertex(x1, y1, terrain[y][x])
            vertex(x2, y2, terrain[y][x + 1])
            # vertex(x3, y3)
            # triangle(x1,y1,x2,y2,x3,y3)
        endShape()
