import matplotlib.pyplot as plt


# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]
plt.style.use("seaborn-v0_8")    # Нанеесение на диаграмму отдельной точки используется функция scatter()
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.cool, s=10)

# Назначение заголовка диаграммы и меток осей.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Назначение размера шрифта делений на осях.
ax.tick_params(axis='both', which='major', labelsize=14)

# Назначение диапазона для каждой оси
ax.axis([0, 5050, 0, max(y_values)])
plt.show()
# plt.savefig()   #Для автоматического сохранения в файл набрать этот код, вместо plt.show()
# plt.savefig('squares_plot.png', bbox_inches='tight')
# Первый аргумент содержит имя файла для сохранения диаграммы;
# Второй аргумент отсекает от диаграммы лишнее пространство.