import whois as w
from testing import sites as s

for x in s:
    print(f"""
        Saytning nomi: {x}
        Tegishli kompaniya: {w.whois(x).org}
        Tashkil topgan vaqti: {w.whois(x).creation_date}
        Emaili: {w.whois(x).emails}
    """)
