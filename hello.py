from functools import reduce

################
# --- LOOPS and List Methods ---#
################
# 1. Divisible By Ten

def div_by_ten(nums):
    counter = 0
    for num in nums:
        if num % 10:
            pass
        else:
            counter += 1
    return counter
    
nums = [20, 30, 55]

print(div_by_ten(nums))

# 2. take a list of names and prepend the string 'Hello, ' before each name.

def add_greetings(names):
    names_with_greetings = []
    for name in names:
        names_with_greetings.append(f"Hello, {name}")
    return names_with_greetings

print(add_greetings(["Owen", "Max", "Sophie"]))

# 3. Delete Starting Even Numbers

""" def delete_starting_evens(lst):
    new_lst = []
    for num in lst:
        
        if len(lst) == 0:
            return "The list is empty"  
        
        elif num % 2 == 0: 
            new_lst.append(num)
            
        else:
            break
    
    for num in new_lst:
        lst.remove(num)

    return lst """



# 3. Better solution

def delete_starting_evens(lst):
    while(len(lst) > 0 and lst[0] % 2 == 0):
        lst = lst[1:] # removes the first element
    return lst

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))

# 4. The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list.

""" def odd_indices(lst):
    odd_indices_values = []
    for i, num in enumerate(lst):
        if i % 2 == 0:
            continue
        else:
            odd_indices_values.append(num)

    return odd_indices_values
 """


# 4. Better solution

def odd_indices(lst):
    new_lst = []
    for index in range(1, len(lst), 2):
        new_lst.append(lst[index])
    return new_lst

print(odd_indices([4, 3, 7, 10, 11, -2]))

# 5  raise a list of numbers to the power of a list of other numbers

def exponents(bases, powers):
    new_lst = []
    for num in bases:
        for power in powers:
            new_lst.append(num ** power)
    return new_lst

print(exponents([2, 3, 4], [1, 2, 3]))
# 6  return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.

def larger_sum(lst1, lst2):
    result_lst1 = reduce((lambda x, y: x + y), lst1)
    result_lst2 = reduce((lambda x, y: x + y), lst2)
    if result_lst1 >= result_lst2:
        return lst1
    else:
        return lst2

print(larger_sum([1,2,3], [1,2,2, 1, 2]))

# 6 Better solution using sum() and ternary operator
def larger_sum2(lst1, lst2):
    return lst1 if sum(lst1) >= sum(lst2) else lst2

print(larger_sum2([1,2,3], [1,2,2, 1, 2]))


# 7 A function that returns a sum of a list as soon as it is bigger than 9k. Should return the last sum.

def over_nine_thousand(lst):
    lst_total = 0
    for num in lst:
        lst_total += num
        if lst_total > 9000:
            break
    return lst_total 

print(over_nine_thousand([8000, 900, 120, 5000]))

# 8 function that finds the max number in a list, without using max() built-in method

def max_num(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

# 9 Find the indices in two equally sized lists where the numbers match

def same_values(lst1, lst2):
    index_match_lst = []
    for i, n in enumerate(lst1):
            if n == lst2[i]:
                index_match_lst.append(i)
    return index_match_lst

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))


# 10 Compare if lst1 is equal to lst2 reversed.

def reversed_list(lst1, lst2):
    lst2.reverse()
    if lst1 == lst2:
        return True
    else:
        return False


#OR

def reversed_list(lst1, lst2):
    if lst1 == lst2[::-1]: # <- it reverts the lst2 -> it is a type of slicing
        return True
    else:
        return False

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))



#######################
# --- Control Flow ---#
#######################

# 1. Create a method that tests whether the result of taking the power of one number to another number provides an answer which is greater than 5000

def large_power(base, exponent):
    return True if base ** exponent > 5000 else False

print(large_power(2, 13))

# 2. function will accept a parameter called budget which describes our spending limit. The next four parameters describe what we are spending our money on. We need to sum all of our spendings and compare it to the budget.

def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    return True if budget < sum([food_bill, electricity_bill, internet_bill, rent]) else False

print(over_budget(100, 20, 30, 10, 40))
print(over_budget(80, 20, 30, 10, 30))

# 3 determine if one number is twice as large as another number. 

def twice_as_large(num1, num2):
    return True if num1 > num2 * 2 else False

print(twice_as_large(10, 5))
print(twice_as_large(11, 5))

# 4. Divisible By Ten

def divisible_by_ten(num):
    return True if num % 10 == 0 else False
    
# 5 check if the sum of two inputs does not equal ten.

def not_sum_to_ten(num1, num2):
    return True if num1 + num2 != 10 else False

# 6. test if a number falls within a certain range. 

def in_range(num, lower, upper):
    return True if num in range(lower, (upper + 1)) else False

print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False

#7. write a program that checks different names and determines if they are equal. 

def same_name(your_name, my_name):
    return True if your_name == my_name else False

print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False

#8. create an example of a function that contains a contradiction.

def always_false(num):
    if num < 10 and num > 10:
        return True
    elif num > 10 and num < 10:
        return True
    else:
        return False
    
print(always_false(0))

# 9 create a function that will help us rate movies. Our function will split the ratings into different ranges and tell the user how the movie was based on the movie’s rating

def movie_review(rating):
    if rating <= 5:
        return "Avoid at all costs!"
    elif rating < 9:
        return "This one was fun."
    elif rating < 10:
        return "Outstanding!"
    
print(movie_review(9))

# 10 select which number from three input values is the greatest using conditional statements

def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    else:
        return "It's a tie!"

print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, 5))


####################
# --- Functions ---#
####################

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))