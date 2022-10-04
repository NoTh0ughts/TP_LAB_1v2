from Types import DataType


class CalcDebtorCount:
    def calc(self, data: DataType) -> int:
        count: int = 0
        for student in data:
            if [x for x in data[student] if x[1] < 61].__len__() > 0:
                count += 1
        return count