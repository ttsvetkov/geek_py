import pandas as pd 
import numpy as np 
import random
 
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data)

print('')

from sklearn. preprocessing import OneHotEncoder

encoder = OneHotEncoder(handle_unknown='ignore')
encoder_df = pd.DataFrame(encoder. fit_transform(data[['whoAmI']]). toarray ())

#merge
final_df = data.join (encoder_df)
final_df.drop('whoAmI', axis= 1 , inplace= True )
final_df.columns = ('Human', 'Robot')

print(final_df)
