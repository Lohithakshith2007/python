groups = [
    [1, 2, 3, 4],
    [2, 4, 6, 8],
    [1, 3, 5, 7],
    [10, 12, 15]
]

flat=[nums for rows in groups for nums in rows if nums>3]
print(flat)

unq={nums for rows in groups for nums in rows if nums%3==0 and nums%2==0}
print(unq)

elements_count={index:len(elements) for index,elements in enumerate(groups)}
print(elements_count)