from dining_table import DiningTable
from visualization import DiningVisualizer


def main():
    num_philosophers = 5
    dining_table = DiningTable(num_philosophers)
    visualizer = DiningVisualizer(dining_table)
    visualizer.visualize()


if __name__ == "__main__":
    main()