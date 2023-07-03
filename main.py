import requests as r
import json
TAG = 'PQU2UJPUJ'
URL = f'https://api.clashroyale.com/v1/players/%23{TAG}/upcomingchests'

def main():
    response = r.get(URL, headers={"Authorization": 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjU0NjIwODA3LTZjZDktNDNhNS1iZGNiLTA1ZjYyZmE4YjUyOSIsImlhdCI6MTY4ODQwMTc4Niwic3ViIjoiZGV2ZWxvcGVyL2NkZTE3NDVlLWE1MGYtYjNlNC1lNDFhLWFiN2EzMGZhMzA3OCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIzMS4xNDQuMjA1LjIyMiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.KHVDZwYKJC8aQTRcjPQUVKxcv06KrlCMWHfScYxINAIyIqB-gX17Tfqdpv8uWsps_85kp6ZOcz_iwkXM8Lchdw'}, params=None).content.decode()
    edited_response = json.loads(response).get('items')
    unique_names = set()
    for d in edited_response:
        name = d['name']
        if name not in unique_names:
            unique_names.add(name)
            print(f'{name}: будет через {int(d.get("index")) + 1}')
    
main()
