pass_dic = {}
Dir = '../data/AvailablePasswords/'
def cnt(str):
    if str in pass_dic:
        pass_dic[str] = pass_dic[str] + 1
    else:
        pass_dic[str] = 1

def sorted_Dic_by_values(dic):
    items = dic.items()
    backitems = [[v[1], v[0]] for v in items]
    backitems.sort(reverse=True)
    return [backitems[i][1] for i in range(0, len(backitems))]

def sort_dic(pass_dic):
    pass_dic = sorted_Dic_by_values(pass_dic)

def create_dic(path):
    file_path = Dir + path
    with open(file_path, 'r') as f:
        for i, passwd in enumerate(f):
            print(i)
            cnt(passwd)
            sort_dic(pass_dic)


def main():
    path = 'Gmail/userpassword.txt'
    create_dic(path)
    sort_dic(pass_dic)
    print(pass_dic[0:11])

if __name__ == '__main__':
    main()