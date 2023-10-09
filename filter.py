df[ [True, False, True, False, True] ] #count this list must be == count rows in DF. It's back where value == your list
df[df['наличие авто']] #back true from DF
df[df['age'] <= 11] #back result
df[df['age'] <= 11 & df['наличие авто']] #most dificult value
df[(df['age'] == 11) | ~ df['наличие авто']] # ~ - its "not"
df.isin([53, 'Oleg']) #back bool DF where == our list
df['age'].isin([51,13,65,12]) #example
df[ df['age'].isin([51,13,65,12]) ] # back DF after filter
df.query('not 'columns' and age > 2') #if val not correct for Py need to use ``
n = 5
df.query('not 'columns' and age > 3 * @n') #example
