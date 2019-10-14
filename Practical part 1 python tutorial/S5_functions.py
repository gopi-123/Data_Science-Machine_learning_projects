# example function definition
def fnc(a, b=None, c="asdf"):
    if not b is None:
        return a+b
    else:
        return a, "you passed none"

result = fnc(1,1)
print result

result, message = fnc(1)
print result, message

print fnc(a=1, c="value")