s = set()
passwd = []
Dir = '../data/AvailablePasswords/'
def count_unique_password(path, encoding = 'utf-8'):
    file_path = Dir + path
    with open(file_path,'rb') as f:        
        for i, pw in enumerate(f):
            print(i)
            passwd.append(pw)
            s.add(pw)

def main():
    path = 'Rockyou/rockyou.txt'
    count_unique_password(path)
    print(len(passwd))
    print(len(s))

if __name__ == '__main__':
    main()
