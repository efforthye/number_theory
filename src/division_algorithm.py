# python src/division_algorithm.py
def divide(a, b):
    q = 0
    while a>=b:
        a = a-b
        q = q+1
    print(f"몫: {q}, 나머지: {a}")
    # print("몫: {}, 나머지: {}".format(q, a))

divide(21, 5) # 몫: 4, 나머지: 1
divide(1523, 24) # 몫: 63, 나머지: 11

# a = bq+r
# a = b(q+1)+a-b
# bq+r = b(q+1)+a-b

# a = a-b
# q = q+1
