import pytest
from eva_data_analysis import text_to_duration

def test_text_to_duration_integer():
    assert text_to_duration("10:00") == 10            # assert: compare the real and expected values, if they are not equal, the test will fail
    # input_value = "10:00"
    # test_result = text_to_duration(input_value) == 10
    # print(f"text_to_duration('10:00') == 10? {test_result}")

def test_text_to_duration_float():
    assert text_to_duration("10:15") == 10.25

def test_text_to_duration_irrational():
    # print(1e-5)
    # print(abs(text_to_duration("10:20")))
    # print(abs(text_to_duration("10:20") - 10.3333333))
    # assert abs(text_to_duration("10:20") - 10.3333333) < 1e-5
    assert text_to_duration("10:20") == pytest.approx(10.3333333)


# test_text_to_duration_integer()
# test_text_to_duration_float()
# test_text_to_duration_irrational()
