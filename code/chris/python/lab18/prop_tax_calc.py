'''
Real Estate Property Tax Calculator
- This will open the CSV file returned by 
  re_data_pull.py, and gather the "Total Net Taxable Value"
  for the most recent year.
'''
from re_data_pull import data_pull
from re_data_pull import value_cleanup
from re_data_pull import tax_calc
import csv

search_year = input('What year would you like info for (ex: 2015)? ')

while True:
    user_address = input('Enter the address or "done": ')
    if user_address == 'done':
        break
    else:
        data_pull(user_address)

        with open('property_tax_info.csv', newline='') as csvfile:
            taxreader = csv.DictReader(csvfile)
            for row in taxreader:
                if row['Assessment Year'] == search_year:
                    print(row['Assessment Year'], ' Taxable Value: ', row['Total Net Taxable Value'])
                    taxable_amount = row['Total Net Taxable Value']
                    
                    tax_calc_float = value_cleanup(taxable_amount)
                    property_taxes = tax_calc(tax_calc_float)

                    print(f"Property Taxes: ${property_taxes}")
