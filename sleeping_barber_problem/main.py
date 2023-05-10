import asyncio
import random
from visualization import BarberShopVisualizer
from barber_shop import BarberShop

async def main():
    num_chairs = 3
    shop = BarberShop(num_chairs)
    visualizer = BarberShopVisualizer(shop, num_chairs)

    tasks = []
    for i in range(10):
        tasks.append(asyncio.create_task(shop.customer(i)))
        tasks.append(asyncio.create_task(visualizer.update()))

    tasks.append(asyncio.create_task(shop.barber()))
    tasks.append(asyncio.create_task(visualizer.update()))

    await asyncio.gather(*tasks)

asyncio.run(main())
