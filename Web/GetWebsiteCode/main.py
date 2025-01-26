import requests
while 1:
    try:
        WebSite = f"""http://{input().replace("https://", "").replace("http://", "")}"""
    except:
        break
    try:
        code = requests.get(WebSite)
        print(code.text)
    except:
        print(f"Incorrect website: {WebSite}!")
