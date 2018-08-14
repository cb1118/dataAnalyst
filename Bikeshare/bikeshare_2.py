import time
import pandas as pd
import numpy as np
import calendar
import datetime

"""
USEFUL FUNCTIONS - REMOVE WHEN DONE
import pandas as pd
import datetime

filename = 'chicago.csv'
# load data file into a dataframe
df = pd.read_csv(filename)


print(df.head())  # start by viewing the first few rows of the dataset!

print(df.columns)
print(df.info())

print(df['Gender'].value_counts())
print(df['Gender'].unique())



# convert the Start Time column to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'])

# extract hour from the Start Time column to create an hour column
df['hour'] = df['Start Time'].dt.hour

print(df.head())

# find the most common hour (from 0 to 23)
popular_hour = df['hour'].value_counts().idxmax()
or
popular_hour = df['hour'].mode()[0]
    
print('Most Frequent Start Hour:', popular_hour)



# print value counts for each user type
user_types = df['User Type'].value_counts()

print(user_types)



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def load_data(city, month, day):
    Loads data for the specified city and filters by month and day if applicable.

#    Args:
#        (str) city - name of the city to analyze
#        (str) month - name of the month to filter by, or "all" to apply no month filter
#        (str) day - name of the day of week to filter by, or "all" to apply no day filter
#    Returns:
#        df - pandas DataFrame containing city data filtered by month and day
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    print(df.head())

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1    
        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]
        
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] ==  day.title()]
    
    return df
    
df = load_data('chicago', 'march', 'all')

print(df.head())
"""

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_input(valid_inputs, input_msg, incorrect_msg):
    """
    Handles collecting user inputs to avoid repetitious code.  Funciton will
    ask for input and validate it against the supplied list parameter.
    
    Returns:
        (str) entered_data to calling function
    """
    loop_count = 0
    entered_data = ""
    while entered_data not in valid_inputs:
        if loop_count == 1:
            input_msg = incorrect_msg + input_msg
        entered_data = input(input_msg)
        entered_data = entered_data.lower()
        loop_count += 1
    
    return entered_data

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    incorrect_data_msg = '\n*** Incorrect data entered ***\n'
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    enter_city_msg = "Please enter the name of the city to analyze (enter chicago, new york city or washington): "
    city = get_input(list(CITY_DATA), enter_city_msg, incorrect_data_msg)
    
    
    # get user input for month (all, january, february, ... , june)
    valid_months = ["january", "february", "march", "april", "may", "june","all"]
    enter_mth_msg = "Please enter the month to analyze (January - June) or All to select all months: "
    month = get_input(valid_months, enter_mth_msg, incorrect_data_msg)
    if month == "all":
        month = 0
    else:
        month = valid_months.index(month)+1

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = [element.lower() for element in list(calendar.day_name)]
    days.append("all")
    enter_day_msg = "Please enter the day of week to analyze (Sunday - Saturday) or All to select all days: "
    day = get_input(days, enter_day_msg, incorrect_data_msg)
 
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # Read city data for the city selected
    df = pd.read_csv(CITY_DATA[city])
    
    # Add column name to first column
    df.rename( columns={'Unnamed: 0':'TripID'}, inplace=True )

    # Convert Start Time field to a datetime data type
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Create month, day of week and hour elements for use in data gathering
    df['month'] = df['Start Time'].dt.month
    df['hour'] = df['Start Time'].dt.hour
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # Apply filters if necessary
    if month > 0:
        df = df.loc[df['month'] == month]
        
    if day != "all":
        df = df.loc[df['day_of_week'] == day.title()]
        
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].value_counts().idxmax()
    print("The most common month for travel: %s (%s)" % (common_month, calendar.month_name[common_month]))
    
    # display the most common day of week
    print("The most common day of the week to travel: %s" % (df['day_of_week'].value_counts().idxmax()))

    # display the most common start hour
    print("The most commnon hour to travel: %s" % (df['hour'].value_counts().idxmax()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used Start Station: %s" % (df['Start Station'].value_counts().idxmax()))

    # display most commonly used end station
    print("The most commonly used End Station: %s" % (df['End Station'].value_counts().idxmax()))


    # display most frequent combination of start station and end station trip
    combo_groupby = df.groupby(["Start Station","End Station"],as_index=False).count()
    combo_group = combo_groupby.loc[combo_groupby['TripID'].idxmax()]
    print("The most frequent combination of start and end stations: ")
    print("   Start Station: ", combo_group[0])
    print("   End Station: ", combo_group[1])
    print("   Number of Trips: ", combo_group[2])
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    trip_dur_sum = df["Trip Duration"].sum()
    print("A total of %s of time was spent traveling (%s)" % (trip_dur_sum, rollup_seconds(trip_dur_sum)))
 
    # display mean travel time
    trip_dur_mean = df["Trip Duration"].mean()
    print("The mean trip time was %s seconds (%s)" % (trip_dur_mean, rollup_seconds(trip_dur_mean)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def rollup_seconds(seconds):
    """
    rolls up seconds to minutes, hours, etc and returns str based response.
    provides readability in situations where the number of seconds is very large
    
    returns:
        (str) second_rollup_as_str
    """
    second_rollup_as_str = " "
    years = int(seconds / 31536000)
    if years > 0:
        seconds = seconds % 31536000
        second_rollup_as_str += str(years) + " years"
    days = int(seconds / 86400)
    if days > 0:
        seconds = seconds % 86400
        second_rollup_as_str += " " + str(days) + " days"
    hours = int(seconds / 3600)
    if hours > 0:
        seconds = seconds % 3600
        second_rollup_as_str += " " + str(hours) + " hours"
    minutes = int(seconds / 60)
    if minutes > 0:
        seconds = int(round(seconds % 60,0))
        second_rollup_as_str += " " + str(minutes) + " minutes"
    if seconds > 0:
        second_rollup_as_str += " " + str(seconds) + " seconds"
    second_rollup_as_str += " "
    
    return second_rollup_as_str


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Get the total number of rows in the data set for use later 
    total_rows = df.shape[0]


    # Display counts of user types
    print("Count of the number of trips by User Type:")
    if "User Type" in df.columns:
        user_type_counts=df['User Type'].value_counts()
        running_count = 0
        for l, v in user_type_counts.items():
            running_count += v
            print("    ",l.ljust(12), v)
            if running_count < total_rows:
                print("    ","Undefined:".ljust(12), total_rows - running_count)
    else:
        print("    User Type data not available in current data set")

    # Display counts of gender
    print("\nCount of the number of trips by Gender:")
    if "Gender" in df.columns:
        gender_counts=df['Gender'].value_counts()
        running_count = 0
        for l, v in gender_counts.items():
            running_count += v
            print("    ",l.ljust(12), v)
            if running_count < total_rows:
                print("    ","Undefined:".ljust(12), total_rows - running_count)
    else:
        print("    Gender data not available in current data set")
    
    # Display earliest, most recent, and most common year of birth
    print("\nBirth year data for riders:")
    if "Birth Year" in df.columns:
        print("    ","Earliest birth year of all riders: ",int(df["Birth Year"].min()))
        print("    ","\n    Most recent birth year of all riders: ", int(df["Birth Year"].max()))
        print("    ","Most popular birth year of all riders: ", int(df['Birth Year'].value_counts().idxmax()))
        """ Could also use this: 
        print(df['Birth Year'].mode()[0]) 
        to determine most popular birth year"""
    else:
        print("    ","Birth Year data not available in current data set")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
