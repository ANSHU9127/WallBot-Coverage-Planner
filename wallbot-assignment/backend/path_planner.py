def is_inside_obstacle(x, y, obstacles):
    for obs in obstacles:
        if obs.x <= x <= obs.x + obs.width and obs.y <= y <= obs.y + obs.height:
            return True
    return False

def generate_trajectory(width, height, obstacles):
    path = []; step = 0.1; y = 0; direction = 1
    while y <= height:
        xr = (0, width) if direction == 1 else (width, 0)
        x = xr[0]
        while (x <= xr[1] and direction == 1) or (x >= xr[1] and direction == -1):
            if not is_inside_obstacle(x, y, obstacles):
                path.append((round(x,2), round(y,2)))
            x += step * direction
        y += step; direction *= -1
    return path