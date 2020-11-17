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

  # Create histogram of life_exp data
    # Default: 10 bins
  plt.hist(life_exp, bins=5)

  # Display histogram
  plt.show()
  
  # Clean up plot
  plt.clf()

## CUSTOMIZATION

  # Basic scatter plot, log scale
  plt.scatter(gdp_cap, life_exp)
  plt.xscale('log') 

  # Strings
  xlab = 'GDP per Capita [in USD]'
  ylab = 'Life Expectancy [in years]'
  title = 'World Development in 2007'

  # Add axis labels
  plt.xlabel(xlab)
  plt.ylabel(ylab)

  # Add title
  plt.title(title)

  # After customizing, display the plot
  plt.show()
  
  #------------------------------------------#
  
  # Scatter plot
  plt.scatter(gdp_cap, life_exp)

  # Previous customizations
  plt.xscale('log') 
  plt.xlabel('GDP per Capita [in USD]')
  plt.ylabel('Life Expectancy [in years]')
  plt.title('World Development in 2007')

  # Definition of tick_val and tick_lab
  tick_val = [1000, 10000, 100000]
  tick_lab = ['1k', '10k', '100k']

  # Adapt the ticks on the x-axis
  plt.xticks(tick_val, tick_lab)

  # After customizing, display the plot
  plt.show()
  
  #------------------------------------------#
  
  # Import numpy as np
  import numpy as np

  # Store pop as a numpy array: np_pop
  np_pop = np.array(pop)

  # Double np_pop
  np_pop = np_pop * 2

  # Update: set s argument to np_pop
  plt.scatter(gdp_cap, life_exp, s = np_pop)  # size s corresponds to population size (re: bubble)

  # Previous customizations
  plt.xscale('log') 
  plt.xlabel('GDP per Capita [in USD]')
  plt.ylabel('Life Expectancy [in years]')
  plt.title('World Development in 2007')
  plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

  # Display the plot
  plt.show()
  
  #------------------------------------------#
  # Specify c and alpha inside plt.scatter()
  plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)  #alpha: opacity, c: colour (developed via a dictionary)

  # Previous customizations
  plt.xscale('log') 
  plt.xlabel('GDP per Capita [in USD]')
  plt.ylabel('Life Expectancy [in years]')
  plt.title('World Development in 2007')
  plt.xticks([1000,10000,100000], ['1k','10k','100k'])

  # Additional customizations
  plt.text(1550, 71, 'India')
  plt.text(5700, 80, 'China')

  # Add grid() call
  plt.grid(True)
  
  # Show the plot
  plt.show()
#-------------------------------------------------------------------------------------------------#

  
