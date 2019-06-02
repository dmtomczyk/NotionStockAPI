from notion.client import NotionClient
from notion.collection import *
from yahoo_fin.stock_info import *


class NotionAPI:

    # Default Constructor
    def __init__(self):
        self.pageUrl = ""

    # Main Constructor
    @classmethod
    def my_collection(cls, inputUrl, client):
        # Sets the notion pageUrl to be used later
        pageUrl = inputUrl
        # Creates our page object using the page url
        page = client.get_block(inputUrl)

    # Prints the page title
    def print_page_title(page):
        print("The current title is:", page.title)

    # Returns a dict of rows
    def get_my_rows(cv):
        my_rows = cv.collection.get_rows()
        print(my_rows)
        return my_rows

    # Adds stock info to row
    def add_stock_info(cv, client, stockDict):
        print("Adding new row...")
        # Add a new record
        row = cv.collection.add_row()
        row.name = "API Testing"
        row.status = "APITesting"
        # row.tags = ["A", "C"]
        # row.where_to = "https://learningequality.org"

    # Sets the page title
    def set_page_title(page):
        print("The page: %s" % (page))
        page.title = "Stock API Test #2"

    # Returns the id of the collection
    def get_collection_view(myClientInstance):
        cv = myClientInstance.get_collection_view(
            "https://www.notion.so/44b1c9b0207b4c0db87ff24ccbded57a?v=c817cfaca39b4e8fba9abdcbdb84705b")
        return cv

    def query_collection(cv, searchParam):
        results = []
        q = CollectionQuery(cv.collection, cv, "UXIN")
        for res in q.execute():
            results.append(res)
        return results

    def print_query_results(array):
        countResults = 0
        for elem in array:
            countResults += 1
            print("print_query_results() #%d - %s" % (countResults, elem))


def main():

    # Default values
    notionPageURL = "https://www.notion.so/44b1c9b0207b4c0db87ff24ccbded57a?v=c817cfaca39b4e8fba9abdcbdb84705b"
    myClientInstance = NotionClient(
        token_v2="05c8397ff8f2a208df71c2c89d12a857b3b25fa546eeff51415f77228b2f6d105c50220121a4d202e7c8e44aaff8e7323968b9129a9b46caad9d6500b474cd105fe29645c49e0fb2e36cd3bceb9e")

    # Returns the "collection view" and stores in cv
    cv = NotionAPI.get_collection_view(myClientInstance)
    print("cv = %s" % cv)

    # Returns array of results
    searchParam = "UXIN"
    queryColView = NotionAPI.query_collection(cv, searchParam)
    NotionAPI.print_query_results(queryColView)

    # Stock testing
    uxinInfo = get_analysts_info("UXIN")
    stockEarnings = uxinInfo.get("Earnings Estimate")
    print(stockEarnings)
    NotionAPI.add_stock_info(cv, myClientInstance, stockEarnings)
    NotionAPI.get_my_rows(cv)

    # Adding stock information to Notion


# Python Protecting
if __name__ == "__main__":
    main()
