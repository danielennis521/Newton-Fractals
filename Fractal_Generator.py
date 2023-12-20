import numpy as np
import matplotlib.pyplot as plt
import random
from PIL import Image


def eval_poly(p, x):
    s = p[0]
    for i in range(1,len(p)):
        s = s*x + p[i]
    return s


def eval_poly_deriv(p, x):
    n = len(p)
    dp = [p[i]*(n-i-1) for i in range(0, n-1)]
    return eval_poly(dp, x)


def newton_counter(p, x0):
    xp = x0+1
    xc = x0
    c = 0
    while np.abs(xc - xp) > 1e-20:
        xp = xc
        dxc = eval_poly_deriv(p, xc)
        if dxc == 0.0:
            xc = xc - eval_poly(p, xc)/ eval_poly_deriv(p, xc + 0.00001)
        else:
            xc = xc - eval_poly(p, xc)/dxc
        c = c+1
        if c == 50:
            break

    return xc, c


def generate_fractal(p, resolution, filename = 'oooo_pretty'):
    r = np.roots(p)
    print(r)
    colors = {}
    for root in r:
        colors[root] = [random.randrange(1,7), random.randrange(1,7), random.randrange(1,7)]

    max_mod = np.max(np.abs(r))
    window = max_mod
    
    fractal = []
    for X in np.arange(-window, window, 2.0*window/resolution):
        fractal.append([])
        for Y in np.arange(window, -window, -2.0*window/resolution):
            root, steps = newton_counter(p, X+Y*1.0j)
            #print(root)
            check = False
            for r in colors:
                if np.abs(r - root) < 1e-3:
                    fractal[-1].append((colors[r][0]*steps, colors[r][1]*steps, colors[r][2]*steps))
                    check = True
            if not check:
                fractal[-1].append((0, 0, 0))
        #print(len(fractal[-1]))
    array = np.array(fractal, dtype=np.uint8)
    new_image = Image.fromarray(array)
    new_image.save(filename+'.png')



# enter whatever values you want to use as coefficients in an array, the first entry should be the leading coefficient
# ex. [1, 2, 3, 4] <=> x^3 + 2x^2 + 3x + 4
# the resolution is the number of points along one axis that you want to be computed

p = [1, 1, -0.5, 1, 1, 0.5, -1]

generate_fractal(p, 2048.0)