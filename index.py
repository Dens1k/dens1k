#work with index for DF
list_index = list('qwqityui')

index_data = pd.Index(list_index,
                      dtype = np.float32,
                      name = 'rows'
                     )

columns_data = pd.Index(['col_1', 'col_2', 'col_3'],
                        name = 'cols'
                       )


