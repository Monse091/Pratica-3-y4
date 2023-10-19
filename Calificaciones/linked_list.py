from node import Node
class LinkedList:
    def __init__(self):
        self.primero = None

    def insert(self, estudiante):
        new_node = Node(estudiante)
        new_node.next_node = self.primero
        self.primero = new_node

        return estudiante

    def get_list(self):
        current = self.primero
        list = []
        while current:
            estudiante = current.valor
            list.append(estudiante)
            current = current.next_node
        return list