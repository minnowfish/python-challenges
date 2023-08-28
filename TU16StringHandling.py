#Exercise 1:  Create a float variable for Ringgit and print it as "RM129"
ringgit = 129.00
print(f"RM{ringgit:.0f}\n")

#Exercise 2: Create a table of numbers with headings
print("Table of Random Numbers:")
numcol1 = [1.0426, 7.39103, 26.710672]
numcol2 = [9.00192928171, 4.291707,0.3861]
numcol3 = [2.329909, 2.087, 49.2018]

for i in range(3):
    print(f"{numcol1[i]:^15.2f} {numcol2[i]:^15.2f} {numcol3[i]:^15.2f} \n" )

#Exercise 3: Create a quick binary convertor
number = int(input("Input the number to convert to binary"))
print(f"Binary: {number:b}")
