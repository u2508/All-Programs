import pandas as pd

# read the csv file
df = pd.read_csv('excel.csv')

# create an excel writer object
writer = pd.ExcelWriter('GMRC.xlsx')

# write the dataframe to excel
df.to_excel(writer,index=False)
# save the excel file
writer.close()