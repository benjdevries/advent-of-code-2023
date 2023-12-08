from enum import IntEnum
from itertools import groupby


class HandType(IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_KIND = 4
    FULL_HOUSE = 5
    FOUR_KIND = 6
    FIVE_KIND = 7


card_to_weight = {"A": "E", "K": "D", "Q": "C", "J": "B", "T": "A"}


def get_hand_weight(hand: str) -> str:
    output = ""
    for card in hand:
        if card.isdigit():
            output += card
        else:
            output += card_to_weight[card]

    return output


def get_hand_type(hand: str) -> HandType:
    card_counts = {}

    for card in hand:
        card_counts.setdefault(card, 0)
        card_counts[card] += 1

    if len(card_counts) == 1:
        # all the same
        print("Five of a kind")
        return HandType.FIVE_KIND

    elif any((n == 4 for n in card_counts.values())):
        # theres four of something
        print("Four of a kind")
        return HandType.FOUR_KIND

    elif len(card_counts) == 2:
        # if there's two types of cards, it must be full house
        # because we eliminated 4 of a kind
        print("Full house")
        return HandType.FULL_HOUSE

    elif any((n == 3 for n in card_counts.values())):
        # there's three of something
        print("Three of a kind")
        return HandType.THREE_KIND

    elif len([n for n in card_counts.values() if n == 2]) == 2:
        # there's two pairs of two
        print("Two pairs")
        return HandType.TWO_PAIR

    elif any((n == 2 for n in card_counts.values())):
        # there's a pair of something
        print("One pair")
        return HandType.ONE_PAIR

    elif len(card_counts) == 5:
        # all distinct
        print("High card")
        return HandType.HIGH_CARD

    else:
        raise ValueError("Invalid hand")


def main():
    hands = []

    with open("input.txt") as f:
        for line in f:
            hand, bid = line.split()
            print(hand)
            hand_type = get_hand_type(hand)
            hands.append({"hand": hand, "type": hand_type, "bid": int(bid)})
            print()

    hands.sort(key=lambda x: x["type"])

    sorted_hands = []

    for _, g in groupby(hands, key=lambda x: x["type"]):
        sorted_group = sorted(g, key=lambda x: get_hand_weight(x["hand"]))
        sorted_hands.extend(sorted_group)

    total = 0

    for i, hand in enumerate(sorted_hands, start=1):
        total += i * hand["bid"]

    print(f"The solution is {total}")


if __name__ == "__main__":
    main()
