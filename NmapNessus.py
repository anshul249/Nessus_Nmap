import pandas as pd
import sys,operator
print('Nessus File:' + sys.argv[1])
arg1 = sys.argv[1]
from subprocess import check_output
fields=['Plugin ID','CVE','CVSS','Risk','Host','Protocol','Port','Name','Synopsis','Description','Solution','See Also','Plugin Output']
script=['Vuln', 'Script']

da=pd.read_csv(arg1, usecols=fields, delimiter= ',')
df=da.sort_values('Name')
scriptFile=pd.read_csv('scripts.csv', usecols=script, delimiter= ',')
for index,row in df.iterrows():
	print index,row[7]
	for index1,row1 in scriptFile.iterrows():
		if str(row[7]) == str(row1[0]):
			print "nmap -Pn -n --script " + str(row1[1]) + " -p " + str(row[6]) + " " + str(row[4])
			out = check_output("nmap -Pn -n --script " + str(row1[1]) + " -p " + str(row[6]) + " " + str(row[4]), shell=True)
			print out