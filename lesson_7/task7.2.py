import os

p = [None] * 4
with open('config.yaml', 'r', encoding='utf-8') as f:
    try:
        dr = f.readline().replace('|', '').replace('\n', '').replace('-', '')
        os.mkdir(dr)
        p1 = os.path.join(os.getcwd(), dr)
        os.chdir(p1)
    except FileExistsError:
        print('Already worked with this')
    for i in f:
        try:
            if i.count(' ') == 3:
                a = i.replace('|--', '').replace('\n', '').replace(' ', '')
                p[0] = os.path.join(p1, a)
                os.mkdir(f'{p[0]}')
            else:
                k = i.count(' ')
                a = i.replace('-', '').replace('\n', '').replace(' ', '').replace('|', '')
                p[(k + 1) // 3 - 1] = os.path.join(f'{p[(k + 1) // 3 - 2]}', a)
                if os.path.isdir(a) or not '.' in a:
                    os.mkdir(p[(k + 1) // 3 - 1])
                else:
                    with open(p[(k + 1) // 3 - 1], 'w') as f:
                        print(f'{a} created')
        except Exception:
            print('Delete project or change the file and try again')
            break
