import asyncio
import random


class Philosopher:
    def __init__(self, name, left_fork, right_fork):
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork

    async def think(self):
        print(f"{self.name} is thinking.")
        await asyncio.sleep(random.uniform(1, 3))

    async def eat(self):
        print(f"{self.name} is hungry and trying to pick up forks.")

        async with self.left_fork, self.right_fork:
            print(f"{self.name} picked up both forks and started eating.")
            await asyncio.sleep(random.uniform(2, 5))

        print(f"{self.name} finished eating and put down both forks.")

    async def dine(self):
        while True:
            await self.think()
            await self.eat()
