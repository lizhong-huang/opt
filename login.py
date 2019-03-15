#!/home/lizhong/.virtualenvs/opt/bin/python3
{
    "resource": "11be82b8-af00-4d73-8bcd-ed50570b08cd",
    "tenant" : "omnipoint.onmicrosoft.com",
    "authorityHostUrl" : "https://login.microsoftonline.com",
    "clientId" : "11be82b8-af00-4d73-8bcd-ed50570b08cd",
    "clientSecret" : "rrnsoJOT6]tdSCJP3945}(!"
 }
import json
import logging
import os
import sys
import adal


def turn_on_logging():
    logging.basicConfig(level=logging.DEBUG)

    #or,
    #handler = logging.StreamHandler()
    #adal.set_logging_options({
    #    'level': 'DEBUG',
    #    'handler': handler
    #})

    #handler.setFormatter(logging.Formatter(logging.BASIC_FORMAT))

parameters_file = (".optauthparameter" if os.path.isfile(".optauthparameter") else
                   os.environ.get('ADAL_SAMPLE_PARAMETERS_FILE'))

if parameters_file:
    with open(parameters_file, 'r') as f:
        parameters = f.read()
    sample_parameters = json.loads(parameters)
else:
    raise ValueError('Please provide parameter file with account information.')

authority_url = (sample_parameters['authorityHostUrl'] + '/' +
                 sample_parameters['tenant'])

GRAPH_RESOURCE = '00000002-0000-0000-c000-000000000000'

RESOURCE = sample_parameters.get('resource', GRAPH_RESOURCE)

#uncomment for verbose log
#turn_on_logging()

### Main logic begins
context = adal.AuthenticationContext(
    authority_url, validate_authority=sample_parameters['tenant'] != 'adfs',
    )

token = context.acquire_token_with_client_credentials(
    RESOURCE,
    sample_parameters['clientId'],
    sample_parameters['clientSecret'])

### Main logic ends

file = open(".optaccesstoken", "w")
file.write(json.dumps(token, indent=2))
