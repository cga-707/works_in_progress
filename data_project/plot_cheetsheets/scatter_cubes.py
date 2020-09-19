import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots()

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
ax.set_title("Cubed Numbers", fontsize=24)
ax.set_ylabel("Number Cubed", fontsize=14)
ax.set_xlabel("Number", fontsize=14)

ax.axis([0, 5100, None, None])

plt.show()