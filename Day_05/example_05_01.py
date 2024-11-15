# Storing coordinates of points as tuples in a list
points = [(1, 2), (3, 4), (5, 6)]

for point in points:
    x, y = point  # Unpacking the tuple
    print(f"Point: {point}, X: {x}, Y: {y}")
