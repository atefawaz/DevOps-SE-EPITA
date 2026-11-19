# Test evidence 

## Case 1 : 
Command:  python3 validator.py messy.env

 echo "Exit code: $?"                                  

Output : 

APP_PORT must be an integer

DEBUG must be false

DB_PASSWORD can not be empty

dbhost must be in UPPERCASE

Exit code: 1


## Case 2 : DEBUG = False
Command :  
python3 validator.py debug.env.example 

 echo "Exit code: $?"

Output : 

DEBUG must be false

Exit code: 1


## Case 3 : Keys are in lower case 

Command : 

python3 validator.py keys.env.example

echo "Exit code: $?"

Output : 

APP_PORT must be an integer

DEBUG must be false

App_port must be in UPPERCASE

debug must be in UPPERCASE

Exit code: 1



## SUCESS CASE : 

Command : 
python3 validator.py valid.env.example

echo "Exit code: $?"

Output : 

Configuration accepted

Exit code: 0
