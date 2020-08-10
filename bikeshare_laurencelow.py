import time
import pandas as pd
import numpy as np
import sys
import os

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    
    while True:
        city = input("Would you like to see data from Chicago, New York City or Washington?").lower()
        #handling unexpected inputs#
        if city in CITY_DATA.keys():
            print(' --> Your chosen city is', city.title(), '\n')
            break
        else:
            print('\nAttention!the city you inserted is not in the list. Please choose among chicago, New York or Washington')
            print('Do you want to try again or exit the program?')
            ter = input('To continue press C, to exit press E: ').lower()
            if ter == 'e':
                print('\n Thank you for using Bikeshare project. Bye!')
                sys.exit()
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input('Which month? January. February, March, April, May or June? Please type out the full month name.').lower()
        print('Just one moment. Loading the data.')
        if month in months [0:5]:
            print('your chosen month is', month.title(),'\n')
            break
        else:
            print('\nAttention! Your chosen month is incorrect.')
            print('Do you want to try again or exit the program?')
            ter = input('To continue press C, to exit press E: ').lower()
            if ter == 'e':
                sys.exit()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days_weeks = days_weeks = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    while True:
        day = input('Which day? Please type a day Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday?').lower()
        print('Just one moment. Loading the data.')
        if day in days_weeks [0:6]:
            print('-->>Your chosen day is', day.title(), '\n')
            break        
        else:
            print('\nAttention! Your chosen day is incorrect.')
            print('Do you want to try again or exit the program?')
            ter = input('To continue press C, to exit press E: ').lower()
            if ter == 'e':
                sys.exit()


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])


    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        days_weeks = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday',
                      'saturday', 'sunday']
        day = days_weeks.index(day.lower())
        df = df[df['day_of_week'] == day]

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    return df


def time_stats(df, month, day, city):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    days_weeks = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday',
                  'saturday', 'sunday']

    # display the most common month
    if month != 'all':
        print('\nFor the chosen month {} '.format(month.title()))
    else:
        month_common = df['month'].moode()[0]
        print('the most common month is {}'.format(months[month_common -1].title()))
    # display the most common day of week
    if day != "all":
        print('For the chose dat of the week {}'.format(day.title()))
    else:
        day_common = df['day_of_week'].mode()[0]
        print('The most common days is {}'.format(days_weeks[day_common].title()))

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("-->>The most common start hour is: {}".format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("-->>The most commonly used start station is: {}".format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print("-->>The most commonly used end station is: {}".format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    start_end_station = 'Start station: ' + df['Start Station'] + '; End station: ' + df['End Station']
    print('-->>The most common combination of start station and end station trip:\
     \n', start_end_station.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Duration'] = df['End Time'] - df['Start Time']
    print('-->>The total travel time is {}'.format(df['Duration'].sum()))

    # TO DO: display mean travel time
    print('-->>The mean travel time is {}'.format(df['Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("\n -->>Counts of user type:\n{}".format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print("\n-->Counts of gender:\n{}".format(df['Gender'].value_counts()))
    else:
        print('\n-->>Gender data is not available for {}\n'.format(city))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("\n-->>The earliest year of birth: {}".format(df['Birth Year'].min()))
        print("-->>The recent year of birth: {}".format(df['Birth Year'].max()))
        print("-->>The most common year of birth: {}\n".format(df['Birth Year'].mode()[0]))
    else:
        print('\nGender data is not available for {}\n'.format(city))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def first_row(city):
    df = pd.read_csv(CITY_DATA[city])
    show_raw_data = input('Do you want to see the first 5 rows of raw data? Please type yes or no: ').lower()
    if show_raw_data == 'yes':
        number_rows =  len(df.index)
        i = int(input('Please, enter the row number you want to see the data from: '))
        while show_raw_data == 'yes':
            print(df.iloc[i:i+5, :])
            i+=5
            #check for the end of data set
            if i >= number_rows:
                print('-->>The end of data set is reached.\n')
                break
            show_raw_data = input('To see the next 5 rows type in "yes" otherwise "no" ').lower()
            if show_raw_data == 'no':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, month, day, city)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        first_row(city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
