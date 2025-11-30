import numpy as np

def demo_dot_and_angle():
    """Compute dot product and angle between two vectors."""
    # You can change these later for more practice
    u = np.array([3, 4])
    v = np.array([10, 5])

    print("=== Dot Product & Angle ===")
    print("u:", u)
    print("v:", v)

    # Dot product
    dot = np.dot(u, v)
    print(f"u · v = {dot}")

    # Lengths (norms)
    norm_u = np.linalg.norm(u)
    norm_v = np.linalg.norm(v)
    print(f"‖u‖ = {norm_u:.3f}")
    print(f"‖v‖ = {norm_v:.3f}")

    # Cosine of the angle
    cos_theta = dot / (norm_u * norm_v)

    # Clip for safety (numerical issues can push slightly outside [-1, 1])
    cos_theta = np.clip(cos_theta, -1.0, 1.0)
    print(f"cos(θ) = {cos_theta:.6f}")

    # Angle in radians and degrees
    theta_rad = np.arccos(cos_theta)
    theta_deg = np.degrees(theta_rad)
    print(f"θ (radians) = {theta_rad:.6f}")
    print(f"θ (degrees) = {theta_deg:.2f}")


if __name__ == "__main__":
    demo_dot_and_angle()