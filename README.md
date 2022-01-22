# Processing-data-with-python

#Creating a Pandas DataFrame

```
import pandas as pd
#creating canned data
data = {'Week':pd.Series(['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'])
 ,'Snowfall':pd.Series(['3.5','0.1','1.00','0','4.6','1.0','0.2'])}
#Reading from a dataframe
dfcanned = pd.DataFrame(data)
print("Amount of Snowfall (in) each day of the week: \n",dfcanned)
```
