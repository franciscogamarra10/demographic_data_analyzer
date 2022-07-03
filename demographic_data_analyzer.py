import pandas as pd
import numpy as np
def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    # auxi1=df.query("  sex=='Male' ")
    average_age_men = df.query("  sex=='Male' ")['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = df.query("  education =='Bachelors' ")['education'].value_counts()/len(df)
    percentage_bachelors =percentage_bachelors[0]*100
  
    ww = df.query("  (education =='Bachelors' or  education == 'Masters' or education == 'Doctorate') ")['education']
    ww=ww.reset_index()

    ww2 = df.query("  (education =='Bachelors' or  education == 'Masters' or education == 'Doctorate') and salary =='>50K' ")['education']
  
    
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
  
    # What percentage of people without advanced education make more than 50K?
    higher_education =len(ww2)/len(ww)
  
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    
  
    lower_education = sum(df.query("  (education not in 'Bachelors') and  (education not in 'Masters') and (education not in 'Doctorate') ")['education'].value_counts()/len(df))

    # percentage with salary >50K
    higher_education_rich = len(ww2)/len(ww)*100
    ww3 = df.query("  (education not in 'Bachelors' and  education not in'Masters' and education not in 'Doctorate') ")['education']
    # ['Bachelors', 'HS-grad', '11th', 'Masters', '9th', 'Some-college',
    #    'Assoc-acdm', 'Assoc-voc', '7th-8th', 'Doctorate', 'Prof-school',
    #    '5th-6th', '10th', '1st-4th', 'Preschool', '12th']
    ww3=ww3.reset_index()

    ww4 = df.query("  (education not in 'Bachelors' and  education not in 'Masters' and education not in'Doctorate') and salary =='>50K' ")['education']
  
    lower_education_rich = len(ww4)/len(ww3)*100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    auxi= df[df['hours-per-week'] ==1]
    
    num_min_workers = auxi.value_counts()

    rich_percentage = auxi[auxi['salary'] =='>50K']['salary'].value_counts()/len(auxi)*100
    rich_percentage = float(rich_percentage)
    paises=df['native-country'].unique()
    pa2=[]
    Npa=[]
    for pa in paises:
    
      ind= sum(np.where(df['native-country']== pa,1,0))
      ind2= sum(np.where(df['native-country']==pa,np.where(df['salary']==">50K",1,0),0))
      pa2.append(pa)
    
      Npa.append(ind2/ind)
    # print(ind,ind2)
    
    max_item = max(Npa)
    
    # pa2[Npa.index(max_item)]
    # df3['index'][0]

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = pa2[Npa.index(max_item)]
    highest_earning_country_percentage = Npa[Npa.index(max_item)]*100

    # Identify the most popular occupation for those who earn >50K in India.
    df5=df.query("  salary =='>50K'  and `native-country` == 'India' ")['occupation'].value_counts()/len(df)
    
    top_IN_occupation = df5.index[0]

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
        'average_age_men': round(average_age_men,1),
        'percentage_bachelors': round(percentage_bachelors,1),
        'higher_education_rich': round(higher_education_rich,1),
        'lower_education_rich': round(lower_education_rich,1),
        'min_work_hours': min_work_hours,
        'rich_percentage': round(rich_percentage,1),
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        round(highest_earning_country_percentage,1),
        'top_IN_occupation': top_IN_occupation
    }

# val=calculate_demographic_data(print_data=True)
# print(type(val))