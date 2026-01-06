# Static Lists
"""
class NodeList:
    def __init__(self, key: int):
        self.key = key


    @property
    def key(self):
        return self._key
    @key.setter
    def key(self, key: int):
        if isinstance(key, int):
            self._key = key
        else:
            raise ValueError("ERROR: Invalid key!")




    def __repr__(self):
        return f"{self.key}"


class List:
    def __init__(self, max_length: int):
        self.max_length = max_length
        self.last_pos = -1
        self.datas = [None for n in range(self.max_length)]


    @property
    def max_length(self):
        return self._max_length
    @max_length.setter
    def max_length(self, max_length: int):
        if isinstance(max_length, int) and max_length >= 0:
            self._max_length = max_length
        else:
            raise ValueError("ERROR: The max_length must be greater than or equal to 0!")
    

    @property
    def last_pos(self):
        return self._last_pos
    @last_pos.setter
    def last_pos(self, last_pos: int):
        if isinstance(last_pos, int) and -1 <= last_pos < self.max_length:
            self._last_pos = last_pos
        else:
            raise ValueError("ERROR: The last_pos must be between -1 and (max_length - 1)!")
    

    @property
    def datas(self):
        return self._datas
    @datas.setter
    def datas(self, datas: list):
        if isinstance(datas, list):
            self._datas = datas
        else:
            raise ValueError("ERROR: The datas must be a list!")
    

    

    def search_element(self, value: int):
        for i in range(self.last_pos + 1):
            if self.datas[i].key == value:
                return i
        return -1
    

    def add_element(self, node: NodeList):
        if self.last_pos < self.max_length-1:
            if self.search_element(node.key) == -1:
                self.last_pos += 1
                self.datas[self.last_pos] = node
            else:
                raise ValueError("ERROR: This element already exists!")
        else:
            raise IndexError("ERROR: The list is full!")
    

    def delete_element(self, node_key: int):
        if self.last_pos != -1:
            index = self.search_element(node_key)
            if index != -1:
                for i in range(index, self.last_pos):
                    self.datas[i] = self.datas[i+1]
                self.datas[self.last_pos] = None
                self.last_pos -= 1
            else:
                raise ValueError("ERROR: This value doesn't exist!")
        else:
            raise IndexError("ERROR: The list is empty!")




    def __str__(self):
        return f"{[self.datas[i] for i in range(self.last_pos + 1)]}"
"""




def main():
    pass


if __name__ == "__main__":
    main()