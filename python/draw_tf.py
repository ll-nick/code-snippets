import math
import numpy as np
from matplotlib import pyplot as plt

"""
A simple script to draw the 3 axes of a coordinate system defined by an affine transformation
"""


def draw_tf(ax, tf, axislength = 0.2, text = ''):
    # Definitions in local coordinate frame
    origin_loc = [0, 0, 0, 1]
    x_loc = [axislength, 0, 0, 1]
    y_loc = [0, axislength, 0, 1]
    z_loc = [0, 0, axislength, 1]
    text_pos_loc = [0, 0, -axislength/2, 1]

    # Transform using given tf
    origin_glob = np.matmul(tf, origin_loc)
    x_glob = np.matmul(tf, x_loc)
    y_glob = np.matmul(tf, y_loc)
    z_glob = np.matmul(tf, z_loc)
    text_pos_glob = np.matmul(tf, text_pos_loc)
    
    # Plot axes
    ax.plot([origin_glob[0], x_glob[0]], [origin_glob[1],x_glob[1]], [origin_glob[2],x_glob[2]], color='r')
    ax.plot([origin_glob[0], y_glob[0]], [origin_glob[1],y_glob[1]], [origin_glob[2],y_glob[2]], color='g')
    ax.plot([origin_glob[0], z_glob[0]], [origin_glob[1],z_glob[1]], [origin_glob[2],z_glob[2]], color='b')

    # Add text
    ax.text(text_pos_glob[0], text_pos_glob[1], text_pos_glob[2], text)

def example():
    axislength = 0.3

    # Origin coordinate system as reference
    origin = np.identity(4)

    # Rotated an translated coordinate system
    phi = math.pi
    cosp = math.cos(phi)
    sinp = math.sin(phi)
    
    # Rotation matrix
    R = np.array([[cosp, -sinp, 0],[sinp, cosp, 0],[0, 0, 1]])
    # Translation vector
    t = np.array([[1, 1, 1]]).T
    # Affine transformation
    tf = np.block([[R, t], [np.zeros(3), 1]])


    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    draw_tf(ax, origin, axislength, "Origin")
    draw_tf(ax, tf, axislength, "Transformation")

    plt.show()

if __name__=="__main__":
    example()