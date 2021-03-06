from django.shortcuts import render

import pandas as pd
import os
from django.conf import settings



month = [1,2,3,4,5,6,7,8,9,10]
h2_sum_of_incomming_greater_than = 1000
h3_sum_of_outing_greater_than = 800
h4_number_of_transactions_in_a_day = 20  

m2_sum_of_incomming_greater_than = 600
m2_sum_of_incomming_less_than = 1000
m3_sum_of_outing_greater_than = 500
m3_sum_of_outing_greater_than = 800
m4_number_of_transactions_lessthan_in_a_day = 20  
m4_number_of_transactions_greaterthan_in_a_day = 10  


l1_sum_of_incomming_less_than = 1000
l1_sum_of_outing_less_than = 500
l1_number_of_transactions_lessthan_in_a_day = 10



def index(request):
    return render(request,'index.html')

def risk23(request):
    df = pd.read_csv('C:\\Users\\amith\\DjangoProjects\\riskmanagement\\Customer-Rating-System-Datasets\\customer_transactions.csv')
    names = pd.read_csv('C:\\Users\\amith\\DjangoProjects\\riskmanagement\\Customer-Rating-System-Datasets\\customer_account_info.csv')
    
    df.columns = ['Key', 'Acckey', 'Amount', 'Type', 'Country', 'Date']
    persons = df.groupby('Acckey')

    high = set()
    medium = set()
    low = set()

    for group_name, df_group in persons:
        t_group = df_group.groupby('Type')
        
        for type_grp, grp in t_group:
            #In cond
            total = grp['Amount'].sum()
            if type_grp=='INN' and total>h2_sum_of_incomming_greater_than:
                high.add(group_name)
            elif type_grp=='INN' and total>m2_sum_of_incomming_greater_than:
                medium.add(group_name)
            else:
                low.add(group_name)

            #Out condn
            if type_grp=='OUT' and total>h3_sum_of_outing_greater_than:
                high.add(group_name)
            elif type_grp=='OUT' and total>m3_sum_of_outing_greater_than:
                medium.add(group_name)
            else:
                low.add(group_name)
    names.columns = ['Acckey', 'Key', 'date']
    try:
        high = pd.DataFrame(high)
        high.columns = ['Acckey']
        
        high_keys = pd.merge(high, names, on='Acckey', how='inner')
        return_high = list(high_keys['Key'])
    except:
        return_high = []
    try:
        medium = pd.DataFrame(medium)
        medium.columns = ['Acckey']
        
        medium_keys = pd.merge(medium, names, on='Acckey', how='inner')
        return_medium = list(medium_keys['Key'])
    except:
        return_medium = []

    try:
        low = pd.DataFrame(low)
        low.columns = ['Acckey']
        
        low_keys = pd.merge(low, names, on='Acckey', how='inner')
        return_low = list(low_keys['Key'])
    except:
        return_low=[]

    return render(request, 'display.html', {'high':return_high, 'medium':return_medium, 'low':return_low})

def rules(request):
    return render(request, 'index.html')