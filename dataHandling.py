password = []
class data_handle(object):
    def loading_password(self, file_path,pass_file_path, encoding ='utf-8'):
        with open(file_path, 'r') as f:            
            print(f.readline())
        self.write_password(pass_file_path)

    def write_password(self, file_path):
        with open(file_path, 'w') as f:
            for i in range(len(password)):
                f.write(password[i] + '\n')    
    
if __name__ == '__main__':
    loading_password('../passwordData/rockyou.txt','../passwordData/small_rockyou.txt')
