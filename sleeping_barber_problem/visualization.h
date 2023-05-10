#ifndef VISUALIZATION_H
#define VISUALIZATION_H

#include <iostream>
#include <vector>
#include <mutex>
#include <cmath>
#include <unistd.h>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>

class BarberShop;

class BarberShopVisualizer {
public:
    BarberShopVisualizer(BarberShop& shop, int numChairs) : shop(shop), numChairs(numChairs) {}

    void update();

    void plot();

private:
    BarberShop& shop;
    int numChairs;
    std::vector<int> barberStatus;
    std::vector<int> queueStatus;
    std::mutex mutex;
};

void BarberShopVisualizer::update() {
    std::unique_lock<std::mutex> lock(mutex);

    barberStatus.push_back(numChairs);
    queueStatus.push_back(numChairs - shop.chairs.size());
    plot();
}

void BarberShopVisualizer::plot() {
    std::vector<double> x(barberStatus.size());
    for (size_t i = 0; i < barberStatus.size(); ++i) {
        x[i] = i;
    }

    cv::Mat plot(numChairs + 1, barberStatus.size(), CV_8UC3, cv::Scalar(255, 255, 255));

    // Plot barber status
    for (size_t i = 1; i < barberStatus.size(); ++i) {
        cv::Point pt1(x[i - 1], numChairs - barberStatus[i - 1]);
        cv::Point pt2(x[i], numChairs - barberStatus[i]);
        cv::line(plot, pt1, pt2, cv::Scalar(255, 0, 0), 1);
    }

    // Plot queue status
    for (size_t i = 1; i < queueStatus.size(); ++i) {
        cv::Point pt1(x[i - 1], numChairs - queueStatus[i - 1]);
        cv::Point pt2(x[i], numChairs - queueStatus[i]);
        cv::line(plot, pt1, pt2, cv::Scalar(0, 0, 255), 1);
    }

    cv::flip(plot, plot, 0);
    cv::imshow("Sleeping Barber Problem", plot);
    cv::waitKey(100);
}

#endif  // VISUALIZATION_H
