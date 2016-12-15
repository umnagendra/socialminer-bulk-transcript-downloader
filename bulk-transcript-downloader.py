##
# Cisco SocialMiner Bulk Chat Transcript Downloader
#
# Copyright (c) 2016 by Cisco Systems, Inc.
# All rights reserved.
#
# The code included in this example is intended to provide guidance to the
# developer on best practices and usage of the SocialMiner Chat RESTful
# APIs and is not intended for production use "as is".
#
# Cisco's responsibility and liability on this code is limited ONLY to the
# correctness and accuracy on the usage of the Chat RESTful API interface and
# the quality of the Chat RESTful API interface itself. Any omissions from this
# example are not to be considered capabilities that are supported or not
# supported by the product.
#
# For specific capabilities refer to the documentation that accompanies the latest
# Cisco SocialMiner release and/or request help from the Cisco Developer Network
# (http://developer.cisco.com) or the Cisco Technical Assistance Center
#

import sys
import argparse
import requests
import time
import xml.etree.ElementTree as ElementTree

# CONSTANTS
SEARCH_API_URL = "http://{}/ccp-webapp/ccp/search/contacts?q=sc.sourceType:chat%20AND%20sc.socialContactStatus:handled"

def usage():
    print __name__ + " --host=<HOSTNAME/IP OF SOCIALMINER> --user=<ADMIN_USERNAME> --password=<ADMIN_PASSWORD>"

def make_search_request(url, user, password):
    print "Making a GET request to the URL", url
    response = requests.get(url, auth=(user, password))
    if response.status_code != 200:
        print "ERROR - API request to SocialMiner failed with status [", response.status_code, "]"
        print "Error response:\n", response.text
        sys.exit(1)
    return response.text


def main():
    argParser = argparse.ArgumentParser(description="Cisco SocialMiner Bulk Chat Transcript Downloader")
    argParser.add_argument("--host", help="Hostname / IP Address of SocialMiner", required=True)
    argParser.add_argument("--user", help="Username of application admin account in SocialMiner", required=True)
    argParser.add_argument("--password", help="Password of application admin account in SocialMiner", required=True)
    args = vars(argParser.parse_args())

    host = args["host"]
    username = args["user"]
    password = args["password"]

    # make a search API request to SocialMiner to get all SCs and their transcripts
    search_response = make_search_request(SEARCH_API_URL.format(host), username, password)
    root = ElementTree.fromstring(search_response)

    for chat_transcript in root.iter('ChatTranscript'):
        print "+--------------- WEB CHAT TRANSCRIPT ---------------+"
        print "| Exported from Cisco SocialMiner [", host, "] by '", username, "' at ", \
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print "|"
        print "| ID:          ", chat_transcript.find('id').text
        print "| Customer:    ", chat_transcript.find('chatInitiator').text
        print "| Started:     ", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(chat_transcript.find('startDate').text)/1000))
        print "| Ended:       ", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(chat_transcript.find('endDate').text)/1000))
        print "+---------------------------------------------------+"

    # TODO - parse the response, extract all ChatTranscripts
    # TODO - for each ChatTranscript, create a text file per SC and dump contents

if __name__ == '__main__':
    main()
