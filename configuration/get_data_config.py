# get_data_config.py

import configparser

# 1. Create config parser object
config = configparser.ConfigParser()

# 2. Read the .ini file
config.read('configuration.ini')

# 3. Access values from sections

# DEFAULT section
app_name = config['DEFAULT']['AppName']
environment = config['DEFAULT']['Environment']
base_url = config['DEFAULT']['BaseURL']

# Credentials section
username = config['Credentials']['Username']
password = config['Credentials']['Password']

# Timeouts section (convert to int)
implicit_wait = int(config['Timeouts']['ImplicitWait'])
page_load_timeout = int(config['Timeouts']['PageLoadTimeout'])

# 4. Print loaded values (for demo)
print(f"App Name: {app_name}")
print(f"Environment: {environment}")
print(f"Base URL: {base_url}")
print(f"Username: {username}")
print(f"Password: {password}")
print(f"Implicit Wait: {implicit_wait} seconds")
print(f"Page Load Timeout: {page_load_timeout} seconds")