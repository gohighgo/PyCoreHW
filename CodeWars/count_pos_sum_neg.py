def count_positives_sum_negatives(arr):
    count=0
    sum=0
    for elem in arr:
        if elem<0:
            sum+=elem
        elif elem>0:
            count+=1
    my_arr=[count, sum]
    if not arr:
        return arr
    return my_arr
