import matplotlib.pyplot as plt
import matplotlib.patches as patches

def parse_maze(filename):
    with open(filename, 'r') as file:
        maze = [list(line.strip()) for line in file.readlines()]
    return maze

def visualize_maze(maze):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    ax.set_xlim(-0.5, len(maze[0]))
    ax.set_ylim(-0.5, len(maze))
    ax.set_xticks(range(len(maze[0])))
    ax.set_yticks(range(len(maze)))
    ax.grid(True)

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            assert(i  < len(maze) and j < len(maze[0]))
            # print(i)
            print(len(maze))
            print(len(maze[i]))
            # print(j)
            if maze[i][j] == '*':
                rect = patches.Rectangle((j, i), 1, 1, facecolor='black')
                ax.add_patch(rect)

    start_x, start_y = len(maze[0]) - 1, len(maze) - 1
    end_x, end_y = 0, 0

    plt.plot(start_x + 0.5, start_y + 0.5, 'go', markersize=10)
    plt.plot(end_x + 0.5, end_y + 0.5, 'ro', markersize=10)

    plt.title('Maze Visualization')
    plt.show()

if __name__ == '__main__':
    maze = parse_maze('maze.txt')
    visualize_maze(maze)
