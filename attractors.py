import math

class Attractors:
    def lorenz(x, y, z, s=10, r=28, b=8/3):
        x_dot = s*(y - x)
        y_dot = r*x - y - x*z
        z_dot = x*y - b*z
        return x_dot, y_dot, z_dot

    def aizawa(x, y, z, a=0.95, b=0.7, c=0.6, d=3.5, e=0.25, f=0.1):
        x_dot = (z-b)*x - d*y
        y_dot = d*x + (z-b)*y
        z_dot = c + a*z - math.pow(z, 3)/3 - math.pow(x, 2) + f*z*math.pow(x, 3)
        return x_dot, y_dot, z_dot
    
    def newton_leipnik(x, y, z, a=0.3, b=0.6, c=5.7):
        x_dot = a*(y-x)+y*x
        y_dot = b*(x-z)-math.pow(x, 2)
        z_dot = c*(x*y-z)
        return x_dot, y_dot, z_dot