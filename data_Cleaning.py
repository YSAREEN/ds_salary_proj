import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')
df.head()

#cleaning things to do
#salary parsing
#company name text only
#state field and
#age of company
#parsing of job description (python etc)
#Salary parsing
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

#1. Remove the rows which have -1 as salary value
df = df[df['Salary Estimate'] != '-1']

#2. Salary Estimate Column remove the text - a. Can use Regex or lambda function to replace characters with blank values
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('K' ,'').replace('$',''))

#3. Clean salary data
min_hr = minus_kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

#4.Extract higher and lower salary values and find average
df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df['min_salary']+df['max_salary'])/2

#5.Remove rating from end of the company name if exits else don't
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating']<0 else x['Company Name'][:-4],axis=1)

#6. State Column
df['State'] = df['Location'].apply(lambda x:x.split(',')[1])
counts = df['State'].value_counts() #jobs in the each state
counts

#7.find the count of jobs in headquarters
df['same_state'] = df.apply(lambda x: 1 if x['Location'] == x['Headquarters'] else 0,axis=1)
df

#8.Age of Company
df['age'] = df['Founded'].apply(lambda x: x if x<1 else 2020 - x)
df

#9.parsing of JD for finding python,aws etc
df['python_ct']=df['Job Description'].apply(lambda x:1 if 'python' in x.lower() else 0)
python_ct = df['python_ct'].value_counts()

df['rstudio_ct']=df['Job Description'].apply(lambda x:1 if 'r-studio' in x.lower() or 'r studio' in x.lower() else 0)
rstudio_ct = df['rstudio_ct'].value_counts()

df['spark_ct']=df['Job Description'].apply(lambda x:1 if 'spark' in x.lower() else 0)
spark_ct= df['spark_ct'].value_counts()

df['aws_ct']=df['Job Description'].apply(lambda x:1 if 'aws' in x.lower() else 0)
aws_ct= df['aws_ct'].value_counts()

df['excel_ct']=df['Job Description'].apply(lambda x:1 if 'excel' in x.lower() else 0)
excel_ct= df['excel_ct'].value_counts()

#c= df.columns

#10. Drop the 1st column
df_final = df.drop(['Unnamed: 0'], axis=1)
df_final

df_final.to_csv('salary_cleaned_data.csv', index = False)

#pd.read_csv('salary_cleaned_data.csv')




