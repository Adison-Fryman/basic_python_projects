#finding the maximum number in a list, or string

def find_max (nums):
    max_num = nums[0]
    for num in nums:
     if num> max_num:
        max_num = num
    return(max_num)


def power_5000(base,exponent):
    result = base**exponent
    if result>= 5000:
        return True
    else:
        return False

# sums all items in a list or string if single digit integers
def sum(nums):
    sum = 0
    for num in nums:
        sum += int(num)
    return sum

# better for here would be a summation of values in a dictionary


def over_budget(budget,rent,food,util,fun):
    total = rent+fun+fun+util
    result = budget-total
    if result>=0:
        print(f'you are under budget by ${result}.')
    else:
        print(f'Your budget is bellow zero at {result} dollars, you spent too much money!')

def did_it_double(num1,num2):
    result= num2/num1
    if result>=2:
        return True
    else:
        return False
def divisible_by_10(num):
    result=num%10
    if result==0:
        return True
    else:
        return False

def not_equal_10(num1,num2):
    result= num2+num1
    if result != 10:
        return True
    else:
        return False

def in_range(num,lowwer,upper):
    if num>=lowwer and num<=upper:
        print('True')
        return True
    else:
        print("False")
        return False

def low_med_high(total_possible, num):
    if num<=(.3333*total_possible):

        return "low"
    elif num<= .6666*total_possible:
        return "Medium"
    elif num<= total_possible:
        return "High"
    else:
        return "Error-Out of Range"

def add_lenth_to_end(num_list):
   num_list.append(len(num_list))
   return num_list

def add_sum_to_end(num_list):
    num_list.append(sum(num_list))
    return num_list

def larger_list(list1,list2):
    if len(list1)>len(list2):
        return 'First list is larger'
    else:
        return 'Second list is larger'

def count_n_in_list(lst,n,needed_amount):
    counter = 0
    for num in lst:
        if num == n:
            counter+=1
    if counter>= needed_amount:
        print(f'you have enough of "{n}"')
    else:
        print(f'You do not have enough of "{n}"')
    return counter

def more_in_list(lst,a,b):
    if lst.count(a)>=lst.count(b):
        return f" You have more {a}'s than {b}'s"
    else:
        return f" You have more {b}'s than {a}'s"

print(more_in_list([1,2,1,3,4,5,1,2,3,1,2,2,2,2,2],1,2))


def combine_and_sort(list1,list2):
    newlist=list1+list2
    newlist.sort()
    print(newlist)


def count_by_n(min,max,n):
    newlist=[x for x in range(min,max,n)]
    return newlist

# remove a section of a list
def remove_section(lst, start, end):
  return lst[:start] + lst[end+1:]

# I left off at advanced loops

# dictionaries
def above_n_count(my_dictionary, number):
  count = 0
  for value in my_dictionary.values():
    if value > number:
      count += 1
  return count

def sum_values(my_dictionary):
  sum=0
  for value in my_dictionary.values():
    sum+=value
  return sum

# defining specific keys and accessing their values
def sum_even_keys(dict1):
  sum=0
  for key,value in dict1.items():
    if key % 2==0:
      sum+= dict1[key]
  return sum

#creating a new dictionary from an excisting one
# with changes to the values
def add_ten(dic1):
  dic2 = {}
  for key,value in dic1.items():
    dic2[key]=value+10
  return dic2

# finding a key in a dictionary***
def find_key_x(dic1,x):
    a=[]
    if x in dic1:
        a.append(x)
    return a

#finding max value in a dictionary and returning corresponding key
def max_val_finder(dic1):
    max_val = float("-inf")
    max_key = float("-inf")
    for key,value in dic1.items():
        if value>max_val:
            max_val=value
            max_key=key
    return max_key


#using **args with a dictionary

#using **kwargs with a dictionary

def print_data(positional_arg, **data):
    print(positional_arg)
    for arg in data.values():
        print(arg)


#print_data('position 1', a='arg1', b=True, c=100)

def add_data(name, **data):
    print(name)
    for key,value in data.items():
        print(key,value)


add_data('Adison', Children=2, maried =True, age=37)

#print(max_val_finder({1:100, 2:1000, 3:4, 4:10}))
#dic1={1:2,3:4,4:5}
#print(find_key_x(dic1,4))




#unpacking

x,y,z=1,2,3
print(x)