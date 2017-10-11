from graphics import *
import math

win = GraphWin("Shapes", 639, 599)
win.setBackground('black')

#Inputs
x1, y1 = [int(x) for x in input("Enter the x/y coordinates for point 1: ").split()]
x2, y2 = [int(x) for x in input("Enter the x/y coordinates for point 2: ").split()]
centerX, centerY = [int(x) for x in input("Enter the center for the circle: ").split()]
radius = int(input("Enter the radius for the circle: "))

#Points for the line
pt1 = Point(x1, y1)
pt2 = Point(x2, y2)
#Draw the Actual Line 
line = Line(pt1, pt2)
line.setOutline('white')
line.draw(win)

#Mid Point
midPointX = (x1+x2) / 2
midPointY = (y1+y2) / 2

#Calculates the length of the line
lineLength = math.sqrt(pow((x1-x2), 2) + pow((y1-y2), 2))

#Points for the three small Circles
cirPt1 = Point(x1, y1)
cirPt2 = Point(x2, y2)
cirMid = Point(midPointX, midPointY)
#Three Small circles
circle1 = Circle(cirPt1, 10)
circle1.setOutline('white')
circle1.draw(win)
circle2 = Circle(cirPt2, 10)
circle2.setOutline('white')
circle2.draw(win)
circleMid = Circle(cirMid, 10)
circleMid.setOutline('white')
circleMid.draw(win)

#Horizontal Line
hxp = Point(0, 350)
hyp = Point(639, 350)
horLine = Line(hxp, hyp)
horLine.setOutline('white')
horLine.draw(win)

#Circle beneath the horizontal line from the prompt
cirp = Point(centerX, centerY)
Cir = Circle(cirp, radius)
Cir.setOutline('white')
Cir.draw(win)

print("\nLine length is:", lineLength)
print("Midpoint of the line is: (", midPointX, ",", midPointY, ")")
print("Point 1: (", x1, ",", y1, ")")
print("Point 1: (", x2, ",", y2, ")")
    
win.getMouse()
win.close()