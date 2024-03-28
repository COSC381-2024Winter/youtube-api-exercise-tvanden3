import config
import sys
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
DEVELOPER_KEY = config.API_KEY
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = 'v3'
def youtube_search(query_term, max_results, pageNumber):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY)
    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube. search().list(
        q=query_term,
        part='id,snippet',
        maxResults=max_results,
     ).execute()

    next_page_token = search_response['nextPageToken']

    next_search_response = youtube. search().list(
        q=query_term,
        part='id,snippet',
        maxResults=max_results,
        pageToken = next_page_token
     ).execute()

    next_page_token = search_response.get("nextPageToken")

    if pageNumber == 1:
        return search_response['items']

    for i in range(2, pageNumber + 1):
        search_responsetwo = youtube.search().list(
            q=query_term,
            part='id,snippet',
            maxResults=max_results,
            pageToken=next_page_token
        ).execute()
        pagekey = search_responsetwo.get("nextPageToken")

    return search_response['items']

if __name__ == "__main__":
    query_term = sys.argv[1]
    max_results = sys.argv[2]
    pageNumber = int(sys.argv[3])
    try:
         print (youtube_search(query_term, max_results, pageNumber))
    except HttpError as e:
        print("An HTTP error %d occurred: \n%s" % (type(e).__name, str(e)))