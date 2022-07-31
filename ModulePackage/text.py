from datetime import datetime


# current_year_full = datetime.now().strftime('%Y') 
current_day_text = datetime.now().strftime('%a') 
current_month_text = datetime.now().strftime('%h')
current_day = datetime.now().strftime('%d') 

# print(current_day_text,current_day,current_month_text)


current_minute = datetime.now().strftime('%M')
current_hour = datetime.now().strftime('%H') 
current_hour = datetime.now().strftime('%I')
current_hour_am_pm = datetime.now().strftime('%p') 
# print(current_hour,current_minute,current_hour_am_pm)

current_day_text = datetime.now().strftime('%a') 
current_month_text = datetime.now().strftime('%h')
current_day = datetime.now().strftime('%d') 

current_minute = datetime.now().strftime('%M')
current_hour = datetime.now().strftime('%H') 
current_hour = datetime.now().strftime('%I')
current_hour_am_pm = datetime.now().strftime('%p') 

odate = current_day_text+","+current_day+" "+current_month_text
otime  =current_hour+":"+current_minute+" "+current_hour_am_pm

print(odate,otime)