# source     : https://www.youtube.com/watch?v=gBC_Fd8EE8A
# self-solved: true

maze = (
        (1, 3),
        (0, 2),
        (1,),
        (0, 4),
        (3, 5, 7),
        (4,),
        (3,),
        (4, 8),
        (7,)
)

visited = [0]
path = [0]
current_pos = 0
while current_pos != 8:

    possible_directions = maze[current_pos]

    d = 0
    while d < len(possible_directions) and possible_directions[d] in visited:
        d += 1

    if d == len(possible_directions):
        path.pop()
        current_pos = path[-1]
        continue

    current_pos = possible_directions[d]
    visited.append(possible_directions[d])
    path.append(possible_directions[d])

    print("visited -> ", visited)
    print("path    -> ", path)
    print()
