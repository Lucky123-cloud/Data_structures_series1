def remove_dups(lst):
    new_lst = set(lst)
    return list(new_lst)


if __name__ == "__main__":
    sample_list = [1, 2, 2, 3, 4, 4, 5]
    print(f"Original list: {sample_list}")
    print(f"List after removing duplicates: {remove_dups(sample_list)}")


# lets do it algorithmically without using set
def remove_dups_algorithmic(lst):
    new_lst = []
    for item in lst:
        if item not in new_lst:
            new_lst.append(item)
    return new_lst


if __name__ == "__main__":
    sample_list = [1, 2, 2, 3, 4, 4, 5]
    print(f"Original list: {sample_list}")
    print(f"List after removing duplicates (algorithmic): {remove_dups_algorithmic(sample_list)}")


# do it with a dictionary
def remove_dups_dict(lst):
    new_dict = {}
    for item in lst:
        new_dict[item] = True
    return list(new_dict.keys())


if __name__ == "__main__":
    sample_list = [1, 2, 2, 3, 4, 4, 5]
    print(f"Original list: {sample_list}")
    print(f"List after removing duplicates (using dict): {remove_dups_dict(sample_list)}")


# lets find the duplicates in a list
def find_duplicates(nums):
    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)


if __name__ == "__main__":
    sample_list = [1, 2, 2, 3, 4, 4, 5]
    print(f"Original list: {sample_list}")
    print(f"Duplicates in the list: {find_duplicates(sample_list)}")