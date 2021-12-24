def multiplicate(A):
    left = [
        1,
    ]
    for elem in A[:-1]:
        left.append(left[-1] * elem)

    right = [
        1,
    ]
    for elem in A[::-1][:-1]:
        right.append(right[-1] * elem)
    right = right[::-1]

    return [left_elem * right_elem for left_elem, right_elem in zip(left, right)]
