# This project is a toy project for training and quality assurance purposes

# day 5

Use this data set https://www.kaggle.com/datasets/kartik2112/fraud-detection and
https://huggingface.co/kmasiak/FraudDetection/blob/main/Dataset.csv

trans_date_trans_time -> this the date and time(when the balance transfered)
cc_num -> the transaction number
marchant -> name/organization of the marchant
category -> category of the marchant
amt -> ammount being transfered
first -> first name
last -> last name
gender -> male/female
steet -> street info
city -> city info
state -> which state
zip -> zip code
lat -> latitude
long -> longitude
city_pop -> city population
job -> what is the job description?
dob -> date of birth
trans_num -> transcation number
unix_time -> It measures time by the number of seconds that have elapsed since 00:00:00 UTC
march_lat -> marchant's latitude
march_long -> marchant's longitude
is_fraud -> fraud or not

Use decision tree ML algorithm, to find patterns for fraud.
Make flask api to give response

The input to your api to test for fraud is
"user_id",
"age",
"bday",
"sex",
"user_blocked",
"user_registration_ip",
"user_registration_datetime",
"deposit_id",
"transaction_date",
"type",
"total_amount",
"in",
