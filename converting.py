import pandas

def xlsx_to_csv_pd():
    data_xls = pandas.read_excel('train.xlsx', index_col=0)
    data_xls.to_csv('train.csv', encoding='utf-8')

xlsx_to_csv_pd()
