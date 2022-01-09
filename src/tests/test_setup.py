import pytest


class Client(object):
    def connect(self):
        pass

    def send(self, msg):
        pass

    def close(self):
        pass


@pytest.fixture()
def client():
    # -- 前処理　
    client = Client()
    client.connect()

    # テスト実行
    yield client

    # -- 後処理
    client.close()


def test_sample(client: Client):
    client.send('message')
    

class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()


# Arrange
@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]


def test_共通のオブジェクトを用意しておいてfixtureで呼び出す(fruit_bowl):
    # Act
    fruit_salad = FruitSalad(*fruit_bowl)

    # Assert
    assert all(fruit.cubed for fruit in fruit_salad.fruit)
