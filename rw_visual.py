import matplotlib.pyplot as plt
from random_walk import RandomWalk

""" Новые блуждания строятся до ттех пор, пока программма остаетсяяя активной"""
# Построение случайного блуждания
while True:
    rw = RandomWalk()
    rw.fill_walk()

    # Нанесение точек на диаграмму
    plt.style.use("classic")
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n):")
    if keep_running == "n":
        break