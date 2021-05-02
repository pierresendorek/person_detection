import os
import json
from typing import Union

class IndexToCategory:
    def __init__(self):
        this_file_path = os.path.dirname(os.path.realpath(__file__))
        with open(this_file_path + "/../data/category_to_index.json", "r") as f:
            self.index_to_category = json.load(f)

    def get_index(self, category:str) -> int:
        for k in self.index_to_category.keys():
            if self._get_category(k) == 'person':
                return int(k)
        return -1

    def _get_category(self, index:Union[int, str]) -> str:
        index = str(index)
        if index in self.index_to_category.keys():
            return self.index_to_category[index].get("name", "None")
        else:
            return "None"



if __name__ == "__main__":
    # print(IndexToCategory().get_category(1))
    print(IndexToCategory().get_index("person"))