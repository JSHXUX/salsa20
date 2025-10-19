from . import word


def compute(w1: word.Word, w2: word.Word, w3: word.Word, shift: int):
    result = w2 + w3
    result = result << shift
    result = w1 ^ result
    return result


def quarterround(list: list[word.Word]):
    if len(list) != 4:
        raise ValueError("List must contain 4 words")
    z1 = compute(list[1], list[0], list[3], 7)
    z2 = compute(list[2], z1, list[0], 9)
    z3 = compute(list[3], z2, z1, 13)
    z0 = compute(list[0], z3, z2, 18)
    return [z0, z1, z2, z3]


def rowround(list: list[word.Word]):
    if len(list) != 16:
        raise ValueError("List must contain 16 words")
    [z0, z1, z2, z3] = quarterround([list[0], list[1], list[2], list[3]])
    [z5, z6, z7, z4] = quarterround([list[5], list[6], list[7], list[4]])
    [z10, z11, z8, z9] = quarterround([list[10], list[11], list[8], list[9]])
    [z15, z12, z13, z14] = quarterround([list[15], list[12], list[13], list[14]])
    return [z0, z1, z2, z3, z4, z5, z6, z7, z8, z9, z10, z11, z12, z13, z14, z15]


def columnround(list: list[word.Word]):
    if len(list) != 16:
        raise ValueError("List must contain 16 words")
    [z0, z4, z8, z12] = quarterround([list[0], list[4], list[8], list[12]])
    [z5, z9, z13, z1] = quarterround([list[5], list[9], list[13], list[1]])
    [z10, z14, z2, z6] = quarterround([list[10], list[14], list[2], list[6]])
    [z15, z3, z7, z11] = quarterround([list[15], list[3], list[7], list[11]])
    return [z0, z1, z2, z3, z4, z5, z6, z7, z8, z9, z10, z11, z12, z13, z14, z15]


def doubleround(list: list[word.Word]):
    if len(list) != 16:
        raise ValueError("List must contain 16 words")
    list = columnround(list)
    list = rowround(list)
    return list