#read / write 
pd.read_csv() / DataFrame.to_csv()
pd.read_sql() / DataFrame.to_sql()
pd.read_parquet() / DataFrame.to_rapquet() 
#read
pd.read_csv(
  filepath: #way to file 
  sep: #(def ,) separator
  index_col: #col for using like tag row 
  usecols: #list name col in df 
  squeeze: #(def False) True -  if data have only one col, give Series 
  dtype: #data type in col 
  nrows: #count row for read 
  parse_dates: ={'date_0':['yyyy','mm','dd']} #list col for view in data and time type
  infer_datetime_format: #(def. False) if True, pandas trying understand format dating row in col (for optimize) 
  keep_data_col: #(def False) if True pandas stay row whick doing parfe date
  endcoding: #code using for reading
  )
#write 
DataFrame.to_csv(
  filepath: #way
  sep:# (def ,) separator
  columns: #col for write in file 
  header: #(def True) write 1st row tag for col. If give list row, they will be using like a tag col 
  index: #(def True) write index row in file
  index_label: #naming for index
  encoding: #(def UTF-8) 
  )

#read from SQL table 
import sqlite3 as sq #create DB 

def create_table(db='avito_data.db', path='/content/avito_data.csv', name_table='avito'):
  con = sq.connect(db)

  df = pd.read_csv(path)
  df.to_sql(name_table, con, if_exists = 'replace', index = False)
  con.close()

create_table() 

sql_request = '''select * from avito'''
#take data from DB
with sq.connect('avito_data.db') as con:
  df_sql = pd.read_sql(sql_request (*sql select), con(*connector))

df_sql

#argue index_col=
with sq.connect('avito_data.db') as con:
  df_sql_index_col = pd.read_sql(sql_request,
                                 con,
                                 index_col=['user_type', 'categoty_name']
                                )
#write in sql 
with sq.connect('avito_data.db') as con:
  df_sql.to_sql('avito_0',
                con,
                if_exists='fail' #create. Replace - overwrite. Append - insert 
               )
