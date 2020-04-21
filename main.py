from field import field
from bodies import gopher, grenade
from random import randint

def title():
    print("welcome to gopher field!")
    print("here's a 10x10 grassy field")


def populate(place):
    print("\n3 sneaky gophers are hiding in there")
    gophers = [gopher(randint(0,9),randint(0,9)) for i in range(0,3)]
    for g in gophers:
        print(g.x, g.y)
        place.loadbod(g)
    place.display()

def clean(x):
    err = False
    try:
        x = int(x)
        if x < 10 & x >= 0:
            print("out of bounds")
        return err, x
    except:
        print("not an int")



def throw(place):
    print("Throw a water balloon!")
    err = True
    while err:
        err, x = clean(input('x coordinate for a water balloon'))
        err, y = clean(input('y coordinate for a water balloon'))
    print("a water balloon at %s" % [x,y])
    place.loadbod(grenade(x,y))
    place.display()

def quit():
    if input("q to quit").upper()=="Q":
        return False
    else:
        return True

keepgoing = True
title()
f = field(10)
f.display()
populate(f)
while keepgoing == True:
    throw(f)
    keepgoing = quit()
