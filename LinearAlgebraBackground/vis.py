import numpy as np
import matplotlib.pyplot as plt
# Use the correct image vectors from A^T
img_vec1 = np.array([1, 2, 3])
img_vec2 = np.array([0, 1, 4])

# Kernel vector (same)
kernel_vector = np.array([5, -4, 1])
kernel_vector = kernel_vector / np.linalg.norm(kernel_vector)

# Create the 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the kernel direction
ax.quiver(0, 0, 0, kernel_vector[0], kernel_vector[1], kernel_vector[2],
          color='red', label='Kernel Vector (Null Space)', linewidth=2)

# Plot the true image vectors
ax.quiver(0, 0, 0, img_vec1[0], img_vec1[1], img_vec1[2],
          color='blue', label='Image Vector 1 (from Aᵗ)')
ax.quiver(0, 0, 0, img_vec2[0], img_vec2[1], img_vec2[2],
          color='green', label='Image Vector 2 (from Aᵗ)')

# Span the image plane using the real image vectors
s = np.linspace(-1.5, 1.5, 10)
t = np.linspace(-1.5, 1.5, 10)
S, T = np.meshgrid(s, t)
X = S * img_vec1[0] + T * img_vec2[0]
Y = S * img_vec1[1] + T * img_vec2[1]
Z = S * img_vec1[2] + T * img_vec2[2]
ax.plot_surface(X, Y, Z, color='lightblue', alpha=0.4)

# Axis settings
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Accurate Image Plane vs Kernel Vector (Now Perpendicular!)')
ax.legend()

plt.tight_layout()
plt.show()
