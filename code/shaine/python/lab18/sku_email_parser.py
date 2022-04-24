#  *'-.-'*'-.-'*'-.-'*'--'*
#     Project: Python 
#   Lab 18: Mini Capstone 
#       Version: 1.0
#   Author: Shaine Warren
#   Email: mwarren86@gmail.com
#       Date: April, 2022
# *'-.-'*'-.-'*'-.-'*'--'*

# pip istalled EZGmail interface to easily work with Google API
#pip installed google api 


import ezgmail
import re
import csv
import ezsheets
from tkinter import *

def parser():

    unreadThreads = ezgmail.unread() # List of GmailThread objects.

    # Tuples of all parsed data
    output_list = []

    for i in range (len(unreadThreads)):

    # parses out the update reason from the subject line
        header = unreadThreads[i].messages[0].subject
        header_split = header.split(' - ')
        subj = header_split[1]
        date = header_split[2]

    # parses the sku numbers from the email body
        body = unreadThreads[i].messages[0].body
        sku_pattern = "(SWMP[0-9]{4,10})"
        sku_find = re.findall(sku_pattern, body)

    # adds all of the parsed data as a tuple to output_list
        for sku in sku_find:
            input = (subj, sku, date)
            output_list.append(input)

    # creates csv of all the SKUs
    with open('sku-updates.csv','w') as f:
        writer = csv.writer(f)
        writer.writerow(['Reason', 'SKU', 'Date'])
        writer.writerows(output_list)

    # uploads the csv to Google Sheets
    ezsheets.upload('sku-updates.csv')

    # Displays "Done" in the GUI window
    feedback = Label(window, text='Done')
    feedback.pack()

    return 

# GUI window
window = Tk()
window.title('Inventory Update Email Parser')
main_button = Button(window, text='Click to Start',command=parser)
main_button.pack()

window.mainloop()