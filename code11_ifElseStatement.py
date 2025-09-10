Total_subjects=int(input("how many subjects??="))
how=int(input("how many marks is a subject worth="))
total=0
for i in range(1,Total_subjects+1):
  marks=float(input(f"subject {i} marks="))
  total+=marks
print("your total marks=",total)
presantage=total/Total_subjects/how*100
print(" your percantage=",presantage)

