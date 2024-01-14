from pprint import PrettyPrinter
pp = PrettyPrinter(indent=4).pprint

class Path:
    line = None,
    index = None,
    value = None,
    numbers = []
    def __init__(self, line, index, value, numbers) -> None:
        self.line = line
        self.index = index
        self.value = value
        self.numbers = numbers
    def __repr__(self) -> str:
        return str(self.__dict__)

triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

numbers = list(map(lambda x: list(map(lambda y: int(y), x)), [line.split(" ") for line in triangle.splitlines()]))
antinumbers = list(map(lambda x: list(map(lambda y: 100-int(y), x)), [line.split(" ") for line in triangle.splitlines()]))
pp(antinumbers)

def process_candidate(candidate: Path) -> list[Path]:
    new_value_left = candidate.value + antinumbers[candidate.line + 1][candidate.index]
    new_value_right = candidate.value + antinumbers[candidate.line + 1][candidate.index+1]
    return [Path(candidate.line+1, candidate.index, new_value_left, candidate.numbers + [antinumbers[candidate.line + 1][candidate.index]]),
            Path(candidate.line+1, candidate.index+1, new_value_right, candidate.numbers + [antinumbers[candidate.line + 1][candidate.index + 1]])]

paths = [Path(0, 0, 25, [25])]
#Problema: mesmo que ele chegue no final só vai acabar quando o último patch chegar no inicio da fila
while paths[0].line != len(numbers)-1:
    print("==========================================================================================================================================================")
    candidate = paths.pop(0)
    new_candidates = process_candidate(candidate)
    print("New Candidates: ")
    pp(new_candidates)
    print("New Paths!")
    paths = paths + new_candidates
    paths.sort(key=lambda x: x.value)
    pp(paths[:5])
result = paths.pop(0)
numbers = [100-x for x in result.numbers]
print(numbers)
print(sum(numbers))