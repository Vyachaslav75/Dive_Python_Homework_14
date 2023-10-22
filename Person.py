import json
from pathlib import Path


class CheckName:
    # def __init__(self, ):
    # self.name=name

    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f"Значение {value} должно быть строкой")
        if not value.isalpha():
            raise ValueError(f"Значение {value} должно быть из букв")


class CheckRange:
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        
        setattr(instance, self.param_name, value)

    def validate(self, value):
        
        if not isinstance(value, int):
            raise TypeError(f"Значение {value} должно быть целым числом")
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"Значение {value} должно быть больше {self.min_value}")
        if self.max_value is not None and value >= self.max_value:
            raise ValueError(f"Значение {value} должно быть меньше {self.max_value}")


class Person:
    name = CheckName()
    own_id = CheckRange(0, 10000000)
    level = CheckRange(0, 8)
    my_list_id = []

    def __init__(self, name, own_id, level):
        if len(self.my_list_id) > 0 and own_id in self.my_list_id:
            raise ValueError(f'Такой ID : {own_id} существует')
        self.name = name
        self.own_id = own_id
        self.level = level
        self.my_list_id.append(self.own_id)

    def __str__(self) -> str:
        return f"Имя: {self.name} ID: {self.own_id}  уровень: {self.level}"
    
    def __eq__(self, other) -> bool:
        if self.name == other.name and self.own_id == other.own_id:
            return True
        else:
            return False


class TempPerson:
    name = CheckName()
    own_id = CheckRange(0, 10000000)
    level = CheckRange(0, 8)

    def __init__(self, name, own_id, level=1):
        self.name = name
        self.own_id = own_id
        self.level = level

    def __str__(self) -> str:
        return f"Имя: {self.name} ID: {self.own_id}  уровень: {self.level}"
    
    # def __eq__(self, other) -> bool:
    #     if self.name == other.name and self.own_id == other.own_id:
    #         return True
    #     else:
    #         return False

def load_data_json(file_path):
    if Path(file_path).exists():
        with open(file_path, "r", encoding="utf-8") as f:
            data_db = json.load(f)
    else:
        data_db = {}
    return data_db


def json_write(file_path, data_db):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data_db, f, indent=4, ensure_ascii=False)


def create_base():
    db = load_data_json('security.json')
    db_obj = []
    for key_lvl in db.keys():
        level = int(key_lvl)
        for key_id in db[key_lvl].keys():
            own_id=int(key_id)
            name=db[key_lvl][key_id]
            usr=Person(name, own_id, level)
            db_obj.append(usr)
    return db_obj

def write_base(db):
    data_db={}
    for usr in db:
        print(usr)
        if usr.level in data_db:
            data_db[usr.level][usr.own_id] = usr.name
        else:
            data_db[usr.level]={}
            data_db[usr.level][usr.own_id] = usr.name
        print(data_db)
    json_write('security.json', data_db)

def worker():
    employes = []
    while True:
        try:
            name = input("Введите имя: ")
            if name == "":
                return employes
            own_id = int(input("Введите ID: "))
            level = int(input("Введите уровень: "))
            user1 = Person(name, own_id, level)
            print(user1)
            employes.append(user1)
        except Exception as e:
            print('Ошибка ввода данных')
            print(e)


if __name__ == "__main__":
    #a = Person("ss", 1, 1)
    #print(a.name)
    #print(type(a.level))
    #empl = worker()
    empl = create_base()
    for item in empl:
        print(item)
    write_base(empl)
    # a = Person("sdf", 234, 1)
    # if a in empl:
    #     print('YES')
