# Findings : messy.env 


## DEFECTS 
1 - APP_PORT is not a number (string)
2- DEBUG must be false 

3 - Values can not be empty : DB_PASSWORD can not be empty

4 - dbhost should be in UPPER CASE 


## VALIDATION RULES

1- APP_PORT must be a whole number from 1024 to 65535 inclusive 

2-DEBUG must be exactly 'false' nothing else is accepted 

3- DB_PASSWORD present non empty

4- DB_HOST present non empty and in KEY  UPPERCASE