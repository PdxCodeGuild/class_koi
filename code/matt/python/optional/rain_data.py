'''
PDX Code Guild - Class Koi
Optional Lab - Rain Data
Matt Walsh
'''


# Version 1

# import datetime module
from datetime import datetime

# import urlopen to allow loading from internet
from urllib.request import urlopen

def load_data():
    """
    Checks cache, loads data, and processes into dictionary
    """
    # string to place and find split points in cache file
    split_point = '\n\n$$SPLIT$$\n\n'
    # display loading message
    print('Initializing.')
    # check last cache update and rebuild if necessary
    if check_cache():
        build_cache(split_point)
    # open cache, split out section, split to list by line
    print('Reading cache: main')
    with open('code/matt/python/optional/rain_data.txt','r') as cache_file:
        cache_file = cache_file.read()
    locations_data_raw = cache_file.split(split_point)[1]
    locations_data_raw = locations_data_raw.split('\n')
    # assign base url to variable
    base_url = 'https://or.water.usgs.gov/non-usgs/bes/'
    # convert to list of dicts and count number of locations
    location_count = 0
    location_master = []
    # iterate through locations in locations_data_raw
    for locations_data_line in locations_data_raw:
        # ignore blank lines
        if locations_data_line != '':
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
        this_location = cache_file.split(split_point)[i + 2]
        location_master[i] = load_each_location(each_location, i, location_count, this_location)    
    # display completion message
    print('Loading complete!')
    # return complete list of dictionaries
    return location_master

def load_each_location(each_location, i, location_count, this_location):
    """
    Loads each location and processes into dictionary
    """
    # splits this_location into list and strip extra characters
    this_location_list = this_location.split("\n")
    for j, line in enumerate(this_location_list):
        this_location_list[j] = line[:-3]
    # show loading message
    print(f'Reading cache: {each_location["raw name"]} - {i + 1}/{location_count}')
    # hold split name as variable for un-normalized data
    if ' Rain Gage - ' in this_location_list[0]:
        split_at = 'Rain Gage - '
    elif ' Rain Gage, ' in this_location_list[0]:
        split_at = ' Rain Gage, '
    else:
        split_at = ' Rain Gage '
    # save name and address to dictionary
    each_location['name'] = this_location_list[0].split(split_at)[0]
    each_location['address'] = this_location_list[0].split(split_at)[1]
    # find start of data table
    row_above = this_location_list.index('-'*114)
    # create empty list to hold rain data
    each_location['rain data'] = []
    # iterate through rain data lines
    for line in this_location_list[row_above + 1:]:
        if line != '':
            # split and strip whitespace
            line = line.split()
            # empty dictionary for each date
            this_date = {}
            # store date info
            date = datetime.strptime(line.pop(0), '%d-%b-%Y')
            this_date['year'] = date.year
            this_date['month'] = date.month
            this_date['day'] = date.day
            # store daily total if not empty
            if len(line) > 0:
                this_date['daily'] = line.pop(0)
            # store hourly totals if not empty
            if len(line) > 0:
                this_date['hourly'] = line
            # add daily dictionary to rain data list
            each_location['rain data'].append(this_date)
    return each_location

def check_cache():
    """
    Checks cache to see if it has been updated within the last hour
    Returns True if an update is needed
    """
    # open and read cache file
    with open('code/matt/python/optional/rain_data.txt','r') as cache_file:
        print('Checking cache.')
        cache_file = cache_file.read()
        # return True if file is empty
        if cache_file == '':
            print('Cache empty. Updating now.')
            return True
        # attempt to read timestamp at beginning of file
        try:
            # set current time and last updates to variables
            now = datetime.utcnow().timestamp()
            last_updated = float(cache_file[:17])
            # assign elapsed time to variable
            time_since = int(now - last_updated)
            # display time since last update and return True if an hour or more has passed
            if time_since > 3600:
                print(f'{time_since/60} minutes since cache update. Updating now.')
                return True
            # return False if less than an hour has passed since last update
            else:
                print('Cache valid and recent. Proceeding without update.')
                return False
        # return True if unable to read timestamp
        except:
            print('An error has occurred. Updating cache.')
            return True

def build_cache(split_point):
    """
    Builds cache file
    """
    # display loading message
    print('Building cache: main')
    # assign url to variable for opening and concatenation
    base_url = 'https://or.water.usgs.gov/non-usgs/bes/'
    # open cache file for writing
    with open('code/matt/python/optional/rain_data.txt','w') as cache_file:
        # add timestamp to beginning of cache and insert split_point
        cache_file.write(str(datetime.utcnow().timestamp()))
        cache_file.write(split_point)
        # load page holding all locations
        locations_data_raw = urlopen(base_url)
        # int variable to count locations and empty list to hold urls
        location_count = 0
        location_urls = []
        for locations_data_line in locations_data_raw:
            # convert each line to string for handling
            locations_data_line = str(locations_data_line)
            # look for urls in row, ignoring rover
            if '.rain' in locations_data_line and 'rover' not in locations_data_line:
                # write each line to cache
                cache_file.write(locations_data_line[2:])
                cache_file.write('\n')
                # find and store url
                location_url = base_url + locations_data_line.split('"')[1]
                # append dictionary to list
                location_urls.append(location_url)
                # increment counter
                location_count += 1
        # insert split point after main page writted to cache
        cache_file.write(split_point)
        # iterate through each location in dictionary and write to cache
        for i, _ in enumerate(location_urls):
            # display loading message
            print(f'Building cache: {location_urls[i][39:-5]} - {i + 1}/{location_count}')
            # load location
            this_location = urlopen(location_urls[i])
            # iterate through each line and write to cache
            for this_location_line in this_location:
                this_location_line = str(this_location_line)
                cache_file.write(this_location_line[2:])
                cache_file.write('\n')
            # add split point after each except last
            if i + 1 != location_count:
                cache_file.write(split_point)
    # display completion message
    print('Cache complete.')
    


# build_cache('\n\n$$SPLIT$$\n\n')
location_master = load_data()
# print(location_master[0].keys())
# location_count = str(locations_data_raw).count('.rain')
# print(type(locations_data_raw))
print(location_master[0]['name'])
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