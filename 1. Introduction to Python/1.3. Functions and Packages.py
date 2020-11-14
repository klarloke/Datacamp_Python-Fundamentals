### HELP! FUNCTION

  # complex() --> complex(real[, imag]) 
    # This is equivalent to (real + imag*1j) where imag defaults to 0.
    # Create a complex number from a real part and an optional imaginary part.
  
  
### MULTIPLE ARGUMENTS

  # Create lists first and second
  first = [11.25, 18.0, 20.0]
  second = [10.75, 9.50]

  # Paste together first and second: full
  full = first + second

  # Sort full in descending order: full_sorted
  full_sorted = sorted(full, reverse = True)

  # Print out full_sorted
  print(full_sorted)
  

### STRING METHODS

  # string to experiment with: place
  place = "poolhouse"

  # Use upper() on place: place_up --> Converts string to all upper case
  place_up = place.upper() 

  # Print out place and place_up
  print(place)
  print(place_up)

  # Print out the number of o's in place
  print(place.count('o'))
  

### LIST METHODS (1)

  # Create list areas
  areas = [11.25, 18.0, 20.0, 10.75, 9.50]

  # Print out the index of the element 20.0
  print(areas.index(20.0))

  # Print out how often 9.50 appears in areas
  print(areas.count(9.50))
  
  # Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]


### LIST METHODS (2)

  # Use append twice to add poolhouse and garage size
  areas.append(24.5)
  areas.append(15.45)

  # Print out areas
  print(areas)

  # Reverse the orders of the elements in areas
  areas.reverse()

  # Print out areas
  print(areas)
  

##### PACKAGES

### IMPORT PACKAGE (i.e. package: math --> to access pi)

  # Definition of radius
  r = 0.43

  # Import the math package
  import math

  # Calculate C
  C = 2*math.pi*r

  # Calculate A
  A = math.pi*(r**2)

  # Build printout
  print("Circumference: " + str(C))
  print("Area: " + str(A))
  
 ### SELECTIVE IMPORT
 
  # Definition of radius
  r = 192500

  # Import radians function of math package
  from math import radians

  # Travel distance of Moon over 12 degrees. Store in dist.
  phi = radians(12)
    # --> converts degrees to radians
  dist = r * phi

  # Print out dist
  print(dist)

  ### DIFFERENT WAYS OF IMPORTING
  
  from scipy.linalg import inv as my_inv
    # to access inv() function from linear algebra --> renamed as "my_inv"
