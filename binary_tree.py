from binarytree import Node

def get_root_number(root):
    pass

def count_elements(root):
    pass

def get_min_element(root):
    pass

def test_get_root_number():
    tree = Node(123)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    assert get_root_number(tree) == 123

def test_count_elements():
    tree = Node(1)
    assert count_elements(tree) == 1

def test_count_elements2():
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    print(tree)

    assert count_elements(tree) == 5

def test_get_min_element():
    tree = Node(10)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(1)
    tree.left.right = Node(5)
    tree.left.left.left = Node(4)
    print(tree)

    assert count_elements(tree) == 1
