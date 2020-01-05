import math
import matplotlib.pyplot as plt

π = math.pi

midpoint_x = math.cos(π/3)  # 60° round the circle
midpoint_y = math.sin(π/3)


def float_range(min, max):
    # simple hack to get an array of values between two numbers, incrementing
    # in steps of 0.01
    # If we had numpy we could just call `frange`
    return [x/100.0 for x in range(int(min * 100), int(max * 100))]


def setup_plot():
    plt.gca().set_aspect('equal', adjustable='datalim')


def draw_unit_circle():
    xs = []
    ys = []

    for θ in float_range(-π, π):
        xs.append(math.cos(θ))
        ys.append(math.sin(θ))
    plt.plot(xs, ys)


def draw_circle(centre, r):
    x, y = centre

    xs = []
    ys = []
    for θ in float_range(-π, π):
        xs.append(x + r * math.cos(θ))
        ys.append(y + r * math.sin(θ))
    plt.plot(xs, ys)


def point_is_on_circle(point, center, radius):
    # show that point (px,py) is a solution to (px-c.x)^2 + (py-c.y)^2 = r^2
    # Since we're using floating-point numbers we need to allow for a margin
    # of error in our calculation
    ε = 0.0001

    cx, cy = center
    px, py = point
    return ((px - cx) ** 2) + ((py-cy) ** 2) - (radius ** 2) < ε


def draw_tangent(point, center, radius):
    if (not point_is_on_circle(point, center, radius)):
        print(point)
        raise Exception(
            "Point is not on the circumference of the circle")
    px, py = point
    cx, cy = center
    xs = [px - (py - cy),  px + (py - cy)]
    ys = [py + (px - cx),  py - (px - cx)]
    plt.plot(xs, ys)


setup_plot()

draw_circle([1, 2], 2)
for incr in range(0, 12):
    # pick 12 points on the circumference of the circle
    # of radius 2 centered at [1,2]
    x = 1 + (2 * math.cos(float(incr) * π / 6.0))
    y = 2 + (2 * math.sin(float(incr) * π / 6.0))

    draw_tangent([x, y], [1, 2], 2)
plt.show()
