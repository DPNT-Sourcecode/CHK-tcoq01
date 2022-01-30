from collections import Counter, namedtuple

Offer = namedtuple('Offer', ['item', 'price', 'quantity', 'combined_item'])

PRICE_LIST = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 80,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 30,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 90,
    'Y': 10,
    'Z': 50,

}

ORDERED_SPECIAL_OFFERS = [
    Offer('A', 200, 5, None),
    Offer('A', 130, 3, None),
    Offer('E', 80, 2, 'B'),
    Offer('B', 45, 2, None),
    Offer('F', 20, 2, 'F'),
    Offer('H', 80, 10, None),
    Offer('H', 45, 5, None),
    Offer('K', 150, 2, None),
    Offer('N', 120, 3, 'M'),
    Offer('P', 200, 5, None),
    Offer('R', 150, 3, 'Q'),
    Offer('Q', 80, 3, None),
    Offer('U', 120, 3, 'U'),
    Offer('V', 130, 3, None),
    Offer('V', 90, 2, None),
]


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not isinstance(skus, str):
        return -1

    total = 0
    checkout_items = Counter(skus)

    for offer in ORDERED_SPECIAL_OFFERS:
        quantity = checkout_items.get(offer.item)
        if not quantity:
            continue

        applied_offer_count = int(quantity / offer.quantity)

        for i in range(applied_offer_count):
            total += offer.price
            checkout_items[offer.item] -= offer.quantity

            combined_item = offer.combined_item
            if combined_item and checkout_items[combined_item] > 0:
                checkout_items[combined_item] -= 1

    for sku, quantity in checkout_items.items():
        if sku not in PRICE_LIST:
            return -1

        total += PRICE_LIST[sku] * quantity
    
    return total




