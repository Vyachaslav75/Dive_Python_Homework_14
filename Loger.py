from Person import *

class Loger:
    db=[]
    def __init__(self, name, own_id):
        self.usr=TempPerson(name, own_id)
        self.loader()
        if self.usr in self.db:
            #print('YES')
            self.usr=self.db[self.db.index(self.usr)]
            #print(self.usr)
        else:
            raise Exception(f'User {name} access denied')
        
    def loader(self):
        self.db = create_base()
        
    def create_user(self, name, own_id, level):
        if level<=self.usr.level:
            temp=Person(name, own_id, level)
            self.db.append(temp)
            return temp
        else:
            raise Exception('Level error')
        
    def __del__(self):
        self.db=[]
        Person.my_list_id=[]
        
if __name__ == "__main__":
    a=Loger('Bobby', 45)
    print (a.usr)
    b=a.create_user('Jack', 47, 4)
    print(b)
    for i in a.db:
        print(i)