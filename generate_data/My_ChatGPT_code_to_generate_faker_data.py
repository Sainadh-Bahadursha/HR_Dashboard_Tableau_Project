# Code obtained from ChatGPT using given prompt from Data with Baraa
# Find the prompt in "Chat_gpt_prompt_to_create_Faker_data.txt" file

import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta

# Initialize the Faker library to generate random names and dates
fake = Faker()

# Constants and probabilities
GENDER_PROB = [0.46, 0.54]  # Probability distribution for genders
GENDERS = ['Female', 'Male']
YEARS = list(range(2015, 2025))  # Years from 2015 to 2024
YEAR_PROB = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]  # Equal probability for each year
DEPARTMENTS = ['HR', 'IT', 'Finance', 'Sales', 'Marketing']
DEPARTMENT_PROB = [0.15, 0.25, 0.2, 0.2, 0.2]  # Probability distribution for departments

# Job titles and their probabilities within each department
JOB_TITLES = {
    'HR': ['HR Manager', 'HR Assistant'],
    'IT': ['Developer', 'System Admin', 'IT Support'],
    'Finance': ['Accountant', 'Financial Analyst'],
    'Sales': ['Sales Manager', 'Sales Representative'],
    'Marketing': ['Marketing Manager', 'Marketing Specialist']
}
JOB_TITLE_PROB = {
    'HR': [0.4, 0.6],
    'IT': [0.5, 0.3, 0.2],
    'Finance': [0.6, 0.4],
    'Sales': [0.4, 0.6],
    'Marketing': [0.5, 0.5]
}

# Education levels required for each job title
EDUCATION_LEVELS = {
    'HR Manager': 'Bachelor\'s Degree',
    'HR Assistant': 'Associate Degree',
    'Developer': 'Bachelor\'s Degree',
    'System Admin': 'Bachelor\'s Degree',
    'IT Support': 'Associate Degree',
    'Accountant': 'Bachelor\'s Degree',
    'Financial Analyst': 'Master\'s Degree',
    'Sales Manager': 'Bachelor\'s Degree',
    'Sales Representative': 'High School Diploma',
    'Marketing Manager': 'Bachelor\'s Degree',
    'Marketing Specialist': 'Associate Degree'
}

# Performance ratings and their probabilities
PERFORMANCE_RATINGS = ['Excellent', 'Good', 'Satisfactory', 'Needs Improvement']
PERFORMANCE_PROB = [0.2, 0.4, 0.3, 0.1]  # Probability distribution for performance ratings
OVERTIME_PROB = [0.3, 0.7]  # Probability distribution for overtime (Yes/No)

# Salary ranges for each job title
SALARY_RANGES = {
    'HR Manager': (60000, 90000),
    'HR Assistant': (35000, 50000),
    'Developer': (70000, 120000),
    'System Admin': (50000, 80000),
    'IT Support': (40000, 60000),
    'Accountant': (60000, 85000),
    'Financial Analyst': (65000, 90000),
    'Sales Manager': (70000, 100000),
    'Sales Representative': (30000, 60000),
    'Marketing Manager': (65000, 95000),
    'Marketing Specialist': (40000, 65000)
}

# States and cities mapping
STATES_CITIES = {
    'CA': ['Los Angeles', 'San Francisco', 'San Diego'],
    'NY': ['New York', 'Buffalo', 'Rochester'],
    'TX': ['Houston', 'Dallas', 'Austin'],
    'FL': ['Miami', 'Orlando', 'Tampa'],
    'IL': ['Chicago', 'Springfield', 'Naperville']
}

# Helper functions
def generate_employee_id(index):
    return f"E{index:05d}"  # Generate a unique employee ID

def choose_gender():
    return np.random.choice(GENDERS, p=GENDER_PROB)  # Randomly choose gender based on probabilities

def choose_state_city():
    state = random.choice(list(STATES_CITIES.keys()))  # Randomly choose a state
    city = random.choice(STATES_CITIES[state])  # Randomly choose a city within the chosen state
    return state, city

def choose_department():
    return np.random.choice(DEPARTMENTS, p=DEPARTMENT_PROB)  # Randomly choose a department based on probabilities

def choose_job_title(department):
    return np.random.choice(JOB_TITLES[department], p=JOB_TITLE_PROB[department])  # Randomly choose a job title within the chosen department

def choose_performance_rating():
    return np.random.choice(PERFORMANCE_RATINGS, p=PERFORMANCE_PROB)  # Randomly choose a performance rating based on probabilities

def choose_overtime():
    return np.random.choice(['Yes', 'No'], p=OVERTIME_PROB)  # Randomly choose whether overtime is applicable

def choose_hire_date():
    year = np.random.choice(YEARS, p=YEAR_PROB)  # Randomly choose a year for hire date
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)
    return fake.date_between(start_date=start_date, end_date=end_date)  # Generate a random hire date within the chosen year

def generate_salary(department, job_title):
    min_salary, max_salary = SALARY_RANGES[job_title]  # Get the salary range for the chosen job title
    return random.randint(min_salary, max_salary)  # Generate a random salary within the range

def calculate_adjusted_salary(base_salary, gender, education_level, age):
    adjusted_salary = base_salary
    # Apply gender adjustment
    if gender == 'Female':
        adjusted_salary *= 0.97  # Decrease salary by 3% for female employees
    # Apply education level adjustment
    if 'Master' in education_level:
        adjusted_salary *= 1.1  # Increase salary by 10% for Master's degree
    elif 'Bachelor' in education_level:
        adjusted_salary *= 1.05  # Increase salary by 5% for Bachelor's degree
    # Apply age adjustment
    if age < 30:
        adjusted_salary *= 0.95  # Decrease salary by 5% for employees under 30
    elif age > 50:
        adjusted_salary *= 1.05  # Increase salary by 5% for employees over 50
    return int(adjusted_salary)  # Return the adjusted salary

def generate_birth_date(hire_date, job_title):
    age_distribution = {
        'HR Manager': (30, 55),
        'HR Assistant': (22, 35),
        'Developer': (22, 40),
        'System Admin': (25, 45),
        'IT Support': (20, 35),
        'Accountant': (25, 50),
        'Financial Analyst': (25, 45),
        'Sales Manager': (28, 50),
        'Sales Representative': (20, 35),
        'Marketing Manager': (28, 45),
        'Marketing Specialist': (22, 35)
    }
    min_age, max_age = age_distribution[job_title]  # Get the age distribution for the chosen job title
    hire_year = hire_date.year
    birth_year = random.randint(hire_year - max_age, hire_year - min_age)  # Generate a random birth year based on age distribution
    while True:
        try:
            birth_date = datetime(birth_year, fake.random_int(min=1, max=12), fake.random_int(min=1, max=28))  # Generate a valid birth date
            break
        except ValueError:
            continue
    return birth_date

def generate_termination_date(hire_date):
    if random.random() > 0.112:  # Only 11.2% of employees have a termination date
        return None
    year = np.random.choice(YEARS, p=YEAR_PROB)
    if year <= hire_date.year + 1:
        year = hire_date.year + 2  # Ensure termination date is at least 1 year after hire date
    start_date = hire_date + timedelta(days=180)  # Ensure termination date is at least 6 months after hire date
    end_date = datetime(year, 12, 31)
    return fake.date_between(start_date=start_date, end_date=end_date)

# Generate the dataset
data = []

for i in range(1, 8951):
    employee_id = generate_employee_id(i)
    first_name = fake.first_name()
    last_name = fake.last_name()
    gender = choose_gender()
    state, city = choose_state_city()
    hire_date = choose_hire_date()
    department = choose_department()
    job_title = choose_job_title(department)
    education_level = EDUCATION_LEVELS[job_title]
    performance_rating = choose_performance_rating()
    overtime = choose_overtime()
    base_salary = generate_salary(department, job_title)
    birth_date = generate_birth_date(hire_date, job_title)
    age = hire_date.year - birth_date.year
    adjusted_salary = calculate_adjusted_salary(base_salary, gender, education_level, age)
    termination_date = generate_termination_date(hire_date)
    
    data.append([
        employee_id, first_name, last_name, gender, state, city, hire_date, department, job_title,
        education_level, performance_rating, overtime, base_salary, birth_date, termination_date, adjusted_salary
    ])

columns = [
    'Employee ID', 'First Name', 'Last Name', 'Gender', 'State', 'City', 'Hire Date', 'Department',
    'Job Title', 'Education Level', 'Performance Rating', 'Overtime', 'Salary', 'Birth Date',
    'Termination Date', 'Adjusted Salary'
]

df = pd.DataFrame(data, columns=columns)  # Create a DataFrame from the generated data

# Save to CSV
df.to_csv('hr_dataset_from_code.csv', index=False)  # Save the DataFrame to a CSV file

print("Dataset generated and saved to 'hr_dataset_from_code.csv'")