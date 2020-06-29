class Currency(object):
    USD = '$'

    @staticmethod
    def fetch_symbol(currency):
        sym = getattr(Currency, currency, None)
        if sym:
            return sym
        return currency
