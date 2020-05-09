import matplotlib.pyplot as plt
import numpy as np

a = 5
b = 1


def main():
    x = np.linspace(0, 20, 50)
    plt.grid()
    m2 = ((b + np.sqrt(b * b + 4 * a)) / 2, 0)
    print(m2)
    count = 15000
    step = 0.001
    points = [
        #[0.001, 0.002],
        #[0.5, 2],
        [1, 3],
        [2, 5],
        [0.001, 10],
        [0.01, 10],
        [4, 5],
        #[2.79128784747792, 0.02]
    ]

    while len(points) > 0:
        current_point = points.pop()
        x0 = current_point[0]
        y0 = current_point[1]

        pointsX = []
        pointsY = []
        curX = x0
        curY = y0
        for i in range(0, count):
            xSaved = curX
            curX = curX + step * f(curX, curY)
            curY = curY + step * g(xSaved, curY)
            pointsX.append(curX)
            pointsY.append(curY)

        plt.plot(pointsX, pointsY)

    plt.show()


def f(x, y):
    return (a + b * x - x * x) * x - x * y


def g(x, y):
    return x * y - y


if __name__ == '__main__':
    main()
