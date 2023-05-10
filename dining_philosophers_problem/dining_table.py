from philosopher import Philosopher
import asyncio


class DiningTable:
    def __init__(self, num_philosophers):
        self.num_philosophers = num_philosophers
        self.forks = [asyncio.Lock() for _ in range(num_philosophers)]
        self.philosophers = [
            Philosopher(f"Philosopher {i}", self.forks[i], self.forks[(i + 1) % num_philosophers])
            for i in range(num_philosophers)
        ]

    async def dine(self):
        tasks = [philosopher.dine() for philosopher in self.philosophers]
        await asyncio.gather(*tasks)
