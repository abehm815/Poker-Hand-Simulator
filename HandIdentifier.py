from collections import Counter
from Card import Card
from enum import Enum

# Enum defining possible poker hand rankings
class HandType(Enum):
    HIGH_CARD = 0
    PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8
    ROYAL_FLUSH = 9

class HandIdentifier:
    """
    Identifies the strongest 5-card poker hand from a list of 7 cards.
    """
    def __init__(self, cards: list[Card]) -> None:
        """
        Accepts 7 cards (e.g., 2 hole cards + 5 community cards),
        and identifies the best possible 5-card poker hand.
        """
        self.cards = cards
        self.type = HandType.HIGH_CARD #Represents the type of the best hand
        self.mainHand = [] #Represents the best 5 card hand 
        self.identifyHand()

    def identifyHand(self):
        """
        Main logic flow for hand evaluation.
        Checks pair-related hands first, then flush/straight-related hands.
        """
        self.checkForPairHands()
        self.checkForFlushStraightHands()

         # Default fallback if no stronger hand found
        if self.type == HandType.HIGH_CARD:
            self.mainHand = self.cards[:5]

    def checkForPairHands(self) -> None:
        """
        Checks for pairs, two pair, trips, full house, and quads.
        """
        self.cards.sort(reverse=True)
        rank_counts = Counter(card.rank for card in self.cards)
        count_values = sorted(rank_counts.values(), reverse=True)
        self.mainHand.clear()

        #Checks for a four of a kind 
        if count_values[0] == 4:
            self.checkFourOfAKind(rank_counts)
            return
        #Checks for a full house
        if count_values[0] >= 3 and (count_values[1] >= 2 or count_values[1] == 3):
            self.checkFullHouse(rank_counts)
            return
        #Checks for a three of a kind
        if count_values[0] == 3:
            self.checkThreeOfAKind(rank_counts)
            return
        #Checks for a two pair
        if count_values[0] == 2 and count_values[1] == 2:
            self.checkTwoPair(rank_counts)
            return
        #Checks for a pair 
        if count_values[0] == 2:
            self.checkPair(rank_counts)
            return

    def checkForFlushStraightHands(self):
        """
        Checks for flush, straight, straight flush, and royal flush.
        """
        flushCards = self.getFlushCards()
        if flushCards:
            if self.checkRoyalFlush(flushCards):
                return
            if self.checkStraightFlush(flushCards):
                return
            if self.type.value < HandType.FLUSH.value:
                self.mainHand = flushCards[:5]
                self.type = HandType.FLUSH
            return
        
        self.checkStraight()

    def checkRoyalFlush(self, flushCards):
        """
        Checks if flush cards form a royal flush.
        """
        flush_ranks = [card.rank for card in flushCards[:5]]
        if flush_ranks == ['A', 'K', 'Q', 'J', 'T']:
            self.mainHand = flushCards
            self.type = HandType.ROYAL_FLUSH
            return True
        return False
    
    def checkStraightFlush(self, flushCards):
        """
        Checks if flush cards form a straight flush.
        """
        flushStraight = self.getHighestStraight(flushCards, True)
        if flushStraight:
            self.type = HandType.STRAIGHT_FLUSH
            self.mainHand = flushStraight
            return True
        return False
    
    def checkStraight(self):
        """
        Checks if a straight is present, including low-Ace straight.
        """
        straightCards = self.getHighestStraight(self.cards, False)
        if not straightCards:
            straightCards = self.getHighestStraight(self.cards, True)
        if straightCards:
            self.type = HandType.STRAIGHT
            self.mainHand = straightCards

    def getHighestStraight(self, cards: Card, aceLow: bool) -> list[Card]:
        """
        Returns the highest straight (if any) from a set of cards.
        Handles duplicates and optionally ace-low straights.
        """
        
        unique_cards = []

        highestRank = 0
        highestStraight = None

        seen_ranks = set()
        for card in cards:
            if card.rank not in seen_ranks:
                unique_cards.append(card)
                seen_ranks.add(card.rank)

        if aceLow:
            ace_cards = [card for card in unique_cards if card.rank == "A"]
            for card in ace_cards:
                unique_cards.remove(card)
            unique_cards.extend(ace_cards)

        for i in range(len(unique_cards) - 4): 
            straight = unique_cards[i:i+5]
            if straight[0].getValue(aceLow) - straight[4].getValue(aceLow) == 4:
                if straight[0].value > highestRank:
                    highestStraight = straight
                    highestRank = straight[0].value
                
        return highestStraight

    def getFlushCards(self) -> list[Card]:
        """
        Returns 5+ cards of the same suit if flush is possible.
        """
        suit_dict = {'S': [], 'H': [], 'D': [], 'C': []}
        for card in self.cards:
            suit_dict[card.suit].append(card)
        for suit_cards in suit_dict.values():
            if len(suit_cards) >= 5:
                return sorted(suit_cards, reverse=True)
        return None

    def checkFourOfAKind(self, rank_counts) -> bool:
        """Builds main hand with four of a kind and top kicker."""
        four_of_a_kind_rank = [rank for rank, count in rank_counts.items() if count == 4]
        four_of_a_kind_cards = [card for card in self.cards if card.rank == four_of_a_kind_rank[0]]
        self.mainHand.extend(four_of_a_kind_cards)
        self.type = HandType.FOUR_OF_A_KIND
        self.mainHand.extend(sorted([card for card in self.cards if card.rank != four_of_a_kind_rank[0]], reverse=True)[:1])
    
    def checkFullHouse(self, rank_counts) -> bool:
        """Builds main hand for full house: three of a kind + pair."""
        three_of_a_kind_ranks = sorted((rank for rank, count in rank_counts.items() if count >= 3),key=lambda rank: "23456789TJQKA".index(rank),reverse=True)
        three_of_a_kind_rank = three_of_a_kind_ranks[0]
        pair_ranks = sorted((rank for rank, count in rank_counts.items() if count >= 2 and rank != three_of_a_kind_rank),key=lambda rank: "23456789TJQKA".index(rank),reverse=True)
        pair_rank = pair_ranks[0]
        self.mainHand.extend([card for card in self.cards if card.rank == three_of_a_kind_rank][:3])
        self.mainHand.extend([card for card in self.cards if card.rank == pair_rank][:2])
        self.type = HandType.FULL_HOUSE
    
    def checkThreeOfAKind(self, rank_counts) -> bool:
        """Builds three-of-a-kind hand with two kickers."""
        three_of_a_kind_rank = [rank for rank, count in rank_counts.items() if count == 3]
        three_of_a_kind_cards = [card for card in self.cards if card.rank == three_of_a_kind_rank[0]]
        self.mainHand.extend(three_of_a_kind_cards)
        self.type = HandType.THREE_OF_A_KIND
        self.mainHand.extend(sorted([card for card in self.cards if card.rank != three_of_a_kind_rank[0]], reverse=True)[:2])
    
    def checkTwoPair(self, rank_counts) -> bool:
        """Builds two pair hand with top kicker."""
        two_pair_ranks = [rank for rank, count in rank_counts.items() if count == 2]
        two_pair_ranks.sort(key=lambda rank: "23456789TJQKA".index(rank), reverse=True)
        self.mainHand.extend([card for card in self.cards if card.rank == two_pair_ranks[0]])
        self.mainHand.extend([card for card in self.cards if card.rank == two_pair_ranks[1]])
        self.type = HandType.TWO_PAIR
        potential_kickers = sorted([card for card in self.cards if card not in self.mainHand],reverse=True)
        if potential_kickers:
            self.mainHand.append(potential_kickers[0])
    
    def checkPair(self, rank_counts) -> bool:
        """Builds one pair hand with three kickers."""
        pair_rank = [rank for rank, count in rank_counts.items() if count == 2]
        single_pair_cards = [card for card in self.cards if card.rank == pair_rank[0]]
        self.mainHand.extend(single_pair_cards)
        self.type = HandType.PAIR
        #Maybe 4
        self.mainHand.extend(sorted([card for card in self.cards if card.rank != pair_rank[0]], reverse=True)[:3])

    def getType(self) -> HandType:
        """Returns the evaluated hand type (enum)."""
        return self.type

    def getMainHand(self) -> list[Card]:
        """Returns the five cards that make up the best hand."""
        return self.mainHand

    def __eq__(self, handIdentifier: object) -> bool:
        """Equality comparison based on hand type and card values."""
        if handIdentifier.getType() != self.type:
            return False
        otherHand = handIdentifier.getMainHand()
        for i in range(5):
            if self.mainHand[i].getValue() != otherHand[i].getValue():
                return False
        return True

    def __gt__(self, handIndentifier: object) -> bool:
        """Greater-than comparison between two poker hands."""
        otherHandValue = handIndentifier.getType().value
        if self.type.value > otherHandValue: 
            return True 
        if self.type.value < otherHandValue:
            return False
        
        otherHand = handIndentifier.getMainHand()
        for i in range(5):
            if self.mainHand[i].getValue() > otherHand[i].getValue():
                return True
        return False

    def __repr__(self) -> str:
        """Returns string representation of the hand type and cards."""
        return f"Hand Type: {self.type.name} | Cards: {self.mainHand}"