from math import fabs, sqrt

def circleCircle(c1, c2):
    maxDist = c1.rad + c2.rad
    dx = c1.x - c2.x
    dy = c1.y - c2.y 
    dist = sqrt(dx * dx + dy * dy)
    return dist <= maxDist
    
def circleLine(c, l):
    dist = fabs((l.y2 - l.y1) * c.x - (l.x2 - l.x1) * c.y  + l.x2 * l.y1 - l.y2 * l.x1) / l.getLength()
    if l.x2 > l.x1:
        minX = l.x1
        maxX = l.x2
    else:
        minX = l.x2
        maxX = l.x1
        
    if l.y2 > l.y1:
        minY = l.y1
        maxY = l.y2
    else:
        minY = l.y2
        maxY = l.y1
        
    return c.x + c.rad >= minX and c.y + c.rad >= minY and c.x - c.rad <= maxX and c.y - c.rad <= maxY and dist < c.rad