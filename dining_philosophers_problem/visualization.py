import asyncio
import numpy as np
import matplotlib.pyplot as plt


class DiningVisualizer:
    def __init__(self, dining_table):
        self.dining_table = dining_table
        self.num_philosophers = dining_table.num_philosophers
        self.fork_states = np.zeros(self.num_philosophers)
        self.philosopher_states = np.zeros(self.num_philosophers)
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim([0, self.num_philosophers])
        self.ax.set_ylim([0, 2])
        self.ax.set_xticks(np.arange(0.5, self.num_philosophers, 1))
        self.ax.set_xticklabels([f"Philosopher {i}" for i in range(self.num_philosophers)])
        self.ax.set_yticks([])
        self.ax.set_title("Dining Philosophers")
        self.ax.set_aspect("equal")
        self.fork_lines = []
        self.philosopher_dots = []

        fork_colors = ["#22212C", "#454158", "#9580FF", "#22212C", "#454158"]
        philosopher_colors = ["#FFFFFF", "#8AFF80", "#FF5555"]

        for i in range(self.num_philosophers):
            fork_line, = self.ax.plot([i, i], [0, 1], color=fork_colors[i % len(fork_colors)], linewidth=2)
            philosopher_dot, = self.ax.plot([i], [1.2], ".", markersize=12, color=philosopher_colors[i % len(philosopher_colors)])
            self.fork_lines.append(fork_line)
            self.philosopher_dots.append(philosopher_dot)

        self.fig.canvas.draw()

    def update(self):
        for i, fork in enumerate(self.dining_table.forks):
            if fork.locked():
                self.fork_states[i] = 1
            else:
                self.fork_states[i] = 0

        for i, philosopher in enumerate(self.dining_table.philosophers):
            if philosopher.left_fork.locked() and philosopher.right_fork.locked():
                self.philosopher_states[i] = 1
            else:
                self.philosopher_states[i] = 0

        for i, line in enumerate(self.fork_lines):
            line.set_ydata([self.fork_states[i], self.fork_states[i] + 1])

        for i, dot in enumerate(self.philosopher_dots):
            dot.set_xdata([i])
            dot.set_ydata([self.philosopher_states[i] + 1.2])

        self.fig.canvas.draw()

    def visualize(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self.dining_table.dine())
        loop.create_task(self.update_loop())
        plt.show()

    async def update_loop(self):
        while True:
            await asyncio.sleep(0.1)
            self.update()
