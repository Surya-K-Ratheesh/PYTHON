def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def two_letters(s):
    if len(s) >= 2 and s[:2].isalpha():
        return True
    return False

def valid_length(s):
    if 2 <= len(s) <= 6:
        return True
    return False

def valid_no(s):
    for i in s:
        if i.isdigit():
            return False
        elif i.isalpha():
            return True
        else:
            return False

    if s[0] == '0':
        return False

    return True



def no_punctuations(s):
    punc = [',','.',' ','/','!','"',':',';']
    for i in s:
        for j in punc:
            if i == j:
                return False
                break
    return True

def is_valid(s):
    if two_letters(s) and valid_length(s) and valid_no(s) and no_punctuations(s):
        return True
    return False

main()
