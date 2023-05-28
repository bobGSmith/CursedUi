def get_lines_or_cols (scr,line_or_col = "line"):
    lines, cols = scr.getmaxyx() 
    if line_or_col == "line":
        return lines 
    if line_or_col == "col":
        return cols
    
