from enum import IntEnum
from itertools import groupby
from pprint import pprint

A = "A"
K = "K"
Q = "Q"
T = "T"
J = "J"


class HandType(IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_KIND = 4
    FULL_HOUSE = 5
    FOUR_KIND = 6
    FIVE_KIND = 7


card_to_weight = {
    A: "D",
    K: "C",
    Q: "B",
    T: "A",
    J: "1",
}


def get_hand_weight(hand: str) -> str:
    output = ""
    for card in hand:
        if card.isdigit():
            output += card
        else:
            output += card_to_weight[card]

    return output


def upgrade_jokers(hand: str, card: str) -> HandType:
    new_hand = hand.replace(J, card)
    print(f"Jokers upgraded to {card} to make {new_hand}")
    return get_hand_type(new_hand)


def get_hand_type(hand: str) -> HandType:
    card_counts = {}

    for card in hand:
        card_counts.setdefault(card, 0)
        card_counts[card] += 1

    if len(card_counts) == 1:
        # all the same
        print("Five of a kind")
        return HandType.FIVE_KIND

    for c, count in card_counts.items():
        if count == 4:
            if c == J or any((_c == J for _c in card_counts.keys())):
                # There's a joker
                print("Joker upgraded: five of a kind")
                return HandType.FIVE_KIND
            else:
                print("Four of a kind")
                return HandType.FOUR_KIND
            
    for c, count in card_counts.items():
        if count == 3:
            if c == J:
                # There are three jokers, upgrade to one of the non-jokers
                # to get 4 or 5 of a kind
                return upgrade_jokers(hand, [_c for _c in hand if _c != J][0])
            if any((_c == J for _c in card_counts.keys())):
                # There is at least one joker, upgrade to the group of three
                # to get 4 or 5 of a kind
                return upgrade_jokers(hand, c)
            elif len(card_counts) == 2:
                print("Full house")
                return HandType.FULL_HOUSE
            else:
                print("Three of a kind")
                return HandType.THREE_KIND

    for c, count in card_counts.items():
        if count == 2:
            if c == J:
                # There are two jokers, if we have three types of cards,
                # there must be another pair, which makes 4 of a kind,
                # else we can make 3 of a kind
                if len(card_counts) == 3:
                    print("Joker upgraded: four of a kind")
                    return HandType.FOUR_KIND
                else:
                    print("Joker upgraded: three of a kind")
                    return HandType.THREE_KIND
            if any((_c == J for _c in card_counts.keys())):
                # There is at least one joker, upgrade to match the pair,
                # to get two pairs, full house, or 3, 4, or 5 of a kind
                return upgrade_jokers(hand, c)
            elif len(card_counts) == 3:
                print("Two pairs")
                return HandType.TWO_PAIR
            else:
                print("One pair")
                return HandType.ONE_PAIR

    if J in card_counts:
        # There's at least one joker and the rest are all distict.
        # Upgrade to the first one to make any above combination
        return upgrade_jokers(hand, [c for c in hand if c != J][0])

    # No jokers :(
    print("High card")
    return HandType.HIGH_CARD


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
