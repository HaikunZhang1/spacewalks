import pytest
from eva_data_analysis import (
    text_to_duration,
    calculate_crew_size
)

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

@pytest.mark.parametrize("input_value, expected_result", [
    ("Valentina Tereshkova;", 1),
    ("Judith Resnik; Sally Ride;", 2)
])
def test_calculate_crew_size(input_value, expected_result):
    actual_result = calculate_crew_size(input_value)
    assert actual_result == expected_result


# test_text_to_duration_integer()
# test_text_to_duration_float()
# test_text_to_duration_irrational()



