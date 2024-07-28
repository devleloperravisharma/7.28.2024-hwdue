import pgzrun

from random import randint

from time import time

TITLE = "Alphabetical fruit connections!"

WIDTH = 800

HEIGHT = 750

fruits = []

lines = []

start_time = 0

end_time = 0

total_time = 0

num_fruits = 5

next_fruits = 0



def create_fruits():

    global start_time


    b = Actor("banana")
    b.pos = randint(50, WIDTH-50), randint(50, HEIGHT-50)
    fruits.append(b)

    bl = Actor("blueberry")
    bl.pos = randint(50, WIDTH-50), randint(50, HEIGHT-50)
    fruits.append(bl)

    m = Actor("mango")
    m.pos = randint(50, WIDTH-50), randint(50, HEIGHT-50)
    fruits.append(m)

    s = Actor("strawberry")
    s.pos = randint(50, WIDTH-50), randint(50, HEIGHT-50)
    fruits.append(s)

    w = Actor("watermelon")
    w.pos = randint(50, WIDTH-50), randint(50, HEIGHT-50)
    fruits.append(w)


    start_time = time()


def draw():
    global total_time

    screen.blit("pink", (0,0))

    number = 1

    for fruit in fruits:

        screen.draw.text(str(number), (fruit.pos[0], fruit.pos[1]+10))

        fruit.draw()
        number += 1
    
    for l in lines:
        screen.draw.line(l[0], l[1], (255,213,213))
    
    if next_fruits<num_fruits:
        
        total_time = time()-start_time
        screen.draw.text(str(round(total_time, 1)), (10,10), fontsize = 30)
    else:
        screen.draw.text(str(round(total_time, 1)), (10,10), fontsize = 30)

def update():
    pass



def on_mouse_down(pos):

    global next_fruits, end_time, lines

    if next_fruits < num_fruits:
        if fruits[next_fruits].collidepoint(pos):
            if next_fruits:
                lines.append((fruits[next_fruits - 1].pos, fruits[next_fruits].pos))
                print((fruits[next_fruits - 1].pos, fruits[next_fruits].pos))
            next_fruits += 1
            print(next_fruits)
        else:
            lines = []
            next_fruits = 0




    

create_fruits()
pgzrun.go()