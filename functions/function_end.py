items3 = ["Mic", "Phone", 323.12, 3123.123, "Justin", "Bag", "Cliff Bars", 134]

def my_sum_and_count(my_num_list):
    total = 0
    count = 0

    for i in my_num_list:
        if isinstance(i, float) or isinstance(i, int):
            total += i
            count +=1
    return total, count

print('Input List:' ,items3)
print('Total Numbers Sum:',my_sum_and_count(items3)[0])
print('Total Numbers Count:',my_sum_and_count(items3)[1])

def my_avg(my_num_list):
    the_sum, num_of_items = my_sum_and_count(my_num_list)
    return the_sum  / (num_of_items * 1.0)

print('Average of Numbers: ', my_avg(items3))