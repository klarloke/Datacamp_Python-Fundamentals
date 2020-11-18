### 2.2.1 MOTIVATION FOR DICTIONARIES

  # Definition of countries and capital
  countries = ['spain', 'france', 'germany', 'norway']
  capitals = ['madrid', 'paris', 'berlin', 'oslo']

  # Get index of 'germany': ind_ger
  ind_ger = countries.index('germany')

  # Use ind_ger to print out capital of Germany
  print(capitals[ind_ger])
#----------------------------------------------------------------#

### 2.2.2. CREATE DICTIONARY

  #Create dictionary
  # Definition of countries and capital
  countries = ['spain', 'france', 'germany', 'norway']
  capitals = ['madrid', 'paris', 'berlin', 'oslo']

  # From string in countries and capitals, create dictionary europe
  europe = { "spain": "madrid","france":"paris","germany":"berlin","norway":"oslo"}

  # Print europe
  print(europe)
  
### ACCESS DICTIONARY
  
  # Definition of dictionary
  europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

  # Print out the keys in europe
  print(europe.keys())  # ----> dict_keys(['spain', 'germany', 'norway', 'france'])

  # Print out value that belongs to key 'norway'
  print(europe['norway'])
