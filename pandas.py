Pandas 

Create Series: 
pd.Series(data, index, dtype, name, copy)

example: 
pd.Series([1,2,3],
          index=['row_1','row_2','row_3'],
          dtype=int, --fail if data loosing 
          name='pd_Series')

other ex.:
dict_array={'row_1':1,
            'row_2':2,
            'row_3':3}
