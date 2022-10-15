def test_create_ids(n):
    # думал списком подавать id для проверки, но раз уж нумарация сквозная...
    from random import seed, randint
    seed(5)
    a = [randint(10000, 9999999) for i in range(n)]
    return a

def sum_of_nums(num):
    s = 0
    while (num != 0):
        s = s + num % 10
        num = num // 10
    return s

def calc(n_customers, n_first_id):
    groups = {}
    for i in range(n_first_id, n_first_id+n_customers-1):
        x = sum_of_nums(i)
        if x in groups:
            groups[x] += 1
        else:
            groups[x] = 1
    return groups

def diagnostic_f1(n_customers):
    return calc(n_customers, 0)        
    

#print(diagnostic_f1(999))

def diagnostic_f2(n_customers, n_first_id):
    return calc(n_customers, n_first_id)

#print(diagnostic_f2(999, 333))
