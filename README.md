
# IP-Lookup
IP-Lookup is a Database and Python Script to Programmatically look up details of an IP address.

# Usage

![enter image description here](https://i.imgur.com/yCzlwxO.gif)

To use this script, you need python3 and the packages as follows:

 - json
 - requests
 - beautifulsoup4
 - codecs
 - base64

The packages base64 and json are already included in python3, to install the other dependencies, run the following:

    python3 -m pip install requests beautifulsoup4

# Sample Output
Using the IP: 

    198.54.117.250

JSON Output:

    {
     "IP": "198.54.117.250",
     "Decimal": "3325457914",
     "Hostname": "namecheap.com",
     "ASN": "22612",
     "ISP": "Namecheap",
     "Organization": "Namecheap",
     "Services": "None detected",
     "Type": "Corporate",
     "Assignment": "Likely Static IP",
     "Blacklist": "",
     "Continent": "North America",
     "Country": "United States",
     "Latitude": "37.751",
     "Longitude": "-97.822"
    }

# Additional Info

**The database connection code has been encrypted to prevent unauthorized connections**

# Customization

the 'ip' variable is the ip to get info on and it can be ipv4 or ipv6  
  
'tab1' is the list of keys for the json data and 'tab2' is the data itself  
  
'PRINT_CREDITS' boolean to determine whether or not to include "IP Lookup by Rohan Patra" in output
