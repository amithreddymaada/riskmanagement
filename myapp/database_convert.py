import pandas as pd
from models import CountriesInfo

tmp_data=pd.read_csv('../Customer-Rating-System-Datasets/countries_info.csv',sep=',')
#ensure fields are named~ID,Product_ID,Name,Ratio,Description
#concatenate name and Product_id to make a new field a la Dr.Dee's answer

countries = [
    CountriesInfo(
        list_id = tmp_data.ix[row]['list_id'], 
        entity_key = tmp_data.ix[row]['entity_key'],
    )
    for row in tmp_data
]
CountriesInfo.objects.bulk_create(countries)