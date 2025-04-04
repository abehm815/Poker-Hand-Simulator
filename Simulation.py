from HandIdentifier import HandIdentifier, HandType
from Deck import Deck
from Card import Card

#Mapping of HandType enums to string descriptions for output readability
handStrTable = {
    HandType.HIGH_CARD : "High Card",
    HandType.PAIR : "Pair",
    HandType.TWO_PAIR : "Two Pair",
    HandType.THREE_OF_A_KIND : "Three Of A Kind",
    HandType.STRAIGHT : "Straight",
    HandType.FLUSH : "Flush",
    HandType.FULL_HOUSE : "Full House",
    HandType.FOUR_OF_A_KIND: "Four of a Kind",
    HandType.STRAIGHT_FLUSH : "Straight FLush",
    HandType.ROYAL_FLUSH : "Royal Flush",
}

class Simulation:

    """
    Simulates a complete round of poker, evaluating the outcome (win/tie/loss)
    for a player's hand against a number of opponents by generating random hands or cards that are not accounted for.
    """

    def __init__(self, playerHand: list[Card], knownComCards: list[Card] = [], knownOppCards: list[list[Card]] = [], numOpps: int = 8):
        """
        Initializes the simulation with player's hole cards, any known community
        or opponent cards, and the number of opponents in the game.
        """
        
        self.knownComCards = knownComCards
        self.knownOppCards = knownOppCards
        self.numOpps = numOpps
        self.playerHand = playerHand

        self.allComCards = None
        self.allOppCards = None

        self.deck = Deck()

        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.numSims = 0

        self.winningOppHands = []
        
    def runSim(self):

        """
        Runs a single simulation round:
        - Fills in unknown cards
        - Compares player's hand to opponents'
        - Updates win/loss/tie stats
        """

        self.deck.resetDeck()
        self.deck.shuffle()
        self.removeKnownCardsFromDeck()
        self.fillAllCards()

        playerHandID = HandIdentifier(self.playerHand + self.allComCards)

        oppHandIDs = []
        for hand in self.allOppCards:
            oppHandID = HandIdentifier(hand + self.allComCards)
            oppHandIDs.append(oppHandID)

        bestOppHand = max(oppHandIDs)

        if playerHandID > bestOppHand:
            self.wins += 1
        
        elif playerHandID == bestOppHand:
            self.ties += 1
        
        else:
            winningOppHandType = handStrTable[bestOppHand.getType()]
            if winningOppHandType not in self.winningOppHands:
                self.winningOppHands.append(winningOppHandType)
            self.losses += 1

        self.numSims += 1

    def removeKnownCardsFromDeck(self):
        """
        Removes any known cards (community, opponents, player) from the deck
        to avoid duplication during simulation.
        """
        for card in self.knownComCards:
            self.deck.removeCard(card)
        for hand in self.knownOppCards:
            for card in hand:
                self.deck.removeCard(card)
        for card in self.playerHand:
            self.deck.removeCard(card)

    def fillAllCards(self):
        """
        Completes the board and opponent hands by drawing the necessary number of cards.
        """
        self.allComCards = self.knownComCards + self.drawComCards()
        self.allOppCards = self.knownOppCards + self.drawOppCards()

    def getOutcomes(self):
        """
        Returns a tuple with the total number of wins, ties, and losses.
        """
        return self.wins, self.ties, self.losses

    def drawComCards(self):
        """
        Draws remaining community cards until there are 5 total.
        """
        return [self.deck.drawTopCard() for _ in range(5 - len(self.knownComCards))]
    
    def drawOppCards(self):
        """
        Draws unknown opponent hands (2 cards per opponent).
        """
        return [[self.deck.drawTopCard() for _ in range(2)] for _ in range(self.numOpps - len(self.knownOppCards))]