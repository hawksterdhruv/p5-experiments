def setup():
    size(800,800)
    background(0)
    layers = 6
    stroke(255)
    strokeWeight(1)
    # textColor
    for i in range(layers):
        for j in range(2**i):
            x = (j+1)*width/(2**i+1)
            y = (i+1)*height/(layers+1)
            next_x_left = (2*j+1)*width/(2**(i+1)+1)
            next_x_right =  ((2*j+1)+1)*width/(2**(i+1)+1)
            next_y = (i+2)*height/(layers+1)
            if i < layers-1:
                line(x,y,next_x_left,next_y)
                line(x,y,next_x_right,next_y)
            fill(255)
            circle(x,y,30)
            fill(0)
            textAlign(CENTER, CENTER);
            text('32',x,y)
    
    
def draw():
    pass
