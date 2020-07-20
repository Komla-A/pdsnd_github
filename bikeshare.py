import time
import pandas as pd
import numpy as np
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("What city would you like data for? (Chicago, New York City, Washington)\n--> ").lower()
        if city not in (CITY_DATA.keys()):
           print('Please choose one of the following cities: Chicago, New York City, or Washington.')
           continue
        else:
           break
    # TO DO: get user input for month (all, january, february, ... , june) 
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month_user =  input("Type a month for a specific time frame of data. For all months type 'all'\n--> ").lower()
        print("Specifically select months between January and June")
        if month_user not in months:
            print("Specifically select months between January and June")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day_user = input("Type a day of the week for a specific time frame of data. For all days of the week type 'all'\n-->").lower()
        if day_user not in days:
            print("Display a day of the week. For all days, display 'all'.")
            continue
        else:
            break
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
    df = pd.read_csv(CITY_DATA[city])
    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time']= pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    df['month']= df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print("The most common month of travel was {}.\n".format(common_month))
      
    # TO DO: display the most common day of week
    df['day']= df['Start Time'].dt.weekday_name
    common_day = df['day'].mode()[0]
    print("The most common day of travel was {}.\n".format(common_day))
    # TO DO: display the most common start hour
    
    df['hour']= df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    return
    print("The most common hour of travel is at {}.\n".format(common_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    common_start = df['Start Station'].size().nlargest(1)
    print("The most commonly used starting station was {}.\n".format(common_start))
    # TO DO: display most commonly used end station
    common_end = df['End Station'].size().nlargest(1)
      
    print("The most commonly used ending station was {}.\n".format(common_end))
    # TO DO: display most frequent combination of start station and end station trip
    se_combined = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print("The most frequently used start to end stations combined was {}.\n".format(se_combined))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    
    total_travel = df['Trip Duration'].sum()
    # TO DO: display mean travel time
    
    average_travel = df['Trip Duration'].mean()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    
    if 'User Type' in df.columns:
        user_types = df['User Type'].value_counts()
        print("The user type counts are: {}\n".format(user_types))
    # TO DO: Display counts of gender
    
        gender_counts = df['Gender'].value_counts()
        print("The gender type counts are: {}\n".format(gender_counts))
    else:
        print("Sorry. Data unavailable!")
    # TO DO: Display earliest, most recent, and most common year of birth
   
    earliest = min(df['Birth Year'])
    most_recent = max(df['Birth Year'])
    most_common = df['Birth Year'].mode
    print("The earliest year of birth was {}.\n".format(earliest))
    print("The most recent year of birth was {}.\n".format(most_recent))
    print("The most common year of birth was {}.\n".format(most_common))
    #except:
    print("Sorry. Data unavailable!")
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
        #"Hello! Let\'s explore some US bikeshare data!"
        #request user input
        #"Which city would you like to explore?"
        #"Which month?"
        #"Which day of the week?"
        #prints
        # descriptive statistics (as per the Project details page ) based on the users input
        #request user input (for raw data display)
        #request user input (for raw data display)
        value = input("Do you want to display five records of data").lower()
        if value.lower() == 'yes':
            df.sample(5)
            continue
        else:
            break
       # request user input
        #Would you like to restart? Enter yes or no. If no, then exit
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()