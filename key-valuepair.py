# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n = int(sys.stdin.readline().strip())
#reads 1 line -- the first line (3)
phone_book = dict()
#makes a dictionary
for i in range(n):
    entry = sys.stdin.readline().strip().split(' ')
    phone_book[entry[0]] = entry[1]
    #goes through given inputs using the first line
    #splits name and phone #
    #enters them into the dictionary
query = sys.stdin.readline().strip()
#move on to second part
#read the queries (online the first line rn)
while query:
    phone_number = phone_book.get(query)
    #gets the # associated with the name 
    if phone_number:
        #checks if its true (it exists)
        print(query + '=' + phone_book.get(query))
    else:
        #phone # doesnt exist
        print('Not found')
    query = sys.stdin.readline().strip()
    #continues on to the next one
    
