import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = ["ALL","JANUARY","FEBRUARY","MARCH","APRIL","MAY","JUNE"]
DAY_OF_THE_WEEK_DATA =["ALL","MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]

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
    invalid_city = True
    while True:
        city = input("Please choose chicago,new york city or washington to analyze: ")
        if city.lower() in CITY_DATA:
            break



    # get user input for month (all, january, february, ... , june)
    invalid_month = True
    while invalid_month:
        month = input("Please choose the month to filter or select all: ")
        if month.upper() in MONTH_DATA:
            invalid_month = False
        else:
            invalid_month = True

    # get user input for day of week (all, monday, tuesday, ... sunday)
    invalid_day = True
    while invalid_day:
        day = input("Enter day of the week or select all: ")
        if day.upper() in DAY_OF_THE_WEEK_DATA:
            invalid_day = False
        else:
            invalid_day = True

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
    df = pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()

    if month.upper() != 'ALL':
        month_index = MONTH_DATA.index(month.upper())
        df = df[df['month'] == month_index]


    if day.upper() != 'ALL':
        day_index = DAY_OF_THE_WEEK_DATA.index(day.upper())
        df = df[df['day'] == day.title()]


    return df


def time_stats(df):
    """Statistical display of the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print("most common month: ",most_common_month)


    # display the most common day of week
    most_common_day = df['day'].mode()[0]
    print("most common day of week: ",most_common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("most common start hour: ",df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("most commonly used start station: ",df['Start Station'].mode()[0])

    # display most commonly used end station
    print("most commonly used end station: ",df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    print("most frequent combination of the stations: ",df.groupby(['Start Station','End Station']).size().idxmax())
    # print("most frequent combination of the stations: ",df.groupby(['Start Station','End Station']).count().sort_values(by=['Start Station','End Station'],axis = 0).iloc(0))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("total travel time: ",df['Trip Duration'].sum())

    # display mean travel time
    print("mean travel time: ",df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("User Types: ",df['User Type'].value_counts())

    # Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
    except Exception as e:
        gender_counts = "NA"

    # print("Gender count: ",df['Gender'].value_counts())
    print("Gender count: ",gender_counts)

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_year_birth = df['Birth Year'].min()
    except Exception as e:
        earliest_year_birth = "NA"

    print("Earliest year of birth: ",earliest_year_birth)

    try:
        recent_year_birth = df['Birth Year'].max()
    except Exception as e:
        recent_year_birth = "NA"

    print("Recent year of birth: ",recent_year_birth)

    try:
        most_common_birth_year = df['Birth year'].mode()[0]
    except Exception as e:
        most_common_birth_year = "NA"

    print("Most common year of birth: ",most_common_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    print(df)
    view_data = input('\n Do you want to see first 5 rows of data? Enter yes or no.\n')
    if view_data.lower() == 'yes':
        start_loc = 0
        while True:
            try:
                print(df.iloc[start_loc:start_loc + 5])
            except Exception as e:
                break
            start_loc += 5
            view_display = input('\nDo you wish to continue?:Enter yes or no.\n')
            if view_display.lower() == 'no':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
