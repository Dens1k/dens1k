#create a multiindex from list 
array = [[1, 1, 2, 2], ['row_1', 'row_2', 'row_3', 'row_4']]
multi_array = pd.MultiIndex.from_arrays(array, names = ['level_0', 'level_1'])

df_index = pd.DataFrame([[1,2,3],
                         [1,2,3]],
                        index = multi_array)

df_columns = pd.DataFrame([[1,2,3],
                         [1,2,3]],
                         columns = multi_array)

#multiIndex can be for index and columns 

#creating multiIndex method "from product" 
level_0 = ['row_1', 'row_2']
level_1 = [1, 2, 3]

multi_product = pd.MultiIndex.from_product([level_0, level_1], names = ['level_0', 'level_1'])

#multiIndex from cortage 
tuples = [(1, 'row_1'), (1, 'row_2'), (1, 'row_3'), (2, 'row_1'), (2, 'row_2'), (2, 'row_3')]

multi_tuples = pd.MultiIndex.from_tuples(tuples,
                                         names = ['level_0', 'level_1']
                                        )
df.index.nlevels #count level index 
df.index.levshape #tuples with length each lvl 
df.index.names #names lvl *df.index.names = ['new_name_1', 'new_name_2']
df.index.set_names(['lvl_0', 'lvl_1'], inplace = True) #create a new multiIndex 
df.index.set_names('new_lvl_0', level = 1, inplace = True) #change index 
df.index.levels #read elements in multiIndex 
df.index = name_new_index #change value index 
df.index.set_levels([[1,2,3],['q','w','e','r','t']]) #change index 
df.index.set_levels(['q','w','e','r','t'], level = 0) #change only on level = 0
df.reset_index() #can read multiIndex look like DF 
df.droplevel([level = 1]) #(['lvl1', 'lvl2'])
