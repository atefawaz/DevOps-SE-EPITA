"""Student scaffold. Implement rules from Lab 2; never print secret values."""
import sys



def validate(values):
    errors = []
    
    port = values.get('APP_PORT',"")
    # checks if port is int 
    if not port.isdigit() : 
        errors.append("APP_PORT must be an integer")
        #  checks if port is in range
    elif not 1024 <= int(port) <= 65535: 
        errors.append("APP_PORT is out of range")
        # checks if debug is false
    if values.get('DEBUG',"") != 'false' :
        errors.append("DEBUG must be false")
        # checks if db host is empty
    if values.get('DB_HOST',"").strip() == "" :    
        errors.append("DB_HOST must  be nonempty ")
        # checks if password is empty o
    if values.get('DB_PASSWORD',"").strip() == "" :
        errors.append("DB_PASSWORD can not be empty")   
        # looping in values to check if KEYS are in uppercase or not  
    for key in values : 
        if not key.isupper():
            errors.append(f"{key} must be in UPPERCASE")

    return errors

def load(path):
    values = {}
    for line in open(path, encoding="utf8"):
        line = line.strip()
        if line and not line.startswith("#"):
            key, value = line.split("=", 1)
            values[key.strip()] = value.strip()
    return values

if __name__ == "__main__":
    issues = validate(load(sys.argv[1]))
    print("\n".join(issues) if issues else "Configuration accepted")
    sys.exit(bool(issues))
