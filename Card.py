valueTable = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'T': 10,
            'J': 11,
            'Q': 12,
            'K': 13,
            'A': 14, 
}

class Card():
    """
    Represents a single playing card with a rank and suit.
    Supports comparison operators and basic card utility methods.
    """
    
    def __init__(self, cardStr: str) -> None:
        """
        Initializes a card from a string like 'AS' (Ace of Spades).
        """
        self.rank = cardStr[0]
        self.suit = cardStr[1]
        self.value = valueTable[self.rank]

    def getSuit(self) -> str:
        """Returns the suit of the card (e.g., 'H', 'S')."""
        return self.suit

    def getRank(self) -> str:
        """Returns the rank of the card (e.g., 'A', 'K', '9')."""
        return self.rank

    def getValue(self, aceLow: bool = False) -> int:
        """
        Returns the numerical value of the card.
        Ace can be treated as low (1) if specified.
        """
        if aceLow and self.value == 14:
            return 1
        return self.value
    
    def __repr__(self) -> str:
        """Returns a string representation of the card."""
        return f"[{self.rank}{self.suit}]"
    
    def __eq__(self, other) -> bool:
        """Checks if two cards are identical in rank and suit."""
        if isinstance(other, Card):
            return self.suit == other.suit and self.rank == other.rank
        return False
    
    def sameValue(self, other) -> bool:
        """Checks if two cards share the same rank (value)."""
        if isinstance(other, Card):
            return self.value == other.value
        return False
    
    def __lt__(self, other) -> bool:
        """Less-than comparison based on card value."""
        if isinstance(other, Card):
            return self.value < other.value
        return False
    
    def __gt__(self, other) -> bool:
        """Greater-than comparison based on card value."""
        if isinstance(other, Card):
            return self.value > other.value
        return False

    def __le__(self, other) -> bool:
        """Less-than-or-equal comparison based on card value."""
        if isinstance(other, Card):
            return self.value <= other.value
        return False

    def __ge__(self, other) -> bool:
        """Greater-than-or-equal comparison based on card value."""
        if isinstance(other, Card):
            return self.value >= other.value
        return False
