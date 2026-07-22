# docs/plugins/algolia.py @ 652a61ce4f9d7d76eaada31535807a485ece0e21 — bounded material capture
from bs4 import Tag

def on_page_content(html, page, config, files):
    if not os.getenv('CI'):
        return html
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    first_element = soup.find()
    for element in soup.find_all(['autoref']):
        element.decompose()
    headings = soup.find_all(['h1', 'h2', 'h3'])
    for current_heading in headings:
        sibling = current_heading.find_next_sibling()

# No direct .select(), .select_one(), or soupsieve.compile() call was found in
# the bounded inspected target path. This is not a complete absence proof.
