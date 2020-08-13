Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruit='banana'
>>> letter= fruit[1]
>>> fruit[0]+fruit[3]
'ba'
>>> fruit[1]+fruit[3]+fruit[5]
'aaa'
>>> N= len(fruit)
>>> N
6
>>> fruit[N-1]
'a'
>>> numbers= []
>>> len(numbers)
0
>>> numbers
[]
>>> numbers.append(55)
>>> len(numbers)
1
>>> numbers
[55]
>>> numbers.append(1)
>>> numbers
[55, 1]
>>> vaardi =['a','ab','abc']
>>> vaardi
['a', 'ab', 'abc']
>>> vaardu_garumi= []
>>> vardvaardu_garumi.append(len(vaardi[0]))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    vardvaardu_garumi.append(len(vaardi[0]))
NameError: name 'vardvaardu_garumi' is not defined
>>> typpe(vaardi)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    typpe(vaardi)
NameError: name 'typpe' is not defined
>>> type(vaardu_garumi)
<class 'list'>
>>> vaardi=['a','ab','abc']
>>> fruit
'banana'
>>> len(fruit)
6
>>> fruit[0]
'b'
>>> N= len(fruit)
>>> n
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    n
NameError: name 'n' is not defined
>>> N
6
>>> fruit[N-1]
'a'
>>> N
6
>>> fruit[len(fruit)-1]
'a'
>>> fruit= 'abcdef'
>>> fruit
'abcdef'
>>> len(fruit)
6
>>> fruit[len(fruit)-1]
'f'
>>> fruit='banana'
>>> letter=fruit[1]
>>> letter= fruit[0]
>>> print(letter)
b
>>> letter= fruit[1.5]
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    letter= fruit[1.5]
TypeError: string indices must be integers
>>> fruit='banan'
>>> len(fruit)
5
>>> lenght= len(fruit)
>>> last= fruit(length)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    last= fruit(length)
NameError: name 'length' is not defined
>>> last = fruit(length-1)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    last = fruit(length-1)
NameError: name 'length' is not defined
>>> print(last)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print(last)
NameError: name 'last' is not defined
>>> index= 0
>>> while index < len(fruit):
	letter =fruit[index]
	print(letter)
	index= index +1

	
b
a
n
a
n
>>> s = 'Monty
