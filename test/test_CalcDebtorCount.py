import pytest

from src.CalcDebtorCount import CalcDebtorCount
from src.Types import DataType


class TestCalcDebtorCount:
    @pytest.fixture()
    def empty_data(self) -> tuple[DataType, int]:
        return DataType(), 0

    def test_empty_data(self, empty_data) -> None:
        assert CalcDebtorCount().calc(empty_data[0]) == empty_data[1]

    @pytest.fixture()
    def none_data(self) -> tuple[DataType, int]:
        return None, 0

    def test_none_data(self, none_data: tuple[DataType, int]) -> None:
        with pytest.raises(TypeError) as ex:
            CalcDebtorCount().calc(none_data[0]) == none_data[1]
            assert ex.type == TypeError

    @pytest.fixture()
    def data_and_result0(self) -> tuple[DataType, int]:
        data = {
            "Иванов Иван Иванович": [
                ("математика", 61),
                ("программирование", 90),
                ("литература", 76)
            ],
            "Петров Петр Петрович": [
                ("математика", 61),
                ("программирование", 90),
                ("литература", 61)
            ]
        }

        return data, 0

    @pytest.fixture()
    def data_and_result1(self) -> tuple[DataType, int]:
        data = {
            "Иванов Иван Иванович": [
                ("математика", 60),
                ("программирование", 90),
                ("литература", 76)
            ],
            "Петров Петр Петрович": [
                ("математика", 100),
                ("программирование", 90),
                ("литература", 61)
            ]
        }

        return data, 1

    @pytest.fixture()
    def data_and_result2(self) -> tuple[DataType, int]:
        data = {
            "Иванов Иван Иванович": [
                ("математика", 60),
                ("программирование", 90),
                ("литература", 76)
            ],
            "Петров Петр Петрович": [
                ("математика", 60),
                ("программирование", 90),
                ("литература", 61)
            ]
        }

        return data, 2

    def test_calc1(self, data_and_result1: tuple[DataType, int]) -> None:
        result = CalcDebtorCount().calc(data_and_result1[0])
        assert result == data_and_result1[1]

    def test_calc2(self, data_and_result2: tuple[DataType, int]) -> None:
        result = CalcDebtorCount().calc(data_and_result2[0])
        assert result == data_and_result2[1]

    def test_calc0(self, data_and_result0: tuple[DataType, int]) -> None:
        result = CalcDebtorCount().calc(data_and_result0[0])
        assert result == data_and_result0[1]
