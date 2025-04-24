from math import sqrt, asin, sin, cos

gravity_constant = 6.67430*10**(-11)

def distance(pos1, pos2):
    (x1,y1) = pos1
    (x2,y2) = pos2
    return sqrt( (x1-x2)**2 + (y1-y2)**2 )

def gravity_accelaration(m1, m2, pos1, pos2):
    r = distance(pos1, pos2)
    force_absolute = gravity_force(m1, m2, r)
    acc_absolute = force_absolute/m1
    (acc_X, acc_y) = get_components(acc_absolute, pos1, pos2)
    return (acc_X, acc_y)

def gravity_force(m1, m2, r):
    G = gravity_constant
    return m1*m2*G/(r**2)

def get_components(absolute_value, pos1, pos2):
    (comp_X, comp_Y) = force_direction(pos1, pos2)
    x = absolute_value * comp_X
    y = absolute_value * comp_Y
    return (x,y)

def force_direction(pos1, pos2):
    # return a normalized vector pointing from pos1 to pos2
    (x1,y1) = pos1
    (x2,y2) = pos2
    length = sqrt( (x1-x2)**2 + (y1-y2)**2 )
    x = (x2-x1)/length
    y = (y2-y1)/length
    return (x,y)
