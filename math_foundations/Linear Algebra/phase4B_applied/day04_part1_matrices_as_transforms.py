import numpy as np


def demo_matrix_stretch():
    """
    Demo 1: Horizontal stretch.
    A = [[2, 0],
         [0, 1]]
    Doubles x, leaves y unchanged.
    """
    A = np.array([[2.0, 0.0],
                  [0.0, 1.0]])

    # Some sample vectors
    vectors = np.array([
        [1, 0],   # e1
        [0, 1],   # e2
        [1, 1],   # diagonal
        [-1, 2]   # another arbitrary vector
    ])

    print("=== Demo 1: Horizontal stretch ===")
    print("Matrix A:\n", A)

    for v in vectors:
        w = A @ v
        print(f"v = {v}  ->  A v = {w}")
    print()


def demo_matrix_shear():
    """
    Demo 2: Shear transformation.
    B = [[1, 1],
         [0, 1]]

    Keeps y the same, shifts x by +y.
    """
    B = np.array([[1.0, 1.0],
                  [0.0, 1.0]])

    vectors = np.array([
        [1, 0],   # e1
        [0, 1],   # e2
        [1, 1],
        [-1, 2]
    ])

    print("=== Demo 2: Shear transformation ===")
    print("Matrix B:\n", B)

    for v in vectors:
        w = B @ v
        print(f"v = {v}  ->  B v = {w}")
    print()


def demo_columns_as_images_of_basis():
    """
    Demo 3: Columns of the matrix = images of basis vectors e1, e2.
    """
    M = np.array([[2.0, -1.0],
                  [1.0,  3.0]])

    e1 = np.array([1.0, 0.0])
    e2 = np.array([0.0, 1.0])

    print("=== Demo 3: Columns as images of e1, e2 ===")
    print("Matrix M:\n", M)

    Me1 = M @ e1
    Me2 = M @ e2

    print("M e1:", Me1, "  (should equal first column of M)")
    print("M e2:", Me2, "  (should equal second column of M)")

    print("First column of M:", M[:, 0])
    print("Second column of M:", M[:, 1])
    print()

    # Any vector v = x e1 + y e2:
    v = np.array([2.0, -1.0])  # 2*e1 + (-1)*e2
    left = M @ v
    right = 2 * Me1 + (-1) * Me2

    print("Check linear combo:")
    print("M v:", left)
    print("2 * M e1 + (-1) * M e2:", right)
    print()


def demo_linear_map_properties():
    """
    Demo 4: Show that M(u + v) = M u + M v and M(c u) = c M u
    for a sample matrix and vectors.
    """
    M = np.array([[1.0, 2.0],
                  [3.0, 4.0]])

    u = np.array([1.0, -1.0])
    v = np.array([2.0,  3.0])
    c = 3.0

    print("=== Demo 4: Linear map properties ===")
    print("Matrix M:\n", M)
    print("u:", u)
    print("v:", v)

    left_add = M @ (u + v)
    right_add = (M @ u) + (M @ v)
    print("\nCheck addition property:")
    print("M(u + v):", left_add)
    print("M u + M v:", right_add)

    left_scale = M @ (c * u)
    right_scale = c * (M @ u)
    print("\nCheck scalar property:")
    print("M(c u):", left_scale)
    print("c (M u):", right_scale)
    print()


if __name__ == "__main__":
    demo_matrix_stretch()
    demo_matrix_shear()
    demo_columns_as_images_of_basis()
    demo_linear_map_properties()