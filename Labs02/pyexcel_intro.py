import pyexcel
dict = [
    {"name":"huy",
    "age":10},
    {"name":"thong",
    "age":30}
]
pyexcel.save_as(records=dict, dest_file_name="pyexcel-intro.xlsx")