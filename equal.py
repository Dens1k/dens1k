series == 5 #checking each value from Series with 5. Answer looks like BOOL
series > [1,2,3,4,5] #it's can be equal. Answer bool
series > df['row'] #index can be equal for this operation
df == 5 #check each value 
df > [1,2,3] #value must be equal count column in df 
df1 == df2 #must be same index row and columns. 
df1 == df2[['col3','col2','col1']] #will be fail, coz sequence must be equal 

method: #can be check not same index! 
eq() ==
ne() !=
le() <=
lt() <
ge() >=
gt() >

Series.le(df1['col3']) #1-st happend equal index, after that operator
df.le(df2[['col2','col3']])
df.le([10,20,30,40], axis = 0)#row equal 
df.equal(df)#True
df.equal(df[['col3','col2','col1']] #false
series.equal(series) #True

df.all() # checking value in each columns. If all values in columns == True answer will be True 
df.all(axis=1)#also we can check row 
df.all(axis=None) #back True if EVERYvalue in DF == True 
df['col1].all() #example Its work with index, series, df 
df.any() #work look like all, but back True if even 1 value == True
