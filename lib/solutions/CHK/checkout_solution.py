from collections import Counter, namedtuple

Offer = namedtuple('Offer', ['item', 'price', 'quantity', 'combined_item'])

PRICE_LIST = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
}

ORDERED_SPECIAL_OFFERS = [
    Offer('A', 200, 5, None),
    Offer('A', 130, 3, None),
    Offer('E', 80, 2, 'B'),
    Offer('B', 45, 2, None),
]

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, str):
        return -1

    total = 0
    checkout_items = Counter(skus)

    for sku, offers in ORDERED_SPECIAL_OFFERS.items():
        if sku not in checkout_items:
            continue

        quantity = checkout_items[sku]

        for offer in offers:
            applied_offer_count = int(quantity / offer.quantity)

            combined_item = offer.combined_item
            if combined_item:
                checkout_items[combined_item] -= applied_offer_count
                total += offer.price * applied_offer_count

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

