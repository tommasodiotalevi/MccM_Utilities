import csv
import sys
import argparse
from json import dumps
#sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/') # Add to pythonpath to import rest
#from rest import McM

def get_request_list(csv_reader):
	'''Given the CSV file containing information about the requests,
	   create the list of requests.'''
	request_list = []
	for row in csv_reader:
		request_list.append(row)
	return request_list

def submit_requests(request_list, dryrun=False):
	'''Given the list of requests, submit the requests to McM database.'''
	if dryrun:
		print('*'*30)
		print('Dry run requested, No submissions will be made.')
		print('*'*30)
	else:
		mcm = McM(dev=True)
	for request in request_list:
		# Add minimally required information to the request
		request['pwg'] = 'HIG'
		request['member_of_campaign'] = 'RunIIFall17wmLHEGS' # TODO: Needs to be checked/adjusted!
		print('Submitting request for %s' % request['Dataset name'])
		# Submit the request to McM database
		# if dry run is not requested.
		if not dryrun:
			put_answer = mcm.put(request)
			if put_answer.get('results'):
				print('New PrepID: %s' % put_answer['prep_id'])
			else:
				print('Something went wrong while creating a request. %s' % (dumps(put_answer)))

	print('*'*30)
	print('Submissions complete!')
	print('*'*30)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file', help='The CSV file containing information about the requests.')
	parser.add_argument('--dry', help='Do dry run, do not submit any request.', action='store_true')
	args = parser.parse_args()

	csvfile = args.file

	with open(csvfile, 'r') as f:
		csv_reader = csv.DictReader(f)

		request_list = get_request_list(csv_reader)
		# Get the headers (fields)
		headers = request_list[0].keys()
		print('The following fields are filled and to be submitted:')
		for header in headers:
			print(header)
		submit_requests(request_list, dryrun=args.dry)

if __name__ == '__main__':
	main()
