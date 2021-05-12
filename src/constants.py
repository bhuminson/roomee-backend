# THIS SHOULD ALWAYS BE FALSE IN MAIN
dev = True

host = "ec2-18-215-111-67.compute-1.amazonaws.com"
db = "dbv08kj3kcvmh2"
user = "ejhswicwaijxhi"
pw = "b6d132d6465d2a329db0a0e1365f67319ab8ddc71785f61dc75f6fe460e17078"

if dev:
    host = "localhost"
    db = "roomee"
    user = "postgres"
    pw = " "
