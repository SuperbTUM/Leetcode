# insert a str to another to get the maximum number
# for example
# target = "7546", insert = "754"
# return "77545446"

def concatenate_string(target: str, insert: str) -> str:
    len_t = len(target)
    len_i = len(insert)
    i = 0
    j = 0
    while i < len_t and j < len_i:
        if target[i] < insert[j]:
            return target[:i] + insert + target[i:]
        elif target[i] > insert[j]:
            if i < len_t - 1:
                i += 1
            if j < len_i - 1:
                j += 1
        else:
            while target[i] == insert[j]:
                # string insert may be put either on the left, middle or right
                if i < len_t - 1:
                    i += 1
    return target + insert


if __name__ == '__main__':
    assert concatenate_string("7546", "754") == "7754546"
    assert concatenate_string("7891", "749") == "7897491"
    assert concatenate_string("5627", "562") == "5656227"
