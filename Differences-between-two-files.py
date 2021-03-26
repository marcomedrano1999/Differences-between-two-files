"""
Differences between two files.

Find differences in file contents.

"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    #Compare the lines to check if are indentical
    if line1 == line2:
        return IDENTICAL
    else:
        #We check the items one by one to determinate the fist difference. Return the index 
        index = 0
        while index < len(line1) and index < len(line2):
            if line1[index] != line2[index]:
                return index
            index += 1
        #if one off the lines is a substring of the another, we return the leght of the substring
        return index

def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    if (idx == -1) or (line1.find("\n") != -1) or (line2.find("\n") != -1) or (line1.find("\r") != -1) or (line2.find("\r") != -1) or (len(line1) < idx) or (len(line2) < idx):
        return ""
    else:
        return line1 + "\n" + "=" * idx + "^\n" + line2 + "\n"


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    idx = 0
    while idx < len(lines1) and idx < len(lines2):
        if singleline_diff(lines1[idx], lines2[idx]) != IDENTICAL:
            return (idx, singleline_diff(lines1[idx], lines2[idx]))
        idx += 1
    if len(lines1) != len(lines2):
        return (idx, 0)
    return (IDENTICAL, IDENTICAL)

def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    openfile = open(filename, "rt")
    data = openfile.readlines()
    openfile.close()
    for line in data:
        if line.find("\n") != -1 or line.find("\r") != -1:
            sub_line = line.splitlines()
            line2 = "".join(sub_line)
            data[data.index(line)] = line2
    return data


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)
    diff = multiline_diff(lines1, lines2)
    if diff == (IDENTICAL, IDENTICAL):
        return "No differences\n"
    else:
        for_lin = "Line {}:\n".format(diff[0])
        idx = diff[1]
        if lines1 == []:
            return for_lin + singleline_diff_format("", lines2[diff[0]], idx)
        if lines2 == []:        
            return for_lin + singleline_diff_format(lines1[diff[0]], "", idx)    
        return for_lin + singleline_diff_format(lines1[diff[0]], lines2[diff[0]], idx)

