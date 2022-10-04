# -*- coding: utf-8 -*-
import json
from typing import Optional

from src.DataReader import DataReader
from src.Types import DataType


class JsonDataReader(DataReader):
    def read(self, path: str) -> Optional[DataType]:
        result: DataType = {}
        with open(path, encoding='utf-8') as file:
            data = json.load(file)

            for student in data:
                result[student]: list[tuple[str, int]] = []
                result[student] = [(y, x[y]) for x in data[student] for y in x]
        return result
