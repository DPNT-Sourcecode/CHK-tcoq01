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

        remaining = quantity
        item_price = PRICE_LIST[sku]
        if sku in SPECIAL_OFFERS:
            offers = SPECIAL_OFFERS[sku]
            for offer in offers:
                applied_offer_count = int(remaining / offer.quantity)

                combined_item = offer.free_item
                if combined_item:
                    checkout_items[combined_item] -= applied_offer_count

                total += offer.price * applied_offer_count
                remaining -= applied_offer_count

        total += item_price * remaining
    
    return total
