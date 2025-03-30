import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define vertices
A = np.array([0.0, 0.0, 0.0])
B = np.array([1.0, 0.0, 0.0])
C = np.array([0.0, 0.0, 1.0])

# Define intersection points
intersection_L2 = np.array([0.0, 0.0, 0.5])
intersection_L3 = np.array([0.5, 0.0, 0.5])

# Create plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot triangle edges
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], 'b-', label='L1 (A to B)')
ax.plot([A[0], C[0]], [A[1], C[1]], [A[2], C[2]], 'r-', label='L2 (A to C)')
ax.plot([B[0], C[0]], [B[1], C[1]], [B[2], C[2]], 'g-', label='L3 (B to C)')

# Plot vertices
ax.scatter(A[0], A[1], A[2], color='black', s=50, label='Vertex A (0, 0, 0)')
ax.scatter(B[0], B[1], B[2], color='black', s=50, label='Vertex B (1, 0, 0)')
ax.scatter(C[0], C[1], C[2], color='black', s=50, label='Vertex C (0, 0, 1)')

# Plot intersection points
ax.scatter(intersection_L2[0], intersection_L2[1], intersection_L2[2], color='red', s=100, marker='o', label='Intersection L2')
ax.scatter(intersection_L3[0], intersection_L3[1], intersection_L3[2], color='green', s=100, marker='o', label='Intersection L3')

# Set labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Intersection of Triangle with Z=0.5 Plane')

# Set view angle
ax.view_init(elev=20, azim=30)

# Add a legend
ax.legend()

plt.show()
