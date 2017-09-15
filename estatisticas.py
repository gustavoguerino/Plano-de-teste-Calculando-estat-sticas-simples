def is_sizeSqn(seqNumeros):
    if(type(seqNumeros) != int):
        raise TypeError()
    for x in range(seqNumeros):
        entrada = raw_input()
        try:
            int(entrada)
        except:
            raise TypeError
    return True