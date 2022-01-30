from collections import Counter, namedtuple

ItemPrice = namedtuple(
    'ItemPrice',
    [
        'price',
        'offer_price',
        'offer_quantity'
    ],
)

PRICE_LIST = {
    'A': ItemPrice(50, 130, 3),
    'B': ItemPrice(30, 45, 2),
    'C': ItemPrice(20, None, None),
    'D': ItemPrice(15, None, None),
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, str):
        return -1

    total = 0
    checkout_items = Counter(skus)

    for sku, quantity in checkout_items.items():
        if sku not in PRICE_LIST:
            return -1

        item_price = PRICE_LIST[sku]
        if item_price.offer_quantity and item_price.offer_price:
            total += (
                item_price.offer_price * int(quantity / item_price.offer_quantity) +
                item_price.price * (quantity % item_price.offer_quantity)
            )
        else:
            total += item_price.price * quantity
    
    return total

