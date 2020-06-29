from webapp.models.ebay import Ebay
from webapp.models.amazon import Amazon

class Partners(object):
    def __init__(self, search_query):
        self.search_query = search_query

    def query_all_partners(self):
        a = {}
        a['featured'] = Ebay.fetch_query_results(self.search_query)
        return a
        Amazon.fetch_query_results(self.search_query)
