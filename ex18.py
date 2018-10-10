def print_three(*args):
    arg1, arg2, arg3 = args
    print ("arg1: %r, arg2: %r, arg3: %r" % (arg1, arg2, arg3))


def print_three_again(arg1, arg2, arg3):
    print ("arg1: %r, arg2: %r, arg3: %r" % (arg1, arg2, arg3))


def print_one(arg1):
    print ("arg1: %r" % arg1)


def print_OK(arg3):
    print ("arg3: %r" % arg3)


print_three("Zed","Shaw","Eric")
print_three_again("Zed","Shaw","Eric")
print_one("First!")
print_OK("ok")

