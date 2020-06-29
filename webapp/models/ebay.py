from webapp.models.partner_response import PartnerResponse
from webapp.models.client.base_client import BaseClient
from config.default import Settings
from webapp.models.currency import Currency

class Ebay(object):

    def __init__(self):
        pass

    @staticmethod
    def fetch_query_results(search_query):
        ebay_obj = Ebay()
        url = ebay_obj.construct_url(search_query)

        client = BaseClient(url)
        response = client.get()

        if response.status_code == 200:
            return ebay_obj.format_response(response.content)
        return response

    def format_response(self, response):
        response = response.get('findItemsByKeywordsResponse')
        response = response[0].get('searchResult')[0]
        if response.get('@count') == 0:
            return
        item = response.get('item')[0]
        item_json = {}
        item_json['partner_icon_path'] = Settings.EBAY_LOGO_PATH
        item_json['partner'] = Settings.Ebay
        item_json['name'] = item['title'][0]
        item_json['category'] = item['primaryCategory'][0].get('categoryName')[0]
        item_json['url'] = item['viewItemURL'][0]
        item_json['image_url'] = item['galleryURL'][0] if item.get('galleryURL') else 'https://sisterhoodofstyle.com/wp-content/uploads/2018/02/no-image-1.jpg'
        item_json['payment'] = item['paymentMethod']
        item_json['price'] = item['sellingStatus'][0]['currentPrice'][0]['__value__']

        currency = item['sellingStatus'][0]['currentPrice'][0]['@currencyId']
        item_json['price_currency'] = Currency.fetch_symbol(currency)

        item_json['shipping_cost'] = item['shippingInfo'][0]['shippingServiceCost'][0]['__value__']
        item_json['free_shipping'] = True if int(float(item_json['shipping_cost'])) == 0 else False
        item_json['shipping_currency'] = item['shippingInfo'][0]['shippingServiceCost'][0]['@currencyId']
        item_json['availability'] = Settings.INSTOCK_LABEL if item['sellingStatus'][0]['sellingState'][0] == 'Active' else Settings.OUTOFSTOCK_LABEL
        item_json['item_condition'] = Settings.BRAND_NEW_ITEM if item['condition'][0]['conditionDisplayName'][0] == 'New' else item['condition'][0]['conditionDisplayName'][0]
        return PartnerResponse(**item_json)


    def construct_url(self, search_query):
        return ('{0}OPERATION-NAME=findItemsByKeywords'
        '&SERVICE-VERSION=1.0.0'
        '&SECURITY-APPNAME={1}'
        '&RESPONSE-DATA-FORMAT=JSON'
        '&REST-PAYLOAD'
        '&keywords={2}'
        '&SortOrderType=BestMatch'
        '&paginationInput.entriesPerPage=1').format(Settings.EBAY_SEARCH_URL, Settings.EBAY_APP_ID, search_query)
