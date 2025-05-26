# test_example.py

def test_sample_number(sample_number):
    assert sample_number == 42

def test_sample_list(sample_list):
    assert "banana" in sample_list

def test_resource(setup_and_teardown):
    assert setup_and_teardown == "Resource Ready"