def concatenate(**kwargs):
    result = ''
    # Iterating over the python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result

print(concatenate(a="Sanchit", b="is", c="the", d="best", e="software", f="developer", g="!"))
