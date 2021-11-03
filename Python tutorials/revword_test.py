from revword2 import revword

def test_number():
    assert revword(5)== "Five"
    assert revword(12)== "Twelve"
    assert revword(105)== "One Hundred Five"
    assert revword(9400)== "Nine Thousand Four Hundred "