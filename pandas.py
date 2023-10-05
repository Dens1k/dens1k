#Pandas 
#Create Series: 
pd.Series(data, index, dtype, name, copy)

#example: 
pd.Series([1,2,3],
          index=['row_1','row_2','row_3'],
          dtype=int, #fail if data loosing 
          name='pd_Series')

#other ex.:
dict_array={'row_1':1,
            'row_2':2,
            'row_3':3}

#series from dict
series_from_dict = pd.Series(dict_array,
                            index=['row_3','row_4','row_100']  #doing choose from dict 
                                   )
#ex with "copy"
np_array = np.array([5,6,6,8,7])
#series from Numpy 
series_from_nparray = pd.Series(np_array,
                                cope=False) #ussing massiv source. if data change, pd too change 

#create PD 
pd.DataFrame(data,index,columns,dtype,copy)

dict_array = {'col_1':[1,2,3],
              'col_2':[4,5,6]}
df = pd.DataFrame(dict_array,
                 index=['row_1','row_2','row_3'],
                 columns=['col_4','col_1','5'], #choosing column for keys
                 dtype=float)
#equal index
pd.dataframe({'col_1':Series_1,'col_2':Series_2})
