import matplotlib.pyplot as plt

x_values = range(1, 5001) # generating a range of cubes
y_values = [x**3 for x in x_values]


plt.style.use('seaborn-v0_8-deep') # apply a built-in style
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues) # determine how the plot is generated, and add stles with scatter() method  #type: ignore

# Set the labes of title, x and y coodinate
ax.set_title("First 5 Cubes", fontsize=20) 
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Cubes", fontsize=14)

ax.tick_params(axis='both',  which='major', labelsize=14) # Set the tickness of the plot


plt.show() # Display plot

# plt.savefig('images/cubes.png', bbox_inches='tight')
