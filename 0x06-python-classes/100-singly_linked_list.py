#!/usr/bin/python3

"""Defines a class Node"""
class Node:
    """Represents a node in a singly linked list

    Attributes:
        __data (int): node data
        __next_node (Node): next node element
    """

    def __init__(self, data, next_node=None):
        """Initializes the node

        Args:
            data (int): node data
            next_node (Node): next linked list node

        Returns:
            None
        """

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """get node data: __data

        Returns:
            (int) node data
        """

        return self.__data

    @property
    def next_node(self):
        """get of __next_node

        Returns:
           the next linked list node
        """
        return self.__next_node

    @data.setter
    def data(self, value):
        """set  of __data

        Args:
            value (int): new node data value

        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """set of __next_node

        Args:
            value (Node): next the linked list node

        Returns:
            None
        """

        if type(value) not in [Node, None]:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __str__(self):
        """String representation of Node instance

        Returns:
            Formatted string representing the node
        """
        return str(self.__data)

"""Defines a class SinglyLinkedList"""

class SinglyLinkedList:
    """Represents a single linked list

    Attributes:
        __head (Node): head of the linked list
    """

    def __init__(self):
        """Initializes the linked list

        Returns:
            None
        """
        self.__head = None

    def SinglyLinkedList(self, value):
        """ inserts a new Node instance into the sorted position

        Args:
            value (int): new node data

        Returns:
            None
        """

        new_node = Node(value)
        curr = self.__head
        if curr is None:
            self.__head = new_node
            return
        if curr.data >= value:
            new_node.next_node = curr
            self.__head = new_node
            return
        while curr is not None:
            if curr.next_node.data >= value:
                break
            curr = curr.next_node
        new_node.next_node = curr.next_node
        curr.next_node = new_node

    def __str__(self):
        """String representation of SinglyLinkedList instance

        Returns:
            Formatted string representing the linked list
        """

        curr = self.__head
        rep_str = ""
        while curr is not None:
            rep_str = str(curr)
            if curr.next_node is not None:
                rep_str += "\n"
            curr = curr.next_node
        return rep_str
