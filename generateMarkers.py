import cv2
import cv2.aruco as aruco
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd


def generateArucomarkers(x: int, y: int):
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)

    fig = plt.figure()
    nx = x
    ny = y
    for i in range(1, nx * ny + 1):
        ax = fig.add_subplot(ny, nx, i)
        img = aruco.drawMarker(aruco_dict, i, 700)
        plt.imshow(img, cmap='gray', interpolation="nearest")
        ax.axis("off")

    plt.savefig("_data/markers.pdf")
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generateArucomarkers(7, 5)  # Generate matrix 7,5
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    arucoParams = aruco.DetectorParameters_create()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
