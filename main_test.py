import pytest
import re

def regex_test(expected, content):
    pos = 0
    for token in expected:
        res = re.search(token, content[pos:])
        if res is None:
            assert False, f'Expect: {token}'
        pos += res.start() + 1

@pytest.mark.T1
def test_main_1():
    # Input: 10 20 30 -> ascending: 10 20 30
    content = open('result1.txt').read()
    print(content)
    regex_test([r'\b10\b', r'\b20\b', r'\b30\b'], content)

@pytest.mark.T2
def test_main_2():
    # Input: 15 5 25 -> ascending: 5 15 25
    content = open('result2.txt').read()
    print(content)
    regex_test([r'\b5\b', r'\b15\b', r'\b25\b'], content)

@pytest.mark.T3
def test_main_3():
    # Input: 30 10 20 -> ascending: 10 20 30
    content = open('result3.txt').read()
    print(content)
    regex_test([r'\b10\b', r'\b20\b', r'\b30\b'], content)

@pytest.mark.T4
def test_main_4():
    # Input: -3 7 -1 -> ascending: -3 -1 7
    content = open('result4.txt').read()
    print(content)
    regex_test([r'-3', r'-1', r'\b7\b'], content)
