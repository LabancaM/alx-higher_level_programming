#!/usr/bin/python3

"""define node and SinglyLinkedList class"""


class Node:
    """Node class"""

    def __init__(self, data, next_node=None):
        """iniitialisation

        args
            data: input data
            next_node: next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get data"""
        return self.__data

    @data.setter
    def data(self, value):
        if isinstance(value, int) is False:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """define SinglyLinkedList class"""

    def __init__(self):
        """initialisation"""
        self.__head = None

    def sorted_insert(self, value):
        """ sorted insert

        args
            value: value to insert
        """
        node = Node(value)
        if self.__head is None:
            node.next_node = None
            self.__head = node
        elif self.__head.data > value:
            node.next_node = self.__head
            self.__head = node
        else:
            head = self.__head
            while head.next_node is not None and head.next_node.data < value:
                head = head.next_node
            node.next_node = head.next_node
            head.next_node = node

        def __str__(self):
            """ print representation"""
            liste = []
            svg = self.__head
            while svg is not None:
                liste.append(str(svg.data))
                svg = svg.next_node
            return "\n".join(liste)
