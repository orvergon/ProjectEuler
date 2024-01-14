def read_matrix() -> list[list[int]]:
    matrix: list[list[int]] = list()

    while True:
        try:
            line = input()
        except Exception:
            break
        matrix.append([int(x) for x in line.split(" ")])
    return matrix


def get_left_to_right_diagonals(matrix: list[list[int]]) -> list[int]:
    #Left Lateral
    for size, line in enumerate(reversed(range(0, len(matrix)))):
        diagonal: list[int] = [matrix[line][0]]
        count = 1
        _x, _y = 1, line+1
        while count <= size:
            diagonal.append(matrix[_y][_x])
            _x += 1
            _y += 1
            count += 1
        yield diagonal

    #Top
    for column in range(1, len(matrix[0])):
        diagonal: list[int] = [matrix[0][column]]
        _x, _y = column + 1, 1
        while _x < len(matrix[0]) and _y < len(matrix):
            diagonal.append(matrix[_y][_x])
            _x += 1
            _y += 1
        yield diagonal


def get_right_to_left_diagonals(matrix: list[list[int]]) -> list[int]:
    #Top
    for column in range(0, len(matrix[0])-1):
        diagonal: list[int] = [matrix[0][column]]
        _x, _y = column - 1, 1
        while 0 <= _x < len(matrix[0]) and 0 <= _y < len(matrix):
            diagonal.append(matrix[_y][_x])
            _x -= 1
            _y += 1
        yield diagonal

    #Lateral
    for line, size in enumerate(reversed(range(0, len(matrix)))):
        diagonal: list[int] = [matrix[line][len(matrix)-1]]
        count = 1
        _x, _y = (len(matrix) - 2), line+1
        while count <= size:
            diagonal.append(matrix[_y][_x])
            _x -= 1
            _y += 1
            count += 1
        yield diagonal


def get_columns(matrix: list[list[int]]) -> list[int]:
    for x in range(len(matrix[0])):
        column: list[int] = list()
        for y in range(len(matrix)):
            column.append(matrix[y][x])
        yield column


def get_lines(matrix: list[list[int]]) -> list[int]:
    for x in matrix:
        yield x


def get_lists(matrix: list[list[int]]) -> list[int]:
    for x in get_lines(matrix):
        yield x
    for x in get_columns(matrix):
        yield x
    for x in get_right_to_left_diagonals(matrix):
        yield x
    for x in get_left_to_right_diagonals(matrix):
        yield x


def mult(l: list[int]) -> int:
    m = 1
    for x in l:
        m = m * x
    return m


def get_small_list(matrix: list[list[int]], size:int = 4) -> list[int]:
    max:int = 0
    lists: list[list[int]] = list(get_lists(matrix))
    for big_list in lists:
        if len(big_list) <= size:
            continue
        else:
            _begin, _end = 0, 4
            while _end <= len(big_list):
                small_list = big_list[_begin:_end]
                new_max = mult(small_list)
                if new_max > max:
                    max = new_max
                    print(big_list[_begin:_end])
                _begin += 1
                _end += 1
    print(max)

matrix = read_matrix()

get_small_list(matrix)
