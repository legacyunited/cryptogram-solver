import pytest
from solver import solve_cryptogram

def test_solve_cryptogram():
    test = solve_cryptogram()
    sample = 'DL KBZ PVVM ZBDE LKBL EVXFROBRT DZ LKV CFOZL QFOZL QFOX FQ WFNVOMXVML VJRVGL BUU LKV FLKVOZ LKBL KBNV PVVM LODVE.'
    
    assert test.solve(sample) == 'IT HAS BEEN SAID THAT DEMOCRACY IS THE WORST FORST FORM OF GOVERNMENT EXCEPT ALL THE OTHERS THAT HAVE BEEN TRIED'

    with pytest.raises(TypeError):
        test.solve()
    
    assert test.solve('') == 'There is no text to decrypt.'
    assert test.solve(' ') == 'There is no text to decrypt.'