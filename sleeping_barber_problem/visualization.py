import asyncio
import matplotlib.pyplot as plt

class BarberShopVisualizer:
    def __init__(self, shop, num_chairs):
        self.shop = shop
        self.num_chairs = num_chairs
        self.barber_status = []
        self.queue_status = []

    async def update(self):
        self.barber_status.append(self.num_chairs)
        self.queue_status.append(self.num_chairs - self.shop.chairs.qsize())
        self.plot()

    def plot(self):
        plt.plot(self.barber_status, label='Barber')
        plt.plot(self.queue_status, label='Queue')
        plt.xlabel('Time')
        plt.ylabel('Number of Customers')
        plt.title('Sleeping Barber Problem')
        plt.legend()
        plt.grid(True)
        plt.show(block=False)
        plt.pause(0.1)
