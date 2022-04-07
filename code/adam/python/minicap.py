# Mini-Capstone

fred_api_key = '9ecdd2a2979134a81e26c655968c4f54'

# import fredapi as fa
# import pandas as pd
# import matplotlib.pyplot as plt
# fred = fa.Fred(api_key = fred_api_key)

# gdp = fred.get_series('GDP')
# gdp.name = 'gdp'
# gdp.tail()

# payems = fred.get_series('PAYEMS')
# payems.name = 'payems'

# df = pd.merge(gdp, payems, left_index=True, right_index=True)
# print(df)
# print(type(df))




import pandas as pd
import pandas_datareader as pdr
import requests
import datetime
import matplotlib.pyplot as plt

start_year = int(input('Enter the start year: '))
start_month = int(input('Enter the start month (1-12): '))

end_year = 2022
end_month = 3

series = 'PAYEMS' #PAYEMS WPSFD4131

start = datetime.date (start_year, start_month, 1)
end = datetime.date (end_year, end_month, 1)
series = 'PAYEMS' #PAYEMS WPSFD4131
df = pdr.DataReader(series, 'fred', start, end)

print(df)
print(type(df))
df.plot()
plt.show()



