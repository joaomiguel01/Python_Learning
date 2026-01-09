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
            raise ValueError("ERROR: The key must be a integer number!")
    

    

    def __str__(self):
        return f"{self.key}"
    

    def __repr__(self):
        return f"{self.key}"

class StaticList:
    def __init__(self, M_numbers: int):
        self.M_numbers = M_numbers
        self.last_pos = -1
        self.datas = [None for n in range(M_numbers)]


    @property
    def M_numbers(self):
        return self._M_numbers
    @M_numbers.setter
    def M_numbers(self, M_numbers: int):
        if isinstance(M_numbers, int) and M_numbers > 0:
            self._M_numbers = M_numbers
        else:
            raise ValueError("ERROR: The M_numbers must be a positive number!")
    

    @property
    def last_pos(self):
        return self._last_pos
    @last_pos.setter
    def last_pos(self, last_pos: int):
        if isinstance(last_pos, int) and -1 <= last_pos < self.M_numbers:
            self._last_pos = last_pos
        else:
            raise ValueError("ERROR: The last_pos must be between -1 and (M_numbers - 1)!")
    



    def search_element(self, key: int):
        for i in range(self.last_pos+1):
            if self.datas[i] is not None and self.datas[i].key == key:
                return i
        return -1


    def add_element(self, key: int):
        node = NodeList(key)

        if self.last_pos < self.M_numbers - 1:
            if self.search_element(node.key) == -1:
                self.last_pos += 1
                self.datas[self.last_pos] = node
            else:
                raise ValueError("ERROR: This element already exists!")
        else:
            raise IndexError("ERROR: Static list is full!")
    

    def delete_element(self, key: int):
        if self.last_pos != -1:
            index = self.search_element(key)
            if index != -1:
                for i in range(index, self.last_pos):
                    self.datas[i] = self.datas[i+1]
                self.datas[self.last_pos] = None
                self.last_pos -= 1
            else:
                raise ValueError("ERROR: Element not found!")
        else:
            raise IndexError("ERROR: Static list is empty!")



    def __str__(self):
        return f"{[self.datas[i] for i in range(self.last_pos+1) if self.datas[i] is not None]}"
    

    def __repr__(self):
        return f"{[self.datas[i] for i in range(self.last_pos+1) if self.datas[i] is not None]}"
"""

"""
class NodeStack:
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
            raise ValueError("ERROR: The key must be a integer number!")


    

    def __str__(self):
        return f"{self.key}"
    

    def __repr__(self):
        return f"{self.key}"

class Stack:
    def __init__(self, m_numbers: int):
        self.m_numbers = m_numbers
        self.top = -1
        self.datas = [None for n in range(self.m_numbers)]

    @property
    def m_numbers(self):
        return self._m_numbers
    @m_numbers.setter
    def m_numbers(self, m_numbers: int):
        if isinstance(m_numbers, int) and m_numbers > 0:
            self._m_numbers = m_numbers
        else:
            raise ValueError("ERROR: The m_numbers must be a positive number!")

    
    @property
    def top(self):
        return self._top
    @top.setter
    def top(self, top: int):
        if isinstance(top, int) and -1 <= top < self.m_numbers:
            self._top = top
        else:
            raise ValueError("ERROR: The top value must be between -1 and (m_numbers-1)!")
    

    def push(self, key: int):
        if self.top < self.m_numbers - 1:
            node = NodeStack(key)
            self.top += 1
            self.datas[self.top] = node
        else:
            raise IndexError("Overflow!")


    def pop(self):
        if self.top != -1:
            node = self.datas[self.top]
            self.datas[self.top] = None
            self.top -= 1
            return node
        else:
            raise IndexError("Underflow!")




    def __repr__(self):
        return f"{[self.datas[i] for i in range(self.top+1)]}"
    

    def __str__(self):
        return f"{[self.datas[i] for i in range(self.top+1)]}"
"""

"""
class NodeQueue:
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
            raise ValueError("ERROR: The key must be a integer number!")
    



    def __str__(self):
        return f"{self.key}"
    
    
    def __repr__(self):
        return f"{self.key}"

class Queue:
    def __init__(self, m_values: int):
        self.m_values = m_values
        self.start_pos = 0
        self.last_pos = -1
        self.datas = [None for n in range(self.m_values)]

    
    @property
    def m_values(self):
        return self._m_values
    @m_values.setter
    def m_values(self, m_values: int):
        if isinstance(m_values, int) and m_values > 0:
            self._m_values = m_values
        else:
            raise ValueError("ERROR: The m_value must be a positive number!")
    

    @property
    def last_pos(self):
        return self._last_pos
    @last_pos.setter
    def last_pos(self, last_pos: int):
        if isinstance(last_pos, int) and -1 <= last_pos < self.m_values:
            self._last_pos = last_pos
        else:
            raise ValueError("ERROR: The last_pos must be between -1 and (m_values - 1)!")
    

    @property
    def start_pos(self):
        return self._start_pos
    @start_pos.setter
    def start_pos(self, start_pos: int):
        if isinstance(start_pos, int) and 0 <= start_pos < self.m_values:
            self._start_pos = start_pos
        else:
            raise ValueError("ERROR: The start_pos must be between 0 and (m_values - 1)!")


    def add_element(self, key: int):
        if self.last_pos == self.m_values - 1:
            raise IndexError("Overflow!")
        
        node = NodeQueue(key)
        self.last_pos += 1
        self.datas[self.last_pos] = node


    def delete_elemet(self):
        if self.start_pos > self.last_pos:
            raise IndexError("ERROR: Underflow!")
        
        node = self.datas[self.start_pos]
        self.datas[self.start_pos] = None
        self.start_pos += 1
        return node

    def __str__(self):
        return f"{self.datas}"


    def __repr__(self):
        return f"{self.datas}"
"""

"""
class NodeLinkList:
    def __init__(self, key: int, after: "NodeLinkList | None"):
        self.key = key
        self.after = after


    @property
    def key(self):
        return self._key
    @key.setter
    def key(self, key: int):
        if isinstance(key, int):
            self._key = key
        else:
            raise ValueError("ERROR: The key must be a integer number!")
    

    @property
    def after(self):
        return self._after
    @after.setter
    def after(self, after: "NodeLinkList | None"):
        if isinstance(after, NodeLinkList) or after is None:
            self._after = after
        else:
            raise ValueError("ERROR: The pointer must point to another node or None!")
    


    
    def __str__(self):
        return f"{self.key}"
    def __repr__(self):
        return f"{self.key}"
    

class LinkList:
    @staticmethod
    def print_data(head: NodeLinkList):
        pont = head
        while pont is not None:
            print(f"{pont} ->", end=" ")
            pont = pont.after
        print("None")
    

    @staticmethod
    def search_node(head: NodeLinkList, key: int):
        pt = head
        ant = None

        while pt is not None:
            if pt.key == key:
                return ant, pt
            ant = pt
            pt = pt.after
        return ant, None


    @staticmethod
    def add_node(head: NodeLinkList, key: int):
        ant, pt = LinkList.search_node(head, key)
        node = NodeLinkList(key, pt)
        if pt is None:
            if ant == None:
                head.after = node
            else:
                ant.after = node

            node.after = None 
        else:
            raise ValueError("ERROR: This element already exists!")

    @staticmethod
    def delete_element(head: NodeLinkList, key: int):
        ant, pt = LinkList.search_node(head, key)
        if pt is not None:
            if ant == None:
                raise ValueError("ERROR: Cannot remove the head node!")
            
            ant.after = pt.after
            pt.after = None
        else:
            raise ValueError("ERROR: This node doesn't exist!")
"""


def main():
    pass


if __name__ == "__main__":
    main()
