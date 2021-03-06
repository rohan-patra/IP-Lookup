"""
Requirements: json, requests, beautifulsoup4

Disclaimer: The database connection code has been encrypted to prevent unauthorized connections

Customization:

the 'ip' variable is the ip to get info on and it can be ipv4 or ipv6

'tab1' is the list of keys for the json data and 'tab2' is the data itself

'PRINT_CREDITS' boolean to determine whether or not to include "IP Lookup by Rohan Patra" in output

"""

import base64, codecs

PRINT_CREDITS = True

ip = input('What is the IP address? ')

magic = 'aW1wb3J0IGpzb24NCg0KaW1wb3J0IHJlcXVlc3RzDQpmcm9tIGJzNCBpbXBvcnQgQmVhdXRpZnVsU291cA0KDQppZiBQUklOVF9DUkVESVRTOg0KICAgIHByaW50KCAnICAgIF9fX19fX19fX19fICAgXyAgICAgICAgICAgICAgICAgXyAgICAgICAgICAgICAgICAgIF8gICAgICAgICAgICBfX19fX18gICAgICBfICAgICAgICAgICAgICAgICAgX19fX19fICAgICBfICAgICAgICAgICAgICAgXG4nICArDQogICAgICcgICB8XyAgIF98IF9fXyBcIHwgfCAgICAgICAgICAgICAgIHwgfCAgICAgICAgICAgICAgICB8IHwgICAgICAgICAgIHwgX19fIFwgICAgfCB8ICAgICAgICAgICAgICAgICB8IF9fXyBcICAgfCB8ICAgICAgICAgICAgICBcbicgICsNCiAgICAgJyAgICAgfCB8IHwgfF8vIC8gfCB8ICAgICBfX18gICBfX18gfCB8IF9fXyAgIF8gXyBfXyAgIHwgfF9fICBfICAgXyAgfCB8Xy8gL19fXyB8IHxfXyAgIF9fIF8gXyBfXyAg'
love = 'VUjtsS8iVP9sVS98VUksVS8tK18tK18tKlNtVSkhWlNtXj0XVPNtVPNvVPNtVPO8VUjtsPNtK18iVPO8VUjtVPNtYlOsVSjtYlOsVSk8VUjiVP8tsPO8VUjtW18tKPNtsPNaKlOpsPO8VUjtsPO8VPNtVP8iVS8tKUjtW18tKPNiVS9tVUjtW18tKPNtsPNtK18iVS9tVUjtK198VPqsKl8tK2NtsPNtKT4vVPNeQDbtVPNtVPptVPNtK3jtsS98VUjtVPNtVUjtsS9sK3jtXS8cVUjtXS8cVUjtVPN8sPO8K3jtsPO8KlxtsPO8VUksXFO8VUkssPO8VUjtsSjtKPNbKlxtsPO8VUjtsPNbK3jtsPO8VUjtsPO8VUjtsPNbK3jtsPO8K3jtsPO8VPussPO8VPOpovptVPfAPvNtVPNtWlNtVPOpK19sY1kssPNtVPNtKS9sK19sY1ksK18iVSksK18isS98KS9pKS9sYS98VP5sKl8tVUksYy9sYlOpK18fVUjtKS98VSksKS9sKl98K3jtsS98KS9sYS98K3jtsS98VSkssPNtKS9sYS98KS9ssS98VPOpK18fK3jtVSkhWlNtXj0XVPNtVPNaVPNtVPNtVPNtVPNt'
god = 'ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHwgfCAgICAgICAgICAgICBfXy8gfCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgXG4nICArDQogICAgICcgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB8X3wgICAgICAgICAgICB8X19fLyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIFxuJykNCndpdGggcmVxdWVzdHMuc2Vzc2lvbigpIGFzIHM6DQogICAgcmVzID0gcy5nZXQoJ2h0dHBzOi8vd2hhdGlzbXlpcGFkZHJlc3MuY29tL2lwLycgKyBpcCkNCiAgICBzb3VwID0gQmVhdXRpZnVsU291cChyZXMuY29udGVudCwgJ2h0bWwucGFyc2VyJykNCiAgICB0YWIxID0gW10NCiAgICB0YWIyID0gW10NCiAgICBmb3IgdGFibGUgaW4gc291cC5maW5kX2FsbCgndGFibGUnKToN'
destiny = 'PvNtVPNtVPNtMz9lVTkcozHtnJ4tqTSvoTHhqTI4qP5mpTkcqTkcozImXPx6QDbtVPNtVPNtVPNtVPOfnKA0MKVtCFOfnJ5yYaA0pzyjXPxhp3OfnKDbWmbaYPNkXD0XVPNtVPNtVPNtVPNtnJLtoTIhXTkcp3EypvxtCvNkBt0XVPNtVPNtVPNtVPNtVPNtVTyzVTkcp3EypyfjKFN9CFNaGTS0nKE1MTHaVT9lVTkcp3EypyfjKFN9CFNaGT9hM2y0qJEyWmbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtqTSvZF5upUOyozDboTymqTIlJmOqXD0XVPNtVPNtVPNtVPNtVPNtVTIfp2H6QDbtVPNtVPNtVPNtVPNtVPNtVPNtVUEuLwRhLKOjMJ5xXTkcp3EypyfjKFxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtqTSvZv5upUOyozDboTymqTIlJmSqXD0XVPNtVPNtVPNtVPNtMJkmMGbAPvNtVPNtVPNtVPNtVPNtVPOcMvOfnKA0MKWoZS0tVG0tWlp6QDbtVPNtVPNtVPNtVPNtVPNtVPNtVUEuLwVhLKOjMJ5xXTkcp3EypyfjKF5mpTkcqPuBo25yYPNkXIfjKFx='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))

print(json.dumps(dict(zip(tab1, tab2)), indent = 1))
