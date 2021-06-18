'''
  If name is less than 3 characters long- name must be at least 3 characters
  otherwise if it's more than 50 characters - name must be maximum of 50 characters
  otherwise - name looks good!
'''


name = str(input("Enter your name:"))
short_name = name<3
if short_name:
    print(f"name must be atleast 3 characters long")


