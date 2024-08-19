#This file is used to test the file c.py

from c import square

def main():
    test_square()
    
def test_square():
    """
    if square(2) != 4:
        print("Error")
        
    if square(3) != 9:
        print("Error")
    """
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 Squared was not 4")
        
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
        
    try:
        assert square(-2) == 4
    except AssertionError:
        print("2 squared was not 4")
        
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")
        
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")
        
    
    
        
if __name__ == "__main__":
    main()