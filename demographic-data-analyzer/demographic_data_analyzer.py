import pandas as pd 
def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    x=df['age'].where(df['sex']=='Male')

    average_age_men =x.mean().__round__(1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors=df['education'].where(df['education']=='Bachelors')
    y=len(bachelors.dropna())
    per=y/(len(df)+1)*100
    percentage_bachelors=per.__round__(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
                
    education=df[['education','salary']].replace(['Masters','Bachelors','Doctorate'],'Advanced')
    advanced=education.where(education['education']=='Advanced')
    advanced=advanced.dropna()
    higher_education=(len(advanced)/len(df)).__round__(1)
    x=advanced['salary'].value_counts()['>50K']
    per1=x/(len(advanced)+1)*100
    higher_education_rich=per1.round(1)
    lower_education=1-higher_education
    na=education.where(education['education']!='Advanced')
    na=na.dropna()
    x=na['salary'].value_counts()['>50K']
    per2=x/(len(na)+1)*100
    lower_education_rich = per2.__round__(1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours =df['hours-per-week'].min()
    lazy=df[['hours-per-week','salary']].where(df['hours-per-week']==1)
    lazy=lazy.dropna()
    num_min_workers=len(lazy)
    rich_percentage=(lazy['salary'].value_counts()['>50K'])/num_min_workers*100
    rich_percentage=int(rich_percentage)
    nation=df[['native-country','salary']].where(df['salary']=='>50K')
    nation=nation['native-country'].dropna()
    nation_salary=nation.value_counts()
    nation_salary
    nations=df['native-country']
    nations=nations.value_counts()
    wanted_list=nation_salary/nations
    highest_earning_country_percentage=(wanted_list.max()*100).__round__(1)
    highest_earning_country=wanted_list.idxmax()
    india=df[['salary','native-country','occupation']].where(df['native-country']=='India')
    india=india.dropna()
    india=india.where(india['salary']=='>50K')
    india=india.dropna()
    india=india["occupation"]
    top_IN_occupation=india.value_counts().idxmax()
    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
