dias = int(input())

a = dias // 365
dias = dias - (a*365)

m = dias // 30
dias = dias - (m*30)

d = dias

print('{} ano(s)'.format(a))
print('{} mes(es)'.format(m))
print('{} dia(s)'.format(d))