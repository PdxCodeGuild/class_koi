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
# from IPython.display import display
# import plotly.express as px
import matplotlib.pyplot as plt

start_year = 2020
start_month = 5

end_year = 2022
end_month = 6

start = datetime.date (start_year, start_month, 1)
end = datetime.date (end_year, end_month, 1)
series = 'PAYEMS' #PAYEMS WPSFD4131
df = pdr.DataReader(series, 'fred', start, end)

print(df)
# display(df)
print(type(df))
df.plot()
plt.show()

# start_date = "2020-01-1"
# end_date = "2020-12-31"
# data = web.DataReader(name="TSLA", data_source='yahoo', start=start_date, end=end_date)
# print(data)



# fig = px.line(df, y='PAYEMS',
#               title='Total Nonfarm Payrolls 2005-2020',
#               labels={'PAYEMS':'All Nonfarm Employees'})

# fig.show()

# category_id = '125'
# response = requests.get('https://api.stlouisfed.org/fred/category?category_id='+category_id+'&api_key=' + fred_api_key + '&file_type=json')
# fred_data = response.json()
# # print(fred_data)

# display(df)