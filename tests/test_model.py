from researchcode.model import MyModel


def test_overfitting():
    my_model = MyModel()
    assert my_model.train() is None
