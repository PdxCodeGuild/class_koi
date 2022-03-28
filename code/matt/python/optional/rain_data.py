'''
PDX Code Guild - Class Koi
Optional Lab - Rain Data
Matt Walsh
'''


# Version 1

# https://or.water.usgs.gov/non-usgs/bes/vernon.rain##########################################

# import urlopen to allow loading from internet
from urllib.request import urlopen

def load_data():
    """
    Loads data from URL and processes into dictionary
    """
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
            location['raw_name'] = locations_data_line.split('"')[1][:-5]
            # append dictionary to list
            location_master.append(location)
            # increment counter
            location_count += 1
    # iterate through each location in dictionary and populate dictionary
    # for each_location in location_master:
    #     load_each_location(each_location['url'])

    return location_master

def load_each_location(data):
    """
    Loads each location and processes into dictionary
    """
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
    # save name and address to dictionary
    data['name'] = this_location_list[0].split(' - ')[0]
    data['address'] = this_location_list[0].split(' - ')[1]
    # find start of data table
    row_above = this_location_list.index('-'*114)
    # create empty list to hold rain data

    
# ------------------------------------------------------------------------------------------------------------------
    print(this_location_list[:30])#######################
    print(data)
    print(f'row above {row_above}')
    pass


load_each_location({'url': 'https://or.water.usgs.gov/non-usgs/bes/cottrell_school.rain', 'raw_name': 'cottrell_school'})

# location_master = load_data()
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
    address: '',
    url: '',
    rain_data: [
        {
            date: '',
            daily: '', # sum of hourly
            hourly: [] # indices of 0-23, each holding raw data
        }
    ]
}


[-, missing data]
'''