import random

def grid():
    fill(0)
    stroke(255)
    strokeWeight(5)
    rect(10,10,390,390)
    stroke(255)
    strokeWeight(5)
    fill(210)
    for i in range(5):
        x = 0
        line(0,80*i,400,80*i)
    
    


def setup():
    size(400,400)
    background(255)
    grid()
    
