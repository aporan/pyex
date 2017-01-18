import sys
print "NAME:", sys.modules[__name__]

try: 
    from test_module.chap2 import chap2_test
    # from test_module import main
    # from lskdj import laskd
except Exception as err:
    # print err
    from ..chap2.chap2_test import test as testtwo # this works from outside test_module with Desktop as path.
    # print "test"
else:
    print "Yay! It worked!"


def test():
    print "this is chap3_test.py"
