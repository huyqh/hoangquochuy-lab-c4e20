def remove_dollar_sign(s):
    list_string = list(s)
    count = 0
    for i in range(len(list_string)):
        if list_string[i] == "$":
            count += 1

    s_replace = s.replace("$","",count)
    return s_replace
replace = remove_dollar_sign(input("Ente the string has the sign($):"))