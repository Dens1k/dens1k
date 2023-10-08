df = pd.DataFrame({'col_1' : [1,2,3]})

df.set_index(['col_1'], #set col in index 
            append = True, #for stay old index 
             inplace = True 
            )

df.reset_index(['col_1']) #doing columns index
#if method stay empty, all index will be columns 

df['col_1'] #for select column (if < 2 it will be Series)
df[['col_1']] #for select column (this for DF)
df[['col_1', 'col_2']] = 1  #for select column (this for DF), and can be give new value
df['NEW_COL'] = 2 #for creating a new col 
df['NEW_COL'] = df['col_1'] #can use existing col 
del df['NEW_COL'] #for del col 
df[[False, True, True, False, True, False]] = 100 #for operation with row where index is True 
