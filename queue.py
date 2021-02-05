n_max = None
a = None
n = None

def create_empty_queue(size = 10):
    global n_max, a, n, zac, kon
    n_max = size #velikost pole
    a = [None] * n_max 
    n = 0 #pocet prvku 
    zac = 0
    kon = n - 1

def enqueue(number):
    global n_max, a, n, zac, kon
    if n == 0:
        a[zac] = number
        n = n + 1
        kon = n - 1
    elif n == n_max:
        return "Queue is full" 
    elif kon == n_max and n != n_max:
        kon = 0
        kon = kon + 1
        a[kon] = number 
        n = n + 1
    else:
        a[n] = number 
        n = n + 1 
        kon = n - 1
            
def dequeue():
    global n_max, a, n, zac, kon
    if n == 0:
        return "Queue is empty"
    else:
        x = a[zac]
        zac = zac + 1
        n = n - 1 
        kon = n
        a[0] = a[zac]
        a[n] = a[kon]
        return x
     
       
        

def get_content():
    global n_max, a, n, zac, kon
    l = []
    for i in range(0, n):
        l.append(a[i])
    return l

def is_empty():
    global n_max, a, n, zac, kon
    if n == 0: 
        return True
    else: 
        return False 


def is_full():
    global n_max, a, n, zac, kon
    if n == n_max:
        return True 
    else:
        return False

def is_sorted():
    global n_max, a, n, zac, kon
    sort_check = True
    for i in range(1, n - 1): 
        if a[i] < a[i - 1]: 
            sort_check = False
        i = i + 1                 
    return sort_check 

def is_sorted_cycling():
    global n_max, a, n, zac, kon
    sort_check = True
    for i in range(zac + 1, kon): 
        if a[zac + 1] < a[zac]: 
            sort_check = False
        zac =  zac + 1                
    return sort_check     

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

def test_dequeue():
    create_empty_queue()
    enqueue(123)
    enqueue(555)
    dequeue()
    assert get_content() == [555]

def test_dequeue2():
    create_empty_queue()
    enqueue(123)
    enqueue(555)
    assert dequeue() == 123
    assert dequeue() == 555

def test_dequeue_empty():
    create_empty_queue()
    assert dequeue() == "Queue is empty"

def test_is_empty_yes():
    create_empty_queue()
    enqueue(1)
    dequeue()
    assert is_empty() == True

def test_is_empty_no():
    create_empty_queue()
    enqueue(1)
    assert is_empty() == False

def test_is_full_yes():
    create_empty_queue(3)
    enqueue(1)
    enqueue(2)
    enqueue(3)
    assert is_full() == True

def test_is_full_no():
    create_empty_queue(3)
    enqueue(1)
    enqueue(2)
    assert is_full() == False

def test_cycling():
    create_empty_queue(5) # size = 5
    enqueue(1)
    enqueue(2)
    enqueue(3)
    enqueue(4)
    dequeue()
    dequeue()
    dequeue()
    enqueue(5)
    enqueue(6)
    enqueue(7)
    assert get_content() == [4, 5, 6, 7]
    enqueue(8)
    assert enqueue(9) == "Queue is full"

def test_is_sorted_yes():
    create_empty_queue(5) # size = 5
    enqueue(1)
    enqueue(2)
    enqueue(3)
    enqueue(4)
    enqueue(5)
    assert is_sorted() == True

def test_is_sorted_no():
    create_empty_queue(5) # size = 5
    enqueue(1)
    enqueue(2)
    enqueue(4)
    enqueue(3)
    enqueue(5)
    assert is_sorted() == False    

def test_is_sorted_cycling_yes():
    create_empty_queue(5) # size = 5
    enqueue(1)
    enqueue(2)
    dequeue()
    dequeue()
    enqueue(3)
    enqueue(4)
    enqueue(5)
    enqueue(6)
    enqueue(7)
    assert is_sorted_cycling() == True

def test_is_sorted_cycling_no():
    create_empty_queue(5) # size = 5
    enqueue(1)
    enqueue(2)
    dequeue()
    dequeue()
    enqueue(3)
    enqueue(4)
    enqueue(5)
    enqueue(1)
    enqueue(2)
    assert is_sorted_cycling() == False