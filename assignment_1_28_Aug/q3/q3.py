# Q3. In DevOps, automating configuration management tasks is essential for maintaining consistency and managing infrastructure efficiently.
# ●       The program should read a configuration file (you can provide them with a sample configuration file).
# ●       It should extract specific key-value pairs from the configuration file.
# ●       The program should store the extracted information in a data structure (e.g., dictionary or list).
# ●       It should handle errors gracefully in case the configuration file is not found or cannot be read.
# ●       Finally save the output file data as JSON data in the database.
# ●       Create a GET request to fetch this information.
# Sample Configuration file: 
# [Database]
# host = localhost
# port = 3306
# username = admin
# password = secret
 
# [Server]
# address = 192.168.0.1
# port = 8080
 
# Sample Output: 
# Configuration File Parser Results:
# Database:
# - host: localhost
# - port: 3306
# - username: admin
# - password: secret
 
# Server:
# - address: 192.168.0.1
# - port: 8080 

import json

try:
  file = open("assignment_1_28_Aug/q3/server.config.json", "r")
  config_data = json.loads(file.read())
  print('Configuration File Parser Results:')
  
  for key, value in config_data.items():
    print(str(key).capitalize() + ':')
    if(type(value) == dict and len(value.keys()) > 0):
      for child_key, child_value in value.items():
        print('- ', str(child_key) + ':', child_value)
    print()

  file.close()

except FileNotFoundError as e:
  print('FileNotFoundError: ', e)

except json.decoder.JSONDecodeError as e:
  print('JSONDecodeError: ', e)


