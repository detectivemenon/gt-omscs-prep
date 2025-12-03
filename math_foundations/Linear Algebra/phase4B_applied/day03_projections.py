import numpy as np
def project_onto(u: np.ndarray, v: np.ndarray) -> np.ndarray:
    """
    Return the projection of v onto u.

    proj_u(v) = ((v·u) / (u·u)) * u
    """
    # Convert to arrays just in case
    u = np.array(u, dtype=float)
    v = np.array(v, dtype=float)

    denom = np.dot(u, u)
    if denom == 0:
        raise ValueError("Cannot project onto the zero vector.")

    scalar = np.dot(v, u) / denom
    return scalar * u

def demo_projection_basic():
    u = np.array([4, 0], dtype=float)
    v = np.array([3, 1], dtype=float)

    proj = project_onto(u, v)
    residual = v - proj

    print("u:", u)
    print("v:", v)
    print("projection of v onto u:", proj)
    print("residual (v - proj):", residual)
    print("dot(u, residual):", np.dot(u, residual))

def demo_projection_tilted():
    u = np.array([2, 1], dtype=float)   # some tilted direction
    v = np.array([3, 4], dtype=float)   # arbitrary vector

    proj = project_onto(u, v)
    residual = v - proj

    print("\n---- Tilted example ----")
    print("u:", u)
    print("v:", v)
    print("projection of v onto u:", proj)
    print("residual (v - proj):", residual)
    print("dot(u, residual):", np.dot(u, residual))

if __name__ == "__main__":
    demo_projection_basic()
    demo_projection_tilted()