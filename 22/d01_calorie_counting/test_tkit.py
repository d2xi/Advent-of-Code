import tkit


def test_genInputString():
    assert tkit.genInputString([]) == ""
    assert tkit.genInputString([[1, 2], [3, 4]]) == "1\n2\n\n3\n4"
