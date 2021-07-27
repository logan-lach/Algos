from Graph.Graph import Node


def kruskals(node):

    visited = {node.name}

    print('hello')


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.neighbors = {
    n2:3,
    n4:1
}

n2.neighbors = {
    n1:3,
    n3:3,
    n5:2,
    n4:6
}

n3.neighbors = {
    n2:3
}

n4.neighbors = {
    n2:6,
    n1:1,
    n5:5
}

n5.neighbors = {
    n2:2,
    n5:5
}


print(kruskals(n1))