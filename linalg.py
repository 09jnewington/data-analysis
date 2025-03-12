# y = a1x +b1
# y = a2x + b2

# ...

# a1x - y = -b1
# a2x - y = -b2

# [[a1, -1], [a2, -1]] * [x, y] = [-b1, -b2]
import numpy as np

def meeting_lines(a1, a2, b1, b2):
    a = np.array([[a1, -1], [a2, -1]])
    b = np.array([-b1, -b2])
    c = np.linalg.solve(a, b)
    return c

def meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    # z = a1y + b1x + c1
    # a1y + b1x - z = -c1
    # a2y + b2x - z = -c2
    # a3y + b3x - z = -c3
    # [[b1, a1, -1], [b2, a2, -1], [b3, a3, -1]] * [x, y, z] = [-c1, -c2, -c3]

    a = np.array([[b1, a1,  -1], [b2, a2, -1], [b3, a3, -1]])
    b = np.array([-c1, -c2, -c3])
    c = np.linalg.solve(a, b)
    return c

def main():
    a1 = 1
    b1 = 4
    c1 = 5
    a2 = 3
    b2 = 2
    c2 = 1
    a3 = 2
    b3 = 4
    c3 = 1

    x, y, z = meeting_planes(a1, b1, c1, a2, b2, c2, a3, b3, c3)
    print(f"Planes meet at x={x}, y={y} and z={z}")


if __name__ == '__main__':
    main()