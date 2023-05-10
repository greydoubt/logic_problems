import asyncio
import random

class BarberShop:
    def __init__(self, num_chairs):
        self.num_chairs = num_chairs
        self.chairs = asyncio.Queue(num_chairs)
        self.barber_sleeping = asyncio.Event()
        self.mutex = asyncio.Lock()

    async def customer(self, name):
        print(f"Customer {name} arrived")
        async with self.mutex:
            if self.chairs.full():
                print(f"No available chairs, customer {name} is leaving")
                return
            await self.chairs.put(name)
            self.barber_sleeping.set()
            print(f"Customer {name} took a seat")

    async def barber(self):
        while True:
            print("Barber is sleeping")
            await self.barber_sleeping.wait()
            self.barber_sleeping.clear()
            async with self.mutex:
                if not self.chairs.empty():
                    customer = await self.chairs.get()
                    print(f"Barber is cutting hair of customer {customer}")
                    await asyncio.sleep(random.uniform(1, 5))
                    print(f"Barber finished cutting hair of customer {customer}")
                else:
                    print("No more customers, barber is going to sleep")
                    break
