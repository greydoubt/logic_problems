#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>
#include "barber_shop.h"
#include "visualization.h"

int main() {
    int numChairs = 3;
    BarberShop shop(numChairs);
    BarberShopVisualizer visualizer(shop, numChairs);

    std::vector<std::thread> threads;

    for (int i = 0; i < 10; ++i) {
        threads.emplace_back([&]() {
            shop.customer(i);
            visualizer.update();
        });
    }

    threads.emplace_back([&]() {
        shop.barber();
        visualizer.update();
    });

    for (auto& thread : threads) {
        thread.join();
    }

    return 0;
}
