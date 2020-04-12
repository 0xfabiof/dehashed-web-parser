import subprocess
import sys


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

try:
	session_id = sys.argv[1]
	query = sys.argv[2]

	all_results = subprocess.check_output(['curl','-s','https://www.dehashed.com/search?query='+query,'-H','Cookie: mysession='+session_id])


	## get array of data-entries-ids

	z = list(find_all(all_results,'data-entry-id="'))

	arrayOfDataEntryIds = []

	for j in z:
		b2 = all_results[j+15:j+51]
		arrayOfDataEntryIds.append(b2)


	## iterate through each of the data-entries-id and request the json for each of them

	final_results = []
	for i in arrayOfDataEntryIds:
		result = subprocess.check_output(['curl','-s','https://www.dehashed.com/search/'+i,'-H','Cookie: mysession='+session_id])
		final_results.append(result)

	for k in final_results:
		print(k)

except:
	print('Error - usage: python2 dehashed.py <valid session_id> <query>')
