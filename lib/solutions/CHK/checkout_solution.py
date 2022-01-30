from collections import Counter, namedtuple

Offer = namedtuple('Offer', ['price', 'quantity', 'free_item'])

PRICE_LIST = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
}

SPECIAL_OFFERS = {
    'A': [Offer(200, 5, None), Offer(130, 3, None)],
    'B': [Offer(45, 2, None)],
    'E': [Offer(80, 2, 'B')],
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


