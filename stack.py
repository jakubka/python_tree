n_max = None
a = None
n = None

def create_empty_stack(size = 10):
    global n_max, a, n
    n_max = size
    a = [None] * n_max
    n = 0

def push(number):
    global n_max, a, n
    if n == n_max:
        a_new = [None] * n_max * 2
        for i in range(1, n + 1):
            a_new[i - 1] = a[i - 1]
        a = a_new
        n_max = n_max * 2
    n = n + 1
    a[n - 1] = number
     

def pop():
    global n_max, a, n
    if n == 0:
        return "zasobnik je prazdny"
    x = a[n - 1]
    n = n - 1
    return x
    

def get_content():
    global n_max, a, n
    l = []
    for i in range(1, n + 1):
        l.append(a[i - 1])
    return l

def get_stack_capacity():
    global n_max, a, n
    return n_max

def test_empty():
    create_empty_stack()
    assert get_content() == []

def test_push():
    create_empty_stack()
    push(123)
    assert get_content() == [123]

def test_push_full():
    create_empty_stack(3)
    assert get_stack_capacity() == 3
    push(123)
    push(123)
    push(123)
    push(123)
    assert get_stack_capacity() == 6

def test_push_full2():
    create_empty_stack(2)
    push(1)
    push(2)
    push(3)
    push(4)
    push(5)
    push(6)
    push(7)
    push(8)
    push(9)
    push(10)
    assert get_content() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_push3():
    create_empty_stack()
    push(123)
    push(555)
    push(777)
    assert get_content() == [123, 555, 777]

def test_pop():
    create_empty_stack()
    push(123)
    push(555)
    pop()
    assert get_content() == [123]

def test_pop2():
    create_empty_stack()
    push(123)
    push(555)
    assert pop() == 555

def test_pop_empty():
    create_empty_stack()
    assert pop() == "zasobnik je prazdny"

def test_everything():
    create_empty_stack()

    push(1)
    push(2)

    assert get_content() == [1, 2]

    assert pop() == 2

    assert get_content() == [1]

    push(3)

    assert get_content() == [1, 3]

    assert pop() == 3
    assert pop() == 1

    assert get_content() == []
