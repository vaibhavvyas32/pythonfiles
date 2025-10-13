import requests
import json


username = input("Enter username: ")
url = f"https://api.github.com/users/{username}/events" 

res = requests.get(url)


if res.status_code == 200:
    print("Got the request! \n")
    data = res.json()

    
    for event in data[:5]:
        event_type = event["type"]
        repo_name = event["repo"]["name"]
        created_time = event["created_at"]

        
        if(event_type=="PushEvent"):
            no_of_commits = event["payload"]["size"]
            print(f"Pushed {no_of_commits} changes to {repo_name} at {created_time}")
        
        
        if(event_type=="CreateEvent"):
            print(f"Created {repo_name} at {created_time}")
        
    


else:
    print(f"Failed to fetch data. error code {res.status_code}")



