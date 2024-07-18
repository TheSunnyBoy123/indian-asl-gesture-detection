import math
from support import *


def transformation(base_point_a, base_point_b):
    """
    Given two points, returns the angle and distance between them needed for transforming the 2D coordinate system to assume these to be base points

    Args:
        base_point_a: The point to become origin
        base_point_b: The point to become (100,0) on x-axis

    Returns:
        current_angle, distance: The angle of rotation currently between a-b line and origin and the 1/distance between the two points
    """
    current_angle_radian = math.atan2(base_point_b[1] - base_point_a[1], base_point_b[0] - base_point_a[0])
    current_angle = radian_to_degree(current_angle_radian)
    
    distance = 100/(math.sqrt((base_point_b[0] - base_point_a[0])**2 + (base_point_b[1] - base_point_a[1])**2))
    return current_angle, distance


if __name__ == "__main__":
    print(transformation([0, 0], [2,0])) # (0.7853981633974483, 1.4142135623730951)