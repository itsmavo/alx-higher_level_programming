#!/usr/bin/python3

""" Class for Node """
class Node:
    """ defines a node of a singly linked list
    Attributes:
    data (int): data
    next_node (Node, optional): node
    """

    def __init__(self, data, next_node=None):
        """ Initiate NOde
        args:
             data (int): data stored in node
             next_node (Node): next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ data getter
        returns:
            data (int)
        """
        return self.__data

    @property
        """ data getter
        returns:
            data (int)
        """
    def next_node(self):
        return self.__next_node

    @data.setter
    """data setter
        args:
            value (Node): value to set
        returns:
            None
        """
    def data(self, value):
        if(not isinstance(value, int)):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    """data setter
        args:
            value (Node): value to set
        returns:
            None
        """
    def next_node(self, value):
        if (not isinstance(value, Node) and value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """Singly linked list class
    """
    __head = None

    def __init__(self):
        pass

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        newList = []
        while(self.__head):
            newList.append(self.__head.data)
            self.__head = self.__head.next_node
        return('\n'.join([str(i) for i in sorted(newList)]))
    def sorted_insert(self, value):
        """insert node in coorect sorted position
        args:
            value (int): value for new node
        """
        newNode = Node(value, self.__head)
        self.__head = newNode
