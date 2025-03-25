def binary_search(list, item):
    low = 0;
    high = len(list) - 1;
    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > mid:
            high =  mid - 1
        else:
            low = mid + 1
    return None;

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9];
print(binary_search(my_list, 5));
print(binary_search(my_list, 11));

# binary search returns the position of the item being searched for
# binary search returns None if the item is not there in the list
# The list has to be sorted for binary search to be performed


