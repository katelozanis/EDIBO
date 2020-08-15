Dnum = 100

print("Given decimal : " + str(Dnum))

# Decimal to binary number conversion
binnum = [int(i) for i in list('{0:0b}'.format(Dnum))]

# Printing result
print("Converted binary list is : ",binnum)
