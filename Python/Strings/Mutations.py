def mutate_string(string, position, character):
    data = list(string)
    data[position] = character
    odata = ''.join(data)
    return odata
