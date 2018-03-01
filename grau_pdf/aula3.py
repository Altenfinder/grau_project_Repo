import quandl
import pandas as pdb
'''
api_key = open('quandlapikey.txt','r').read()
'''
df = quandl.get('FMAC/HPI_AK',authtoken='')

print df.head()

fiddy_states = pdb.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

print fiddy_states[0][0]

for abbv in fiddy_states[0][0][1:]:
    print quandl.get('FMAC/HPI_'+str(abbv))
