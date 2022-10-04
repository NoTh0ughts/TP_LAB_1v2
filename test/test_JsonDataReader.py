import pytest

from src.JsonDataReader import JsonDataReader
from src.Types import DataType


class TestJsonDataReader:
    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = '{  "Иванов Иван Иванович" :  [    {"математика":80},    {"программирование": 90},    {"литература": ' \
               '76}  ],  "Петров Петр Петрович" :  [    {"математика": 100},    {"программирование": 90},    ' \
               '{"литература":61}  ]} '

        data = {
          "Иванов Иван Иванович": [
            ("математика", 80),
            ("программирование", 90),
            ("литература", 76)
          ],
          "Петров Петр Петрович": [
            ("математика", 100),
            ("программирование", 90),
            ("литература", 61)
          ]
        }

        return text, data

    @pytest.fixture()
    def incorrect_data(self) -> str:
        return '"Иванов Иван Иванович": "литература": 97, "математика": 99, "программирование": 98}, "Петров Петр Петрович": {"литература": 12, "математика": 10, "программирование": 11}} '

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.json")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = JsonDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]

    def test_incorrect_json_format(self, incorrect_data: str) -> None:
        with pytest.raises(OSError) as ex:
            JsonDataReader().read(incorrect_data)
            assert ex.type == OSError
