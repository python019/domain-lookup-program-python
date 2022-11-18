import whois as pywho
import time as t

search = input("Qaysi domenni qidirmoqchisiz?: ")


# domain name
t.sleep(0.35)
print("   Domain nomi:", search)

print('''   -------------------''')

# creation date
print("   Asoschi kompaniya:", pywho.whois(search).org)
t.sleep(0.35)

print('''   -------------------''')

# creation date
try:
    for x in pywho.whois(search).creation_date:
        t.sleep(0.15)
        print("   Tashkil etilgan sanasi:", x)
except TypeError:
    print("   Tashkil etilgan sanasi:", pywho.whois(search).creation_date)
    
print('''   -------------------''')

t.sleep(0.35)
for content in pywho.whois(search).emails:
    t.sleep(0.15)
    print("   Emaillar:", content)
