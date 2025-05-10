import getpass
while 1:
  try:
      print(getpass.getpass("Enter password (Ctrl+C to quit): "))
  except:
    break
