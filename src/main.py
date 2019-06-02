# https://github.com/jamalex/notion-py
# Thanks to this repo for their work

from notion.client import NotionClient

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
# TODO: This is my private key -- REMOVE BEFORE POSTING <token_v2>
client = NotionClient(
    token_v2="05c8397ff8f2a208df71c2c89d12a857b3b25fa546eeff51415f77228b2f6d105c50220121a4d202e7c8e44aaff8e7323968b9129a9b46caad9d6500b474cd105fe29645c49e0fb2e36cd3bceb9e")

# Replace this URL with the URL of the page you want to edit
page = client.get_block(
    "https://www.notion.so/44b1c9b0207b4c0db87ff24ccbded57a?v=c817cfaca39b4e8fba9abdcbdb84705b")

print("The old title is:", page.title)

# Note: You can use Markdown! We convert on-the-fly to Notion's internal formatted text data structure.
page.title = "The title has now changed, and has *live-updated* in the browser!"
