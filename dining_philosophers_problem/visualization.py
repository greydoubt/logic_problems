import asyncio
import numpy as np
import matplotlib.pyplot as plt


class DiningVisualizer:
    def __init__(self, dining_table):
        self.dining_table = dining_table
        self.num_philosophers = dining_table.num_philosophers
        self.states = np.zeros(self.num_philosophers)
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim([0, self.num_philosophers])
        self.ax.set_ylim([0, 2])
        self.ax.set_xticks(np.arange(0.5, self.num_philosophers, 1))
        self.ax.set_xticklabels([f"Philosopher {i}" for i in range
        self.num_philosophers])
        self.ax.set_yticks([])
        self.ax.set_title("Dining Philosophers")
        self.ax.set_aspect("equal")
        self.line, = self.ax.plot(range(self.num_philosophers), self.states, "ro")
        self.fig.canvas.draw()
    
    def update(self):
        self.states = np.zeros(self.num_philosophers)
        for i, philosopher in enumerate(self.dining_table.philosophers):
            if philosopher.left_fork.locked() and philosopher.right_fork.locked():
                self.states[i] = 1
        self.line.set_ydata(self.states)
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
