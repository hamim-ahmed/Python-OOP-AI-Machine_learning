def merge_sort( start_index, end_index):
    if start_index >= end_index:
        return

    middle = (start_index + end_index) // 2
    # print("start",start_index)
    # print("middle",middle)
    merge_sort( start_index, middle)
    merge_sort( middle + 1, end_index)
    print(start_index,end_index,middle)
    merge( start_index, end_index, middle)

def merge(start_index, end_index, middle):

    start_sublist = lst[start_index:middle + 1]             #first sublist
    end_sublist = lst[middle + 1:end_index + 1]             #2nd sublist

    start_sublist_index = 0       #index count for 1st sublist.
    end_sublist_index = 0         #index count for 2nd sublist
    sorted_index = start_index                              #start_index for main list come from merge_sort >>form which index next sorting will be start.

    while start_sublist_index < len(start_sublist) and end_sublist_index < len(end_sublist):      #while both of the list has element left. >>if element of one sublist finished...break.

        if start_sublist[start_sublist_index] <= end_sublist[end_sublist_index]:   #comparing 2 sublist value..
            lst[sorted_index] = start_sublist[start_sublist_index]              #if first sublist value is smaller then insert it into main list and
            start_sublist_index = start_sublist_index + 1                        #increment 1st sublist index value by 1

        else:
            lst[sorted_index] = end_sublist[end_sublist_index]                  # else 2nd sublist value is smaller, so insert this into main list and
            end_sublist_index = end_sublist_index + 1                            # increment 2nd sublist index value by 1

        sorted_index = sorted_index + 1              #after inserting increment main list index value by one.

    while start_sublist_index < len(start_sublist):              #if start_sublist( 1st sublist) has element remain in it.
        lst[sorted_index] = start_sublist[start_sublist_index]      #insert all the  reamaining element into the main list directley...as they already sorted.
        start_sublist_index = start_sublist_index + 1               #increasing 1st sublist index by one everytime until all elements are over....
        sorted_index = sorted_index + 1                             #increasing the index of the main list every time also.

    while end_sublist_index < len(end_sublist):                  #if end_sublist(2nd sublist) has element remain in it.
        lst[sorted_index] = end_sublist[end_sublist_index]        #insert all the remaining element into the main list from the 2nd sublist.>>alreay sorted.
        end_sublist_index = end_sublist_index + 1
        sorted_index = sorted_index + 1


# lst = [50,3,20,32,1,34,32,11,84,43,23,11,44,76,7]
lst = [6,5,12,10,9,1]
print("Initial list is:",lst)
merge_sort( 0, len(lst)-1)
print("sorted list is:",lst)