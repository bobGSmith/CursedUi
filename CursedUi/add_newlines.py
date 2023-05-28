def add_newlines (string, nth = 10, indent = " ", startIndent=False,newline="\n"):
    new_str = newstr = indent if startIndent else ""
    prev_len = 0
    for i, w in enumerate(string.split(" ")): 
        cur_len = len(w) + 1
        if prev_len + cur_len > nth - len(indent) - 4: 
            new_str += f"\n{indent}"
            prev_len = 0
        if "\n" in w:
            prev_len = len(w.split("\n")[-1])
            new_str += f" {w.split(newline)[0]}"
            new_str += f"\n{indent}"
            new_str += w.split("\n")[-1]
        else: 
            new_str += w if prev_len == 0  else f" {w}"
            prev_len += cur_len

    return new_str