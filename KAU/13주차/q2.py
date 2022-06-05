def appear(str_a:str, str_b:str) -> any: 
    string_duplicate = list()
    for i in str_a: 
        for j in str_b:
            if i == j and i not in string_duplicate:
                # i에 있는 문자열이랑 j에 있는 문자열이랑 같으면서, 리스트에 해당 문자열이 없다면
                string_duplicate.append(i)
                # 리스트에 해당 문자열을 append
            else:
                continue
            # 아니라면 continue

    return string_duplicate

print(appear('banana', 'na'))
print(appear('banana', 'nbza'))