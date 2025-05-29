import openpyxl
def read_excel():
    # 打开excel文件
    wb=openpyxl.load_workbook("../data/data.xlsx")
    # 选择表
    sheet=wb["Sheet1"]
    # 读数据
    data=[]
    keys=[cell.value for cell in sheet[1]]
    for row in sheet.iter_rows(min_row=2,values_only=True):
        dict_data=dict(zip(keys, row))
        data.append(dict_data)
    print(data)
    # 关闭文件
    wb.close()
    return data