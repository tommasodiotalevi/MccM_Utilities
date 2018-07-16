import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM
from json import dumps

mcm = McM(dev=False)

# Example to get  ALL requesst which are member of a given campaign and are submitted
# It uses a generic search for specified columns: query='status=submitted'
# Queries can be combined: query='status=submitted&member_of_campaign=Summer12'
#campaign_requests = mcm.get('requests', query='dataset_name=NMSSMCascade_mH-*_mSUSY-*_TuneCUEP8M1_13TeV-madgraph-pythia8')
#for request in campaign_requests:
#    print(request['prepid'])

# Example to retrieve single request dictionary
# More methods are here:
# https://cms-pdmv.cern.ch/mcm/restapi/requests/
single_request_prepid = 'HIG-RunIISummer15wmLHEGS-02135'
single_request = mcm.get('requests', single_request_prepid, method='get')
#print('Single request "%s":\n%s' % (single_request_prepid, single_request['generators']))#dumps(single_request, indent=4)))
for key in single_request:
	print key
## Example how to get multiple requests using range
#requests_query = """
#    B2G-Fall13-00001
#    B2G-Fall13-00005 -> B2G-Fall13-00015
#"""
#range_of_requests = mcm.get_range_of_requests(requests_query)
#print('Found %s requests' % (len(range_of_requests)))
#for request in range_of_requests:
#    print(request['prepid'])
