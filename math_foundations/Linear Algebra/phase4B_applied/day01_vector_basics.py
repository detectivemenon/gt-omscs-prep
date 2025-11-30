import numpy as np

def demo_vector_creation():
    """Create simple vectors u and v, and compute their lengths."""
    u = np.array([3, 4])
    v = np.array([1, 2])

    print("=== Vector Creation ===")
    print("u:", u)
    print("v:", v)

    # Length (norm) of each vector
    norm_u = np.linalg.norm(u)
    norm_v = np.linalg.norm(v)
    print(f"‖u‖ (length of u) = {norm_u:.3f}")
    print(f"‖v‖ (length of v) = {norm_v:.3f}")
    print()


def demo_vector_scaling():
    """Show what happens when we scale a vector by different factors."""
    u = np.array([3, 4])

    print("=== Vector Scaling ===")
    print("Original u:", u)
    print("2 * u   =", 2 * u)
    print("-1 * u  =", -1 * u)
    print("0.5 * u =", 0.5 * u)
    print()


def demo_vector_addition():
    """Add two vectors elementwise."""
    u = np.array([3, 4])
    v = np.array([1, 2])

    print("=== Vector Addition ===")
    print("u:", u)
    print("v:", v)
    print("u + v =", u + v)
    print()


def demo_linear_combination():
    """Compute a*u + b*v for some scalars a, b."""
    u = np.array([3, 4])
    v = np.array([1, 2])

    a, b = 2, -1
    combo = a * u + b * v

    print("=== Linear Combination a*u + b*v ===")
    print("u:", u)
    print("v:", v)
    print(f"a = {a}, b = {b}")
    print("a*u + b*v =", combo)
    print()


if __name__ == "__main__":
    demo_vector_creation()
    demo_vector_scaling()
    demo_vector_addition()
    demo_linear_combination()