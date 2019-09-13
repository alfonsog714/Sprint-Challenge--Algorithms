'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


# Currently

def count_th(word, count = 0):
    # count = 0
    new_string = word[2:]

    if len(word) <= 1:
        return count

    if word[0] == "t" and word[1] == "h":
        count += 1
        # print(f"Line 21: {new_string}")
        return count_th(new_string, count)
    elif word[0] != "t":
        new_string = word[1:]
        # print(f"Line 24: {new_string}")
        return count_th(new_string, count)

    else:
        return count_th(new_string, count)

# print(count_th("THtHThth"))