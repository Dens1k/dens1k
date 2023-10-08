#work with index for DF
list_index = list('qwqityui')

index_data = pd.Index(list_index,
                      dtype = np.float32,
                      name = 'rows'
                     )

columns_data = pd.Index(['col_1', 'col_2', 'col_3'],
                        name = 'cols'
                       )

#use it index in df 
df_data = pd.DataFrame({'col_1' : [1, 2, 3, 4, 5, 6, 7, 8],
                        'col_2' : [1, 2, 3, 4, 5, 6, 7, 8],
                       'col_3' : [1, 2, 3, 4, 5, 6, 7, 8]},
                       index = index_data,
                       columns = columns_data) 

#get index from DF
#index columns = name columns 
index = df.index 
columns = df.columns 
#change index col in DF 
df.columns = ['new_col','new_col2','new_col3']
columns = df.columns 

#index to list 
index.to_list() 
columns.to_list()

#to massive 
index.to_numpy() 
columns.to_numpy() 

#distinct, count index 
index_data = df_data.index
columns_data = df_data.columns 
print(f'Index row => {index_data}')
print(f'Index row => {columns_data}')

index_data_unique() #uniq data 
index_data.nunique() #count uniq data 

index_data.is_unique #boolian aboou uniq value 
print(index_data.duplicated()) #writing bool. If data already been in list - True

print(index_data.name) #write name index 
print(columns_data.name) #write name col 

index_data.name = 'rows_new' #rename row 
columns_data.name = 'cols_new' #rename col 

df_data.rename(columns={'col_1' : 'col_11'}#rename col in DF without change a data 
              , axis = 1) #coordinate X, Y 

df_data.rename({'col_1' : 'col_11'}
              , axis = 1) #coordinate X, Y 

df_data.rename(columns={str.upper,#can use foo 
              axis = 0,
              inplace = True)#can change data in DF 

df_nan.index.hasnans #have df empty 
df_nan.index.isna() #show True for NaN value 
df_nan.index.dropna() #del NaN





