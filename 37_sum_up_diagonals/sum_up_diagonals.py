def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    operations = len(matrix)
    start = 0
    end = -1
    idx = 0
    sum = 0
    while (idx < operations):
        sum += matrix[idx][start]
        sum += matrix[idx][end]
        idx += 1
        start += 1
        end -= 1

    return sum