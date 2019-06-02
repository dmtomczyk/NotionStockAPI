from notion.client import NotionClient
from notion.collection import *
from yahoo_fin.stock_info import *


class StockAPI:

    # Default Constructor
    def __init__(self):
        self.pageUrl = ""

    # Main Constructor
    @classmethod
    def ourCollection(cls, inputUrl, client):
        # Sets the notion pageUrl to be used later
        pageUrl = inputUrl
        # Creates our page object using the page url
        page = client.get_block(inputUrl)

    def printPageTitle(page):
        print("The current title is:", page.title)

    def setPageTitle(page):
        print("The page: %s" % (page))
        page.title = "Stock API Test #2"

    def getCollectionView(myClient, myCollection):
        cv = myClient.get_collection_view(
            "https://www.notion.so/44b1c9b0207b4c0db87ff24ccbded57a?v=c817cfaca39b4e8fba9abdcbdb84705b")
        return cv

    def queryCollection(cv, searchParam):
        results = []
        q = CollectionQuery(cv.collection, cv, "UXIN")
        for res in q.execute():
            results.append(res)
        return results

    def printQueryResults(array):
        countResults = 0
        for elem in array:
            countResults += 1
            print("printQueryResults() #%d - %s" % (countResults, elem))


def main():

    # TODO: Change these before posting -- NOTION PAGE URLS, ETC
    myPageUrl = "https://www.notion.so/44b1c9b0207b4c0db87ff24ccbded57a?v=c817cfaca39b4e8fba9abdcbdb84705b"
    myClient = NotionClient(
        token_v2="05c8397ff8f2a208df71c2c89d12a857b3b25fa546eeff51415f77228b2f6d105c50220121a4d202e7c8e44aaff8e7323968b9129a9b46caad9d6500b474cd105fe29645c49e0fb2e36cd3bceb9e")
    myCollection = StockAPI.ourCollection(
        "https://www.notion.so/44b1c9b0207b4c0db87ff24ccbded57a?v=c817cfaca39b4e8fba9abdcbdb84705b", myClient)

    # Returns the collection view and stores in colView
    colView = StockAPI.getCollectionView(myClient, myCollection)

    # Returns array of results
    searchParam = "UXIN"
    queryColView = StockAPI.queryCollection(colView, searchParam)
    StockAPI.printQueryResults(queryColView)

    # Stock testing
    uxinInfo = get_analysts_info("UXIN")
    for elem in uxinInfo:
        print(elem)


# Python Protecting
if __name__ == "__main__":
    main()
