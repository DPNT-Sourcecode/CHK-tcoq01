from collections import Counter, namedtuple

ItemPrice = namedtuple(
    'ItemPrice',
    [
        'price',
        'special_offer_price',
        'special_offer_quantity'
    ],
)

PRICE_LIST = {
    'A': ItemPrice(50, 130, 3),
    'B': ItemPrice(30, 45, 2),
    'C': ItemPrice(20),
    'D': ItemPrice(15),
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total = 0
    items = Counter(skus)
    
