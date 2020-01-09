#!/usr/bin/python3


class Node:
    """Represents a node in a singly linked list

    Attributes:
        __data (int): data stored inside the node
        __next_node (Node): next node in the linked list
    """

    def __init__(self, data, next_node=None):
        """Initializes the node

        Args:
            data (int): node data
            next_node (Node): linked list next node

        Returns:
            None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get: __data

        Returns:
            node data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """set:__data

        Args:
            value (int): node data

        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get: __next_node

        Returns:
           the next node in the linked list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """set: __next_node

        Args:
            value (Node): linked list next node

        Returns:
            None
        """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __str__(self):
        """String representation of Node instance

        Returns:
            Formatted string representing the node
        """
        return str(self.__data)


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

        new = Node(value)
        curr = self.__head
        if curr is None or curr.data >= value:
            if curr:
                new.next_node = tmp
            self.__head = new
            return
        while curr.next_node is not None:
            if curr.next_node.data >= value:
                break
            curr = curr.next_node
        new.next_node = curr.next_node
        curr.next_node = new


    def __str__(self):
        """String representation of SinglyLinkedList instance

        Returns:
            Formatted string representing the linked list
        """
        rep_str = ""
        curr = self.__head
        while curr is not None:
            rep_str += str(curr)
            if curr.next_node is not None:
                rep_str += "\n"
            curr = curr.next_node

