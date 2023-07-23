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
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers,
               cmap=plt.cm.Blues, edgecolor='none', s=1)

    # Выделение первой и последней точек
    ax.scatter(0, 0, c="green", edgecolor='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

    #Удаление осей. переводят флаг видимости каждой оси в состояние False
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n):")
    if keep_running == "n":
        break