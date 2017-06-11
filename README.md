# bulk-transcript-downloader
Sample application to export chat transcripts (in bulk) from a SocialMiner server

## Overview
This sample does the following:
1. Invokes a `/search` REST API request on a Cisco SocialMiner server for all handled chat contacts
2. Processes the response from the server, and extracts chat transcript data
3. Exports transcript for each chat session into a separate text file (with additional metadata)
4. Archives all the exported transcripts into a ZIP file

## Running
### Setup
1. Cisco SocialMiner server
2. Client machine with [Python 2.7+](https://www.python.org/downloads/) in the system/user `PATH`

### Run
```shell
python bulk-transcript-downloader.py --host <HOST_ADDRESS> --user <ADMIN_USERNAME> --password <ADMIN_PASSWORD>
```
where
```
HOST_ADDRESS        = IP address/hostname of the SocialMiner server
ADMIN_USERNAME      = login id of the application administrator account of the SocialMiner server
ADMIN_PASSWORD      = login password of the application administrator account of the SocialMiner server
```
