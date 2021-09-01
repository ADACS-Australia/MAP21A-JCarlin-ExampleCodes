#! /usr/bin/env python

def test_hard_compute():
    from mymodule.default import hard_compute

    answer = hard_compute(1, 'hellp')
    expected = 1
    if answer != expected:
        raise AssertionError(f"hard_compute(1,'help') should return {expected} but returned {answer}")

    answer = hard_compute(1, 'test', 7)
    expected = "test.7"
    if answer != expected:
        raise AssertionError(f"hard_compute(1,'test', 7) should return {expected} but returned {answer}")

    answer = hard_compute(None,'hello')
    expected = -1
    if answer != expected: # "is" instead of "==" since expected is None
        raise AssertionError(f"hard_compute(None,'hello') should return {expected} but returned {answer}")

    return

if __name__ == "__main__":
    # introspect and run all the functions starting with 'test'
    for f in dir():
        if f.startswith('test'):
            print(f)
            globals()[f]()