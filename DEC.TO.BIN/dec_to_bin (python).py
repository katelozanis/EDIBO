Dnum = 100

print("Given decimal : " + str(Dnum))



binnum = [int(i) for i in list('{0:0b}'.format(Dnum))]


print("Converted binary list is : ",binnum)
