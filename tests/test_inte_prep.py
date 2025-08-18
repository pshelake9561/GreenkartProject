import pytest

@pytest.mark.usefixtures("scope_class")
class TestExample:
    def test_prep_one(self):
        print("This is test prep one in the class")

    def test_prep_two(self):
        print("This is test prep two in the class")


