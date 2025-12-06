"""
Day 4 Part 2 – Geometric Transformations (Reflections + Shears)

This file is NOT about memorizing NumPy tricks. It’s here so you can:
- See reflections as simple 2x2 matrices
- See shears as simple 2x2 matrices
- Confirm numerically that “matrix as function” intuition is right
"""

import numpy as np


def apply_transform(A: np.ndarray, points: np.ndarray) -> np.ndarray:
    """
    Apply a 2x2 matrix A to a set of 2D points.

    points shape: (n, 2)  -> rows are [x, y]
    A shape:      (2, 2)

    Returns: transformed points, same shape as points.
    """
    return (A @ points.T).T


def demo_reflections():
    """
    Show a few simple reflections:

    - Across x-axis
    - Across y-axis
    - Across the line y = x
    """
    print("=== REFLECTIONS ===")

    # Three sample points
    pts = np.array([
        [2.0, 1.0],
        [-1.0, 2.0],
        [3.0, -2.0],
    ])
    print("Original points:\n", pts)

    # 1) Reflect across x-axis: (x, y) -> (x, -y)
    R_x = np.array([[1.0, 0.0],
                    [0.0, -1.0]])
    pts_rx = apply_transform(R_x, pts)
    print("\nReflection across x-axis (y -> -y):\n", pts_rx)

    # 2) Reflect across y-axis: (x, y) -> (-x, y)
    R_y = np.array([[-1.0, 0.0],
                    [0.0, 1.0]])
    pts_ry = apply_transform(R_y, pts)
    print("\nReflection across y-axis (x -> -x):\n", pts_ry)

    # 3) Reflect across line y = x: (x, y) -> (y, x)
    R_diag = np.array([[0.0, 1.0],
                       [1.0, 0.0]])
    pts_rdiag = apply_transform(R_diag, pts)
    print("\nReflection across line y = x (swap x,y):\n", pts_rdiag)


def demo_shears():
    """
    Show simple shear transformations:

    - x-shear (push horizontally depending on y)
    - y-shear (push vertically depending on x)
    """
    print("\n=== SHEARS ===")

    # Simple square-ish shape (4 corners)
    square = np.array([
        [0.0, 0.0],
        [1.0, 0.0],
        [1.0, 1.0],
        [0.0, 1.0],
    ])
    print("Original square:\n", square)

    # 1) Shear in x direction: (x, y) -> (x + k*y, y)
    kx = 1.0
    Sx = np.array([[1.0, kx],
                   [0.0, 1.0]])
    square_sx = apply_transform(Sx, square)
    print(f"\nX-shear with kx={kx} (x -> x + {kx}*y):\n", square_sx)

    # 2) Shear in y direction: (x, y) -> (x, y + k*x)
    ky = 0.5
    Sy = np.array([[1.0, 0.0],
                   [ky, 1.0]])
    square_sy = apply_transform(Sy, square)
    print(f"\nY-shear with ky={ky} (y -> y + {ky}*x):\n", square_sy)


def demo_composed_transforms():
    """
    Show that combining transforms is just multiplying matrices.

    Example:
        R = reflection across x-axis
        S = shear in x
        Combined = S @ R
    """
    print("\n=== COMPOSED TRANSFORMS (S @ R) ===")

    pts = np.array([
        [2.0, 1.0],
        [-1.0, 2.0],
    ])
    print("Original points:\n", pts)

    # Reflection across x-axis
    R_x = np.array([[1.0, 0.0],
                    [0.0, -1.0]])

    # X-shear
    kx = 1.0
    Sx = np.array([[1.0, kx],
                   [0.0, 1.0]])

    # Apply individually: first reflect, then shear
    pts_reflected = apply_transform(R_x, pts)
    pts_ref_then_shear = apply_transform(Sx, pts_reflected)

    print("\nAfter reflection across x-axis:\n", pts_reflected)
    print("\nAfter then applying x-shear:\n", pts_ref_then_shear)

    # Now do the same with one combined matrix:
    combined = Sx @ R_x  # do R first, then S
    pts_combined = apply_transform(combined, pts)
    print("\nCombined matrix Sx @ R_x:\n", combined)
    print("\nApplying combined once (should match above):\n", pts_combined)


if __name__ == "__main__":
    # Tiny smoke tests
    demo_reflections()
    demo_shears()
    demo_composed_transforms()