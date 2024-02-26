import re
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    pattern = "[A-Z][a-z]*"
    return re.findall(pattern, simple_string)

def grades():
    with open ("assets/grades.txt", "r") as file:
        grades = file.read()


        gradeB_pattern = "[\w ]*:\ B"
        gradeB_list = re.findall(gradeB_pattern, grades)
        names_list = []
        for elem in gradeB_list:
            name = elem.split(":")[0]
            names_list.append(name)
    return names_list

def logs():
    with open("assets/logdata.txt", "r") as file:
        logdata = file.read()
   
    pattern = """
    (?P<host>[\d]*.[\d]*.[\d]*.[\d]*)    
    (\ -\ )  
    (?P<user_name>[\w-]*) 
    (\ \[) 
    (?P<time>\w*/\w*/.*)
    (\]\ \") 
    (?P<request>.*)
    (")
    """
 
    result = []
    for item in re.finditer(pattern, logdata, re.VERBOSE):
        result.append(item.groupdict())
    return result