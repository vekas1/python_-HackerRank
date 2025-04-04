def swap_case(s):
    result = ""
    for val in range(len(s)):
        if s[val].isupper():
            result += s[val].lower()
        elif s[val].islower():
            result += s[val].upper()
        else:
            result += s[val]  
    return result


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)