from he import hello

def test_default():
    assert hello() == "Hello, world"
    
def test_argument():
    for name in ["Surya", "Cristiano"]:
        assert hello(name) == f"Hello, {name}"