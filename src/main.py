from notion.client import NotionClient
from notion.collection import *
from yahoo_fin.stock_info import *

# NOTE:
# Available Statuses    -   { "Owned", "Pending", "Researching", "APITesting"}
# Standard Params       -   { "shares", "status", "marketopen", "fiftytwolow", "fiftytwohigh" }
# Common Functions      -
#   - get_stock_info_for_one_company(collectionView, stockName, status)
# Dependencies          -   { notion-py by jamalex, yahoo_fin, Anaconda(ftplib, io, pandas, requests, requests_html)}


class NotionAPI:

    # Default Constructor
    def __init__(self):
        self.pageUrl = ""

    # WORKING -- Returns a dict of rows
    def get_my_rows(collectionView):
        my_rows = collectionView.collection.get_rows()
        # print(my_rows)
        return my_rows

    # WORKING -- Adds stock info to row
    def add_stock_info(collectionView, name, status, shares, low, high, marketOpen):

        # Add a new record
        row = collectionView.collection.add_row()
        row.name = name
        row.status = status
        row.shares = shares
        row.fiftytwolow = low
        row.fiftytwohigh = high
        row.marketopen = marketOpen

    # WORKING -- Sets the page title
    def set_page_title(page):
        print("The page: %s" % (page))
        page.title = "Stock API Test #2"

    # WORKING -- Returns the id of the collection
    def get_collection_view(myClientInstance):
        collectionView = myClientInstance.get_collection_view(
            "https://www.notion.so/959730e14a554c2f967b70bccd414f0b?v=1a9d0f526c1049ebb304bfc359d2eb6f")
        return collectionView

    # WORKING -- Queries an existing collection
    def query_collection(collectionView, searchParam):
        results = []
        q = CollectionQuery(collectionView.collection, collectionView, "UXIN")
        for res in q.execute():
            results.append(res)
        return results

    # WORKING -- This returns a DataFrame object (Panda) -- Attributes -- Use .get("Col name"), then I can grab the items per index
    def get_stock_info_for_one_company(collView, name, status):

        # Declaring empty list that will store the results of our query
        stockResults = []

        # Setting our stock name and pulling from yahoo finance
        stockName = name
        stockInfo = get_stats(stockName)

        # PULLS "52 Low" & "52 High" from yahoo. -- https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.at.html#pandas.DataFrame.at
        fiftyTwoLow = float(stockInfo.at[35, "Value"])
        fiftyTwoHigh = float(stockInfo.at[34, "Value"])

        # PULLS "Open" value from yahoo finance
        marketOpen = float(get_quote_table(stockName).get("Open"))

        # PUSHING our info to the notion page
        NotionAPI.add_stock_info(
            collView, name, status, 8, fiftyTwoLow, fiftyTwoHigh, marketOpen)


def main():

    # NOTE: These are for a test account of mine that is not hooked up to anything else, though I would appreciate not using my token
    notionPageURL = "https://www.notion.so/959730e14a554c2f967b70bccd414f0b?v=1a9d0f526c1049ebb304bfc359d2eb6f"
    myClientInstance = NotionClient(
        token_v2="7f142fc772b9196c819854cc5a21666999c2e3accaa201b9fb40495b23ba66984966676769a93a81122b35b9b94baa51f02f45c39823d9eef1c3c81a4a410f97d88d344471e110f9f298a26cf5ad")

    # TESTING -- Returns the "collection view" and stores in collectionView
    collectionView = NotionAPI.get_collection_view(myClientInstance)
    print("collectionView = %s" % collectionView)

    # TESTING
    stockInfoRetrieved = NotionAPI.get_stock_info_for_one_company(
        collectionView, "UXIN", "Owned")


if __name__ == "__main__":
    main()
