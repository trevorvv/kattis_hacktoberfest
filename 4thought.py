operations = [' + ', ' - ', ' * ', ' // ']

size = int(input())

for i in range(size):
    answer = False
    n = int(input())
    for o1 in operations:
        if answer == True:
            break
        for o2 in operations:
            if answer == True:
                break
            for o3 in operations:
                sv = f'4 {o1} 4 {o2} 4 {o3} 4'
                if n == eval(sv):
                    sv = sv.replace('//', '/')
                    print(f'{sv} = {n}')
                    answer = True
                    break
    if answer == False:
        print('no possible solution')
