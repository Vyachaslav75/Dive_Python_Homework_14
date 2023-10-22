import pytest
from Loger import Loger
from pathlib import Path

@pytest.fixture
def my_user():
    usr=Loger('Bobby', 45)
    #return usr
    yield usr
    del usr

@pytest.fixture
def file_path():
    return 'security.json'

@pytest.fixture
def create_usr(my_user):
    usr=my_user.create_user('Jack', 47, 4)
    return usr

def test_check_usr(my_user):
    assert my_user.usr in my_user.db

def test_file_path(file_path):
    assert Path(file_path).exists(), f'File {file_path} not exist'
    
def test_create_usr(create_usr):
    assert create_usr.name == 'Jack'


if __name__ == "__main__":
    pytest.main(['-v'])