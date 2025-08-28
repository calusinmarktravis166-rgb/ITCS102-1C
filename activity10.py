from getpass import getpass

username = 'mark'
pword = 'mark158'

u = input("USERNAME --> ")
p = getpass("PASSWORD --> ")
from getpass import getpass

if (u == username) and (p == pword) :
        print("Access Granted")
else:
        print("Access Denied")
 