import numpy as np
def f(x, y):
	return 10 * x + y

my_aaray = np.fromfunction(f, (5, 4), dtype = int)
print(my_aaray)

import numpy as np
def f(x, y):
	return 10 * x + y

my_aaray = np.fromfunction(f, (5, 4), dtype = int)

# Slicing the Numpy Arrays:
print(my_aaray[2, 3]) # my_array[2][3]
print(my_aaray[0:5, 1]) # From Row-1 to Row-5, print the 2nd element
print(my_aaray[ : , 1]) # From all rows, print 2nd element
print(my_aaray[1:3, : ]) # From Row-2 to Row-3, print all elements

import numpy as np

import numpy as np
def f(x, y):
	return 10 * x + y

my_array = np.fromfunction(f, (5, 4), dtype = int)

print(f'Before:\n {my_array}')
#my_array[:, [0, -1]] = 0  #For all Rows, set 0 to 1st and last columns
my_array[[0, -1], :] = 0 #For 1st row and last row, set all elements to 0

#After:
print(f'After:\n {my_array}')

import numpy as np

import numpy as np
def f(x, y):
	return 10 * x + y

my_array = np.fromfunction(f, (5, 4), dtype = int)

my_array[[0, 1, -1], :] = 0 #For 1st row and last row, set all elements to 0

#After:
print(f'After:\n {my_array}')

def get_minimum_cost(k, costs):
	costs.sort(reverse=True)
	total_min_cost = 0
	n = len(costs)
	for i in range(n):
		total_min_cost += (i // k + 1) * costs[i]

	return total_min_cost

print( get_minimum_cost(3, [9, 7, 5, 3, 1]))


def get_minimum_coins(amount, denominations):
	denominations.sort(reverse=True)
	number_of_coins = 0
	n = len(denominations)
	i = 0
	while amount > 0:
		number_of_coins += amount // denominations[i]
		amount = amount % denominations[i]
		i += 1
	return number_of_coins

print( get_minimum_coins(88, [1, 2, 5, 20]))

import numpy as np

my_array = np.zeros((8, 8), dtype = int)
#my_array[1::2, ::2] = 8
#Starting from row-index-1 and there after, for all alternatives rows, and for all columns from index 0 and there after alternative columns, replace the cells with value 8
my_array[::2, 1::2] = 1
# Odd indexed-rows Even Indexed-Columns
print(my_array)

import numpy as np

# nan is not a number

print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(np.nan in set([np.nan]))
print(0.3 == 3 * 0.1)

-------------------------------------------------
list1 = [2, 3, 5]

string = ' '.join(map(str, list1)) # convert a list of items of tyep other than str into a string
print(string)
print(type(string))

list2 = ['23', '55', '67']
string = ' '.join(list2) 
print(string)

import numpy as np

#my_matrix = np.array([[0,1],[1,0]])
#print(my_matrix)

chess_board = np.tile( np.array([[1, 0],[0, 1]]), (4,4))
# chess_board = np.tile( np.array([['*', ' '],[' ', '*']]), (4,4))
#print('\n', chess_board)

list1 = []
for array in chess_board:
    list1 = list(array)
    string = ' '.join(map(str, list1))
    print(string)
	
    # Normalize a 5x5 random matrix
import numpy as np

my_array = np.random.random((5,5))
#print(my_array)

values = my_array - np.mean (my_array)
print('\n', values)

values = np.std (my_array)
print('\n', values)

my_array = (my_array - np.mean (my_array)) / (np.std (my_array))
print(my_array)

def read_heights(section):
    m = int(input(f'Enter number of girls of section-{section}: '))
    heights = []
    print(f'Enter {m} heights of girls of Section-{section}: ')
    for i in range(m):
        heights.append(int(input()))
    return heights

list1 = read_heights('A')
list2 = read_heights('B')

list1.sort()
list2.sort()
merged_list = list()

j = 0
i = 0
while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        merged_list.append(list1[i])
        i += 1
    else:
        merged_list.append(list2[j])
        j += 1
merged_list.extend(list1[i:])
merged_list.extend(list2[j:])

print(merged_list)