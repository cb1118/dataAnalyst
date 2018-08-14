"""
bikeshare_data.py

Udacity Data Analyst NanoDegree Project
Completed on May 29, 2018

@author: Chris Bartsch
"""
import time
import pandas as pd
import numpy as np
import calendar
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

pd.set_option('display.width',250)

def get_input(valid_inputs, input_msg, incorrect_msg):
    """
    Handles collecting user inputs to avoid repetitious code.  Funciton will
    ask for input and validate it against the supplied list type parameter.
    
    Returns:
        (str) entered_data to calling function
    """
    loop_count = 0
    user_data = ""
    while user_data not in valid_inputs:
        if loop_count == 1:
            input_msg = incorrect_msg + input_msg
        user_data = input(input_msg)
        user_data = user_data.lower()
        loop_count += 1
    
    return user_data

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
    valid_months = ["all","january", "february", "march", "april", "may", "june"]
    enter_mth_msg = "Please enter the month to analyze (January - June) or All to select all months: "
    month = get_input(valid_months, enter_mth_msg, incorrect_data_msg)

    #convert month to integer for use in remaining data gathering
    month = valid_months.index(month)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    #create a list of days based on calendar package
    days = [element.lower() for element in list(calendar.day_name)]
    
    #add all to list as a valid selection.
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
    
    # Add column name to first column, may not be necessary but used in subsequent analysis
    df.rename( columns={'Unnamed: 0':'TripID'}, inplace=True )

    # Convert Start Time field to a datetime data type
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Create month, day of week and hour elements for use in data gathering
    df['month'] = df['Start Time'].dt.month
    df['hour'] = df['Start Time'].dt.hour
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # Apply filters if necessary
    # filter to month if all (month = 0) not selected
    if month > 0:
        df = df.loc[df['month'] == month]

    # filter to day if all not selected.        
    if day != "all":
        df = df.loc[df['day_of_week'] == day.title()]
        
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].value_counts().idxmax()
    print("The most common month for travel:          %s (%s)" % (common_month, calendar.month_name[common_month]))
    
    # display the most common day of week
    print("The most common day of the week to travel: %s" % (df['day_of_week'].value_counts().idxmax()))

    # display the most common start hour
    print("The most commnon hour to travel:           %s" % (df['hour'].value_counts().idxmax()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most commonly used Start Station:")
    print("    ","Station Name:".ljust(18), df["Start Station"].value_counts().idxmax())
    print("    ","Number of Trips:".ljust(18), df["Start Station"].value_counts().max())

    # display most commonly used end station
    print("\nThe most commonly used End Station:")
    print("    ","Station Name:".ljust(18), df["End Station"].value_counts().idxmax())
    print("    ","Number of Trips:".ljust(18), df["End Station"].value_counts().max())

    # display most frequent combination of start station and end station trip
    combo_groupby = df.groupby(["Start Station","End Station"],as_index=False).count()
    combo_group = combo_groupby.loc[combo_groupby['TripID'].idxmax()]
    print("\nThe most frequent combination of start and end stations: ")
    print("    ","Start Station:".ljust(18), combo_group[0])
    print("    ","End Station:".ljust(18), combo_group[1])
    print("    ","Number of Trips:".ljust(18), combo_group[2])
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
       Uses the rollup_seconds function to provide text based breadkdown of seconds 
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    trip_dur_sum = df["Trip Duration"].sum()
    print("A total of %s seconds of time was spent traveling" % (trip_dur_sum))
    print("    ","(%s)" % (rollup_seconds(trip_dur_sum)))
 
    # display mean travel time
    trip_dur_mean = int(round(df["Trip Duration"].mean(),0))
    print("The mean trip time was %s seconds" % (trip_dur_mean))
    print("    ","(%s)" % rollup_seconds(trip_dur_mean))


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


def user_stats(df,total_rows):
    """Displays statistics on bikeshare users.
    
    considered using " "*4 to print spaces but it did not save time or keystrokes
    The first 2 IF sections could be converted to a function, but seemed of limited value
    after this project.
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types *
    print("Count of the number of trips by User Type:")

    # Verify that User Type exists.
    if "User Type" in df.columns:
        user_type_counts=df['User Type'].value_counts()
        running_count = 0
        for label, value in user_type_counts.items():
            running_count += value
            print("    ",label.ljust(18), value)
        # Calculate and output an undefined row for rows with no values
        if running_count < total_rows:
            print("    ","Undefined:".ljust(18), total_rows - running_count)
    else:
        print("    ","User Type data not available in current data set")


    # Display counts of gender
    print("\nCount of the number of trips by Gender:")
    
    # Verify that Gender exists.
    if "Gender" in df.columns:
        gender_counts=df['Gender'].value_counts()
        running_count = 0
        for label, value in gender_counts.items():
            running_count += value
            print("    ",label.ljust(18), value)
        # Calculate and output an undefined row for rows with no values
        if running_count < total_rows:
            print("    ","Undefined:".ljust(18), total_rows - running_count)
    else:
        print("    ","Gender data not available in current data set")

    
    # Display earliest, most recent, and most common year of birth
    print("\nBirth year data for riders:")
    
    # Verify that Birth Year exists.
    if "Birth Year" in df.columns:
        print("    ","Earliest year:".ljust(18),int(df["Birth Year"].min()))
        print("    ","Most recent year:".ljust(18),int(df["Birth Year"].max()))
        print("    ","Most popular year:".ljust(18) ,int(df['Birth Year'].value_counts().idxmax()))
        # Could also use this: print(df['Birth Year'].mode()[0]) to determine most popular birth year"""
    else:
        print("    ","Birth Year data not available in current data set")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_raw_data(df, increment, total_rows):

    st_row = 0
    end_row = st_row + increment
    continue_ = "Z"
    view_raw = input("Would you like to see a few rows of raw data? (Y/N): ")
    if view_raw.upper() == "Y":
        x = input("\nFor readability it is preferable to use a wide viewing window.  Press <Enter> to continue...")
        while continue_.upper() != "X":
            
            if st_row == 0:
                valid_answers = ["N","X"]
                show_data_msg = "At start of File.  Enter (N)ext for next set of rows or e(X)it to quit "
            elif st_row + increment > total_rows-1:
                valid_answers = ["P","X"]
                show_data_msg = "EOF reached.  Enter (P)revious for previous rows or e(X)it to quit "
            else:
                valid_answers = ["N","P","X"]
                show_data_msg = "Enter (N)ext for next set of rows, (P)revious for previous rows or e(X)it to quit " 

            print(df[st_row:end_row])

            #make sure continue_ is not a valid answwer to avoid endless loop
            continue_ = "Z"
            
            while continue_.upper() not in valid_answers:
                continue_ = input(show_data_msg)

            if continue_.upper() == "N":
                st_row += increment
                if end_row + increment > total_rows -1:
                    end_row = total_rows 
                else:
                    end_row = st_row + increment
            if continue_.upper() == "P" and st_row > 0:
                st_row -= increment
                end_row = st_row + increment


def main():
    while True:

        city, month, day = get_filters()
        
        df = load_data(city, month, day)

        #Get the total number of rows in the data set for use in other functions
        total_rows = df.shape[0]

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, total_rows)
 
        #change 2nd argument to reflect how many data rows to see at a time.  
        #   Could build this as a user supplied input.
        show_raw_data(df, 5, total_rows)        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
