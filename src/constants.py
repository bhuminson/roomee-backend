# THIS SHOULD ALWAYS BE FALSE IN MAIN
dev = True

host = "ec2-23-23-128-222.compute-1.amazonaws.com"
db = "d4n8vp78jra9c"
user = "zdtrqgmvvxojhg"
pw = "7a6b61d68568deb83ecfcd9d14a757ed8966fe017e0917194e065e4a0e340972"

if dev:
    host = "localhost"
    db = "roomee"
    user = "postgres"
    pw = " "
