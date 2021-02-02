n_max = None
a = None
n = None

def create_empty_queue(size = 10):
    global n_max, a, n, zac, kon
    n_max = size #velikost pole
    a = [None] * n_max 
    n = 0 #pocet prvku 
    zac = a[0]
    kon = a[0]

def enqueue(number):
    global n_max, a, n, zac, kon
    if n == 0:
        a[0] = number
        n = n + 1
        kon = a[n-1]
    elif n == n_max:
        return "Queue is full" 
    else:
        a[n] = number 
        n = n + 1 
        kon = a[n-1]
        
        

def dequeue():
    pass

def get_content():
    global n_max, a, n
    l = []
    for i in range(0, n):
        l.append(a[i])
    return l

#########################################################

def test_empty():
    create_empty_queue()
    assert get_content() == []

def test_enqueue():
    create_empty_queue()
    enqueue(123)
    assert get_content() == [123]

def test_enqueue2():
    create_empty_queue()
    enqueue(111)
    enqueue(222)
    enqueue(333)
    assert get_content() == [111, 222, 333]

def test_enqueue_full():
   create_empty_queue(2)
   enqueue(1)
   enqueue(2)
   assert enqueue(3) == "Queue is full" 

# def test_dequeue():
#     create_empty_queue()
#     enqueue(123)
#     enqueue(555)
#     dequeue()
#     assert get_content() == [555]

# def test_dequeue2():
#     create_empty_queue()
#     enqueue(123)
#     enqueue(555)
#     assert dequeue() == 123

# def test_dequeue_empty():
#     create_empty_queue()
#     assert dequeue() == "Queue is empty"