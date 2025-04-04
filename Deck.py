from random import shuffle
from Card import Card

# Definitions for suits and ranks to build a standard 52-card deck
suits = ['H','S','C','D'] # Hearts, Spades, Clubs, Diamonds
ranks = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']

class Deck():
    """
    Represents a standard 52-card deck with functionality for shuffling,
    drawing, removing cards, and resetting the deck.
    """
    def __init__(self):
        """
        Initializes a new deck of 52 cards and an empty list for drawn cards.
        """
        self.deck = self.generateDeck()
        self.drawnCards = []

    def generateDeck(self) -> list[Card]:
        """
        Generates a full 52-card deck using all suit and rank combinations.
        Only called during initialization.
        """
        return [Card(f"{rank}{suit}") for suit in suits for rank in ranks]
    
    def resetDeck(self) -> None:
        """
        Returns all drawn cards back to the deck and resets it to full.
        """
        self.deck.extend(self.drawnCards)
        self.drawnCards.clear()

    def shuffle(self) -> None:
        """
        Randomly shuffles the deck in place.
        """
        shuffle(self.deck)

    def drawTopCard(self) -> Card:
        """
        Draws and returns the top card of the deck. If deck is empty, returns None.
        Drawn card is moved to the drawnCards list.
        """
        if self.deck:
            drawnCard = self.deck.pop()
            self.drawnCards.append(drawnCard)
            return drawnCard
        else:
            return None
        
    def removeCard(self, card: Card):
        """
        Removes a specific card from the deck (if found),
        simulating it being drawn. Logs ValueError if card not found.
        """
        try:
            self.deck.remove(card)
            self.drawnCards.append(card)
        except ValueError:
            print(f"Could not remove card, {card} not found in deck. (Usually happens by passing in duplicate cards as parameters)")
            return None
        
    def __repr__(self) -> str:
        """
        Returns a string representation of the current deck state.
        """
        repString = f"Deck Length: {len(self.deck)}\n"
        for card in self.deck:
            repString += f"{card.__repr__()}\n"
        return repString