def magic_calculation(a, b):
    add, sub = magic_calculation_102.add, magic_calculation_102.sub
    #imports all the files for the magic calc...Trust me it's magical
    if a < b:
        c = add(a, b)

        for i in range(4, 6):
            c = add(c, i)

        return c

    return sub(a, b)
