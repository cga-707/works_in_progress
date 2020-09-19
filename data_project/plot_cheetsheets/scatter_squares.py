import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.gist_rainbow, s=10)

# Set chart title and axis
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Number", fontsize=14)
ax.set_ylabel("Number Squared", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# Set range for each axis
ax.axis([0, 1100, 0, 1100000])

# Saves the plot. The first argument is the assigns the filename.
# The second gets rid of extra white space
plt.savefig('squares_plot.png', bbox_inches='tight')