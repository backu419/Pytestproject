def test_demo1():
    a=10
    b=20
    assert a != b
    print("My first pytest")
def test_demo2():
    name='HCL'
    text="HCL is located all over India"
    assert name in text
    print("My second pytest")
