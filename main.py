import whois as pywho
import time as t

search = input("Which domain lookup?: ")


# domain name
t.sleep(0.35)
print("   Domain name:", search)

print('''   -------------------''')

# creation date
print("   Company:", pywho.whois(search).org)
t.sleep(0.35)

print('''   -------------------''')

# creation date
try:
    for x in pywho.whois(search).creation_date:
        t.sleep(0.15)
        print("   Creation date:", x)
except TypeError:
    print("   Creation date:", pywho.whois(search).creation_date)
    
print('''   -------------------''')

t.sleep(0.35)
for content in pywho.whois(search).emails:
    t.sleep(0.15)
    print("   Emails:", content)
