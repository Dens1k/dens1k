df.iat[2,1] #info about elements throat index row and columns 
# we use only index: 0,1,2,3... for row and columns 
# 1st param - rows, 2nd - columns 

df['age'].iat[3] #work with Series. We can get value 

df.iat[4, 0] = 'new_name' #can change a data 

df.at['row_3', 'name'] #same .iat but choose a TAG index and columns 
df.at['age'].at['row_2'] #example 
df.at['row4', 'name'] = 100 #example

"""
  df.iloc[ index rows, index columns ]
"""

df.iloc[ [list index rows], [list index col]]
df.iloc[ slicing:index, slicing:col ] 
df.iloc[ [list, bool, value], [list, bool, value] ]

df.iloc[1, 1]
df['наличие авто'].to_list()
df.iloc[df['наличие авто'].to_list(), [True,False,False] ]
df.iloc[1:3, 0]
df.iloc[1:3, [0]] #back DF
df.iloc[1:3, 1] = 99

"""
  df.loc['tag rows', 'tag col']
"""

df.loc['row_2', 'name'] 
df.loc[['row_1', 'row_2']] # back only rows 
df.loc[:, ['age', 'name']] # back columns 
df.loc['row_0' : 'row_3', 'name'] # back Series   
df.loc['row_0' : 'row_3', ['name']] # back DF 

df.loc[df['name'] == 99 ] # back column + working filter 
df.loc['row_0':'row_2', 'name'] = 1 #change data in DF 
# we can change data with format: List, Series, DF
