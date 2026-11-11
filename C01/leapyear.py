 
current_yr = int(input("Enter current year (yyyy): ")) 
final_yr = int(input("Enter final year (yyyy): ")) 
print("Future leap years from", current_yr, "-", final_yr) 
if current_yr <= final_yr: 
  for i in range(current_yr, final_yr + 1): 
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0): 