import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Hypothesis: Because Developed country has better medical treatment, they will have less infant_deaths due to HIV/AIDS targeted before year 2010.
df = pd.read_csv('C:/Users/sd529/OneDrive/Desktop/Data_analysis/Life_Expectancy_Data.csv')

data = pd.DataFrame(df,columns=['Country','Status','Year','infant_deaths','HIV/AIDS','Population'])
#print(data)
#print(data['Status'])

developed = data[(data['Status'] == 'Developed')]
developing = data[(data['Status'] == 'Developing')]
#print(developed)
sorted_developed = developed.sort_values(by='infant_deaths', ascending=False)
sorted_developing = developing.sort_values(by='infant_deaths',ascending=False)

#print(sorted_developed)
# print(sorted_developing.head(20))
#print(sorted_developed.head(20))


"""
both developed and developing countries have similar population range but has significant difference in infant_deaths. the goal is to research through 
the main factor affecting the infant deaths between the developed and developing countires. Because all 3 countries had very low HIV rate, it cannot be the factor to compare 
the difference.
"""

# filtering only Afghanistan population more than 20 million since the population provided in the dataset is wrong on some years.
Afghan_filtered = data[(data['Country'] == 'Afghanistan')&(data['Population'] > 20000000)]
#print(Afghan_filtered)

# romania and Australia tends to be suitable countries to compare to Afghanistan as candidates for developed countries
developed_more = data[(data['Status'] == 'Developed')&(data['Population'] > 20000000)]
#print(developed_more)

# filtering only Romania and Australia population more than 20 million.
Auro_filtered = data[(data['Status'] == 'Developed')&(data['Population'].between(20000000,30000000))]
#print(Auro_filtered)

dev = data[data['Status'] == 'Developed']
sorted_dev_byHIV = dev.sort_values(by='HIV/AIDS', ascending=True)
# print(sorted_dev_byHIV)

"""
Next question will be the comparison between multiple developing countries and find out why some developing country has significantly less infant deaths than others.
Looking into multiple factors like, HIV, Hepatitis_B, Measles, Diphtheria and Polio will be necessary.
"""

range_20million_developing = data[(data['Status'] == 'Developing')&(data['Population'].between(10000000,20000000))]

# Nigeria has the highest infant deaths with highest HIV/AIDS rate below 20million population.
highest_death_developing = range_20million_developing.sort_values(by='infant_deaths',ascending=False)
# Chile & Greece had lowest infant deaths with lowest HIV/AID rate below 20million population.
Lowest_death_developing = range_20million_developing.sort_values(by='infant_deaths',ascending=True)

# Attempting to look for similar HIV/AIDS rates with singifincant difference in infant deaths.

sim_HIV= data[(data['Status'] == 'Developing')&(data['Population'].between(10000000,30000000))&(data['HIV/AIDS'].between(1,3))]


# creating another data frame to include more factors like measles and hepatitis B

New_data = pd.DataFrame(df,columns=['Country','Status','Year','infant_deaths','HIV/AIDS','Hepatitis_B','Measles ','Polio','Population'])
New_data_ranged = New_data[(New_data['Status'] == 'Developing')&(New_data['Population'].between(10000000,20000000))&(New_data['Country'] != 'India')]
# print(highest_death_developing)
# print(Lowest_death_developing)
# print(sim_HIV)


new_highest_death_developing = New_data_ranged.sort_values(by='infant_deaths',ascending=False)
# Chile & Greece had lowest infant deaths with lowest HIV/AID rate below 20 million population.
new_lowest_death_developing = New_data_ranged.sort_values(by='infant_deaths',ascending=True)

# print(new_highest_death_developing.head(30))
# print(new_highest_death_developing)

# from this sorted data, we notice that the number of measles don't have significant changes in infant deaths.
highest_measles = New_data_ranged.sort_values(by='Measles ',ascending=False)
lowest_measles = New_data_ranged.sort_values(by='Measles ',ascending=True)

high1 = highest_measles.head(20)

# print(high1)

measles_values = high1.loc[:,'Measles '].to_list()
infant_values = high1.loc[:,'infant_deaths'].to_list()
HIV_AIDS_values = high1.loc[:,'HIV/AIDS'].to_list()

"""
Graph representing the comparison between the measles and infant deaths

plt.plot(measles_values,infant_values)
plt.xlabel("Number of Measles")
plt.ylabel("Number of Infant Deaths")
plt.show()

"""

"""
new_highest_death_developing.plot(x='Year',y=['infant_deaths','HIV/AIDS'])
plt.show()
"""


# print(infant_values)
#print(infant_deaths)
# high1.plot('Measles','infant_deaths')

# Nigeria only:

nigeria_data = pd.DataFrame(df,columns=['Country','Status','Year','infant_deaths','HIV/AIDS','Hepatitis_B','Measles ','Polio','Population','GDP'])
nigeria_data_ranged = nigeria_data[(nigeria_data['Country'] != 'India')&(nigeria_data['Country'] == 'Nigeria')]

# print(nigeria_data_ranged)


# new_infant_HIV_only = pd.DataFrame(nigeria_data_ranged,columns=['infant_deaths','HIV/AIDS'],index = ['Year'])


Nigeria_death = nigeria_data_ranged.sort_values(by='infant_deaths',ascending=False)
# print(Nigeria_death)


nigeria_infant = Nigeria_death.loc[:,'infant_deaths'].to_list()
nigeria_HIV = Nigeria_death.loc[:,'HIV/AIDS'].to_list()
nigeria_year = Nigeria_death.loc[:,'Year'].to_list()

# print(nigeria_year)

# this graph shows the decrease in infant deaths over the years:
"""
plt.plot(nigeria_year,nigeria_infant)
plt.xlabel('Nigeria_Year')
plt.ylabel('Number of nigeria infant deaths')
plt.show()
"""
# this graph shows the decrease in HIV rate over the years:
"""
plt.plot(nigeria_year,nigeria_HIV)
plt.xlabel('Nigeria_Year')
plt.ylabel('HIV/AIDS Rate')
plt.show()

"""
# this shows the constant decrease rate in HIV and infants over the years
"""
plt.plot(nigeria_year,pct_infant,pct_hiv)
plt.xlabel("nigeria_Year")
plt.ylabel("percent change")
plt.show()
"""



New_data = pd.DataFrame(df,columns=['Country','Status','Year','infant_deaths','HIV/AIDS','Hepatitis_B','Measles ','Polio','Population','Diphtheria ','thinness_1-19 years','GDP'])
Developed_cnt = New_data[(New_data['Status'] == 'Developed')&(data['Population'].between(10000000,30000000))]
Developing_cnt = New_data[(New_data['Status'] == 'Developing')&(New_data['Country'] != 'India')&(data['Population'].between(10000000,30000000))]

GDP_lowtohigh_developing = Developing_cnt.sort_values(by = ['GDP'], ascending=[True])

GDP_hightolow_developing = Developing_cnt.sort_values(by = ['GDP'], ascending=[False])

GDP_developed = Developed_cnt.sort_values(by = ['GDP'], ascending=[True])


# print(GDP_developing.head(20))
print(GDP_hightolow_developing.head(20))
