import socket
while 1:
    try:
        WebSite = input().replace("https://", "").replace("http://", "")
    except:
        break
    try:
        ip = socket.gethostbyname(WebSite)
        print(ip)
    except:
        print(f"Incorrect website: {WebSite}!")
