str1 = "DBRbrURBBxRUUxFFxRDDxRRRRRRRRRRRRRRRRRRRR"

last_x = str1.rfind('x')
substr = str1[:last_x]
substr2 = substr.replace("x", "")
print(substr2)