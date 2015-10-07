"""
Test me
"""
print "hi"

def test_me(var_x):
    if var_x > 0:
        return "positive"
    else:
        return "negative"
test_me(-1)
test_me(2)
test_me(3)