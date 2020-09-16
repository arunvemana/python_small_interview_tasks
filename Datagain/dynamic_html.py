data = ""
new_row = """<tr></tr>"""
new_column_black = """<td style="border: 1px solid black;
  width:30px;
  height:30px;" bgcolor="black" ></td>"""
new_column_white = """<td style="border: 1px solid black;
  width:30px;
  height:30px;"></td>"""

input_Wh = int(input("enter the width height of the table without px"))
input_Wh_cell = int(input("enter the cell width height without px"))
column_row_count = int(input_Wh/input_Wh_cell)

condition_check = True

for i in range(column_row_count):
    data += new_row
    for j in range(column_row_count):
        if condition_check:
            data = data[:-5]+new_column_white+data[-5:]
        else:
            data = data[:-5]+new_column_black+data[-5:]
        condition_check = (lambda a:False if a else True)(condition_check)

html_text = f"""<!DOCTYPE html>
<html>
<head>
</head>
<body>

<h1>Write a Python script using nested for loop to
create a chess board, use table width = 270px and
take 30px as cell height and width. You need to output
HTML in a file on the local file system which when
opened in the browser looks like a chess board.</h1>

<table style="border-collapse: collapse;border: 1px solid black;  table-layout: auto;
  width: {input_Wh}px;
  height:{input_Wh}px;" class="a">
{data}
</table>
</body>
</html>
"""

with open("test_html.html","w") as f:
    f.write(html_text)
