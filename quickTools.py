
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

def count_n_in_list(lst,n,max):
    counter = 0
    for num in lst:
        if num == n:
            counter+=1
    if counter>= max:
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



# I left off at advanced lists review #5, this is about half way done with the review.
#is it even/odd function up to (pick a number for now that you can figure out on your own)

