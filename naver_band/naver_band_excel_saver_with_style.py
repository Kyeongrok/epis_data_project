import pandas as pd
def save_to_excel(df, file_name):
    df.style.set_table_styles(
        [{
            'selector': 'th',
            'props': [('background-color', '#add8e6')]
        }])
    writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
    workbook = writer.book
    format4 = workbook.add_format({'bg_color': '#FFFF00', 'bold':False})
    text_wrap = workbook.add_format({'text_wrap': True, 'bottom': 1, 'top': 1, 'left': 1, 'right': 1, 'bold':False})
    border_fmt = workbook.add_format({'bottom': 1, 'top': 1, 'left': 1, 'right': 1, 'bold':False})

    df.to_excel(writer, 'sheet1', index=False)
    worksheet = writer.sheets['sheet1']
    worksheet.set_column(0, 0, 7.42, cell_format=border_fmt)
    worksheet.set_column(1, 1, 4.58, cell_format=border_fmt)
    worksheet.set_column(2, 2, 25, cell_format=border_fmt)
    worksheet.set_column(3, 3, 25, cell_format=border_fmt)
    worksheet.set_column(4, 4, 4.83, cell_format=border_fmt)
    worksheet.set_column(5, 5, 50, cell_format=text_wrap)
    worksheet.set_column(6, 7, 5, cell_format=text_wrap)
    worksheet.set_column(8, 8, 20, cell_format=text_wrap)
    worksheet.set_column(9, 9, 41, cell_format=text_wrap)
    worksheet.set_column(10, 10, 21, cell_format=text_wrap)
    worksheet.set_column(11, 11, 8, cell_format=text_wrap)



    worksheet.conditional_format('A1:L1', {'type': 'cell', 'criteria': '>=', 'value': 0, 'format': format4})
    writer.save()