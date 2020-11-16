### 2.1.1. BASIC PLOTS WITH MATPLOTLIB

## LINE PLOT

  # Print the last item from year and pop
  print(year[-1])
  print(pop[-1])

  # Import matplotlib.pyplot as plt
  import matplotlib.pyplot as plt

  # Make a line plot: year on the x-axis, pop on the y-axis
  plt.plot(year, pop)

  # Display the plot with plt.show()
  plt.show()

## SCATTER PLOT

  # Change the line plot below to a scatter plot
  plt.scatter(gdp_cap, life_exp)

  # Put the x-axis on a logarithmic scale
  plt.xscale('log')

  # Show plot
  plt.show()
#-------------------------------------------------------------------------------------------------#

### 2.1.2. HISTOGRAM
