'''
Task -----------------condition------------------------------
Weight converter:
  Input the weight of a person in either kg or lbs. If the person provides his/her
  weight in kg then convert it into lbs
  else convert it to kg.
'''
weight = float(input("Enter your weight:"))
weight_given = input("lbs or kg:")

if weight_given == kg:
    convert_lbs = (weight*2.20)
    print(f"Your weight in lbs is {convert_lbs}")
else:
    convert_kg = (weight/2.20)
    print(f"Your weight in kg is {convert_kg}")
