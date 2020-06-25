def concatenate(**new):
    result = ''
    # Iterating over the python kwargs dictionary
    for arg in new:
        result += arg
    return result

print(concatenate(a="Sanchit", b="is", c="the", d="best", e="software", f="developer", g="!"))
