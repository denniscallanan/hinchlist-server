import requests

session_tokens = {}


def get_authorized_user(access_token):
    if access_token in session_tokens:
        print("User " + session_tokens[access_token] + " authorized through session")
        return session_tokens[access_token]
    r = requests.get(url="https://graph.facebook.com/me", params={
        "fields": "id",
        "access_token": access_token
    })
    response = r.json()
    if "id" in response:
        print("User " + response.get("id") + " authorized through FB auth")
        session_tokens[access_token] = response.get("id")
        return response.get("id")
    return None
