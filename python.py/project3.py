import datetime  

currentTime = datetime.datetime.now()  

print(f"Current date and time: {currentTime}")    
print(f"Year: {currentTime.year}")  
print(f"Month: {currentTime.month}")  
print(f"Day: {currentTime.day}")  
print(f"Hour: {currentTime.hour}")  
print(f"Minute: {currentTime.minute}")  
print(f"Second: {currentTime.second}")  

formatted_time = currentTime.strftime("%d-%m-%Y %H:%M:%S")  
print(f"Formatted Time: {formatted_time}")  
