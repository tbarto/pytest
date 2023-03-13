from app import runningSum

def test_runningsum_empty_list(expected, actual):
    input = []
    expected = []
    
    assert runningSum(input) == expected
    
def test_runningSum_multiple_values():
    input = [1,2,3,4]
    expected = [1,2]
    
    assert runningSum(input) == expected
