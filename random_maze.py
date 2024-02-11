file = open("random-maze.py", mode="rt", encoding="ascii")
random_maze_repr = file.read()
file.close()

random_maze = set()
for line in random_maze_repr.splitlines():
    line = line.strip()
    if line not in ("{", "}", ""):
        core = line[1:-2]
        x, y = core.split(",")
        x, y = int(x.strip()), int(y.strip())
        random_maze.add((x, y))

random_maze = eval(maze_repr)

def load_maze(filename):
    file = open(filename, mode="rt", encoding="ascii")
    maze_repr = file.read()
    file.close()
    maze = eval(maze_repr)
    return maze

random_maze = load_maze("random-maze.py")

