import sys
print "NAME:", sys.modules[__name__]

try:
    from pyex.pyimports.chap2 import chap2_test
    chap2_test.test()
    # from test_module import main
    # from lskdj import laskd
except Exception as err:
    # print err
    from ..chap2.chap2_test import test as testtwo # this works from outside test_module with/without Desktop as path.
    # print "test"
else:
    print "Yay! It worked!"


def test():
    print "this is chap3_test.py"

