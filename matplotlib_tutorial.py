import numpy as np
import matplotlib.pyplot as plt

x1 = [2, 4, 6 ,7]
x2 = [1, 2, 3, 4]
y1 = [4, 3, 5, 1]
y2 = [4, 2, 3, 1]


plt.plot(x1, y1, 'b', x2, y2, 'r')

# Multiple subplots
# fig, ax = plt.subplots(2,2)
# print(ax.shape)
# ax[0,0].plot(np.arange(6))          <em># top left</em>
# ax[0,1].plot(np.arange(6,0,-1))     <em># top right</em>
# ax[1,0].plot((-1)**np.arange(6))    <em># bottom left</em>
# ax[1,1].plot((-1)**np.arange(1,7))  <em># bottom right</em>
# plt.show()

# Or

# plt.subplot(2, 2, 1)    <em># Note the 1-indexing of subplots. </em>
# plt.plot(np.arange(6))
# plt.subplot(2, 2, 2)
# plt.plot(np.arange(6, 0, -1))
# plt.subplot(2, 2, 3)
# plt.plot((-1)**np.arange(6))
# plt.subplot(2, 2, 4)
# plt.plot((-1)**np.arange(1, 7))
# plt.show()


def subfigures(arr: np.array):
    fig, ax = plt.subplots(1, 2)
    x1 = arr[:, 0]
    y1 = arr[:, 1]

    ax[0].plot(x1, y1)
    ax[1].scatter(x1, y1, c=arr[:, 2], s=arr[:, 3])

    ax[0].set_title("left plot")
    ax[1].set_title("right plot")
    fig.suptitle("suptitle")
    plt.savefig('test.png')


def main():
    a = np.array([[1, 2, 10, 1000], [2, 3, 20, 200], [3, 4, 30, 300], [4, 5, 40, 400]])
    subfigures(a)


if __name__ == "__main__":
    main()