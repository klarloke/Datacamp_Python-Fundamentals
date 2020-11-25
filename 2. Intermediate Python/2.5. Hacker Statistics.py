### 2.5.1. RANDOM NUMBERS

## Random Float
  # Import numpy as np
  import numpy as np

  # Set the seed
  np.random.seed(123)

  # Generate and print random float
  print(np.random.rand())
#-------------------------------------------------#

## Roll Dice 

  # Import numpy and set seed
  import numpy as np
  np.random.seed(123)

  # Use randint() to simulate a dice - randomly chooses an integer {1,2,3,4,5,6}
  print(np.random.randint(1, 7))  

  # Use randint() again
  print(np.random.randint(1, 7))
#-------------------------------------------------#

# Determine you next move

  # Numpy is imported, seed is set

  # Starting step
  step = 50

  # Roll the dice
  dice = np.random.randint(1,7)

  # Finish the control construct
  if dice <= 2 :
      step = step - 1
  elif dice <= 5 :
      step = step + 1
  else:
      step = step + np.random.randint(1,7)

  # Print out dice and step
  print(dice)
  print(step)
#-------------------------------------------------#
