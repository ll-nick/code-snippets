import math
import numpy as np
 
"""
Efficient method to compute the inverse of an affine transformation.
"""

def inverse_transformation(tf):
    R = tf[:3, :3]
    R_inv = np.transpose(R)
    t = tf[:3, 3].reshape(3,1)
    t_inv = -np.matmul(R_inv,t)
    tf_inv = np.block([[R_inv, t_inv], [np.zeros(3), 1]])

    return tf_inv

def example():
    # Define example transformation
    phi = math.pi
    cosp = math.cos(phi)
    sinp = math.sin(phi)
    
    # Rotation matrix
    R = np.array([[cosp, -sinp, 0],[sinp, cosp, 0],[0, 0, 1]])
    # Translation vector
    t = np.array([[1, 1, 1]]).T
    # Affine transformation
    tf = np.block([[R, t], [np.zeros(3), 1]])

    tf_inv = inverse_transformation(tf)

    print("Input transformation:\n{}".format(tf))
    print("Inverse transformation:\n{}".format(tf_inv))

if __name__=="__main__":
    example()