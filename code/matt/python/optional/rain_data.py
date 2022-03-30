'''
PDX Code Guild - Class Koi
Optional Lab - Rain Data
Matt Walsh
'''


# Version 1

# https://or.water.usgs.gov/non-usgs/bes/vernon.rain##########################################

# import datetime module
from datetime import datetime, timedelta

# import urlopen to allow loading from internet
from urllib.request import urlopen

def load_data():
    """
    Loads data from URL and processes into dictionary
    """
    # display loading message
    print('Initializing')
    # assign url to variable for opening and concatenation
    base_url = 'https://or.water.usgs.gov/non-usgs/bes/'
    # load page holding all locations and data links
    locations_data_raw = urlopen(base_url)
    # convert to list of dicts and count number of locations
    location_count = 0
    location_master = []
    for locations_data_line in locations_data_raw:
        # convert each line to string for handling
        locations_data_line = str(locations_data_line)
        # look for urls in row, ignoring rover
        if '.rain' in locations_data_line and 'rover' not in locations_data_line:
            # create empty dictionary for each location
            location = {}
            # find and store url
            location['url'] = base_url + locations_data_line.split('"')[1]
            # strip raw name from url and store
            location['raw name'] = locations_data_line.split('"')[1][:-5]
            # append dictionary to list
            location_master.append(location)
            # increment counter
            location_count += 1
    # iterate through each location in dictionary and populate dictionary
    for i, each_location in enumerate(location_master):
        location_master[i] = load_each_location(each_location)
    # return complete dictionary
    return location_master

def load_each_location(data):
    """
    Loads each location and processes into dictionary
    """
    # show loading message
    print(f'Loading: {data["raw name"]}')
    # load location
    this_location = urlopen(data['url'])
    # create empty list to hold each line
    this_location_list = []
    # iterate through each line
    for line in this_location:
        # convert to string
        line = str(line)
        # strip extra characters
        line = line[2:-3]
        # append to list
        this_location_list.append(line)
    # hold split name as variable for un-normalized data
    if ' Rain Gage - ' in this_location_list[0]:
        split_at = 'Rain Gage - '
    elif ' Rain Gage, ' in this_location_list[0]:
        split_at = ' Rain Gage, '
    else:
        split_at = ' Rain Gage '
    # save name and address to dictionary
    data['name'] = this_location_list[0].split(split_at)[0]
    data['address'] = this_location_list[0].split(split_at)[1]
    # find start of data table
    row_above = this_location_list.index('-'*114)
    # create empty list to hold rain data
    data['rain data'] = []
    # iterate through rain data lines
    for line in this_location_list[row_above + 1:]:
        # split and strip whitespace
        line = line.split()
        # empty dictionary for each date
        this_date = {}
        # store date info
        date = datetime.strptime(line.pop(0), '%d-%b-%Y')
        this_date['year'] = date.year
        this_date['month'] = date.month
        this_date['day'] = date.day
        if len(line) > 0:
            print(f'line {line} -- len {len(line)}')
            this_date['daily'] = line.pop(0)
        if len(line) > 0:
            print(f'line {line} -- len {len(line)}')
            this_date['hourly'] = line
        data['rain data'].append(this_date)
    return data

def check_cache():
    """
    Checks cache to see if it has been updated within the last hour
    Returns True if an update is needed
    """
    # open and read file
    with open('code/matt/python/optional/rain_data.txt','r') as data_file:
        data_file = data_file.read()
        # return True if file is empty
        if data_file == '':
            return True
        # attempt to read timestamp at beginning of file
        try:
            # set current time and last updates to variables
            now = datetime.utcnow().timestamp()
            last_updated = float(data_file[:17])
            # assign elapsed time to variable
            time_since = now - last_updated
            # display time since last update and return True if an hour or more has passed
            if time_since > 3600:
                print(f'{time_since/60} minutes since updated. Updating now.')
                return True
            # return False if less than an hour has passed since last update
            else:
                return False
        # return True if unable to read timestamp
        except:
            print('An error has occurred. Updating cache.')
            return True



location_master = load_data()
print(location_master[0].keys())
# location_count = str(locations_data_raw).count('.rain')
# print(type(locations_data_raw))
# print(location_master)
# print(location_count)
""" 
# create empty list to hold all locations
locations_data = []

# iterate through all lines and convert to strings
for locations_data_line in locations_data_raw:
    locations_data_line = str(locations_data_line)
    # look for relative URL in lines and save
    if '.rain' in locations_data_line:
        rel_url = locations_data_line.split('"')[1]
        # load each location with loading message
        print(f'Loading: {rel_url[:-5]}')
        each_location = urlopen(base_url + rel_url)
        print(f'Finished: {rel_url[:-5]}')



        # print(line) """



'''
eachdict = {
    name: '',
    raw name: '',
    address: '',
    url: '',
    rain_data: [
        {
            year: '',
            month: '',
            day: '',
            daily: '', # sum of hourly
            hourly: [] # indices of 0-23, each holding raw data
        }
    ]
}


[-, missing data]
'''