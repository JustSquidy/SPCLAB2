
list = [2,4,6]

new_list = [ num + 1 for num in list ]
print(new_list) # adds 1 to each number in the list

zero_list = [0, 3, 4 ,0 , 22, 1]

no_zero_list = [ num for num in zero_list if num != 0 ]
print(no_zero_list) # removes all the 0s from the list

class_list = ['ITEC 2560', 'BTEC 1010', 'ITEC 2905']

itec_list = [ course for course in class_list if course.startswith('ITEC') ]
print(itec_list) # only displays the courses that start with ITEC

double_list = [0, 10, 4, 0,32]

no_zero_double_list = [ num*2 for num in double_list if num != 0 ]
print(no_zero_double_list) # removes 0s and doubles the remaining numbers