# Default values, to be used for all environments or overridden by individual environments.
# An example might be setting DEBUG = False in config/default.py and DEBUG = True in config/development.py.
from dotenv import load_dotenv
import os
load_dotenv()

class Settings(object):
    EBAY_SEARCH_URL = os.getenv("EBAY_SEARCH_URL")
    EBAY_APP_ID = os.getenv("EBAY_APP_ID")
    Ebay = 'Ebay'
    EBAY_LOGO_PATH = 'static/assets/Ebay-logo.png'
    INSTOCK_LABEL = 'InStock'
    OUTOFSTOCK_LABEL = 'OutofStock'
    BRAND_NEW_ITEM = 'Unused'
    FREE_SHIPPING = 'Free Shipping'

    WEBSITE_NAME = 'MYYNAH'
    MYYNAH_LOGO_IMG_PATH = 'static/assets/Myynah-logo.png'
    MYYNAH_IMG_PATH = 'static/assets/Myynah-name-cinzel.png'
    ABOUT_IMG_PATH = 'static/assets/About-icon.png'
