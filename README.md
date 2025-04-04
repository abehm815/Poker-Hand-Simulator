# Poker Hand Evaluator & Simulator

A Python-based poker hand evaluation and simulation engine for Texas Hold'em. This project allows you to identify the best possible hand from a group of cards and simulate outcomes against one or more opponents to determine win, tie, and loss probabilities.

This tool is useful for understanding poker hand strength, calculating equity in different game scenarios, building AI for poker games, or running statistical experiments.

## Features

- Full hand evaluation engine for Texas Hold'em
- Detects all major hand types (High Card through Royal Flush)
- Simulates games against any number of opponents
- Supports known/unknown opponent cards and community cards
- Object-oriented design for extensibility and integration
- Includes detailed example usage

## File Structure

- `Card.py`: Defines the `Card` class, including comparison operators and card value logic.
- `Deck.py`: Defines a standard 52-card `Deck` with draw, shuffle, and reset functionality.
- `HandIdentifier.py`: Evaluates a set of cards to determine the strongest 5-card poker hand.
- `Simulation.py`: Simulates complete games and calculates win/tie/loss statistics.
- `example_usage.py`: Demonstrates how to use the evaluator and simulation components.

## Requirements

- Python 3.10 or higher
- No external dependencies (uses Python standard library only)

## Installation

Clone this repository:

```bash
git clone https://github.com/abehm815/Poker-Hand-Simulator.git
cd poker-hand-simulator
```

## Usage

### Hand Evaluation Example

You can pass 7 cards to the `HandIdentifier` class to get the best 5-card poker hand:

```python
from HandIdentifier import HandIdentifier
from Card import Card

hand = [
    Card('AS'),
    Card('AC'),
    Card('KC'),
    Card('KD'),
    Card('5H'),
    Card('6H'),
    Card('TC'),
]

identifier = HandIdentifier(hand)
print(identifier.getMainHand())  # Best 5-card hand
print(identifier.getType())      # HandType.FULL_HOUSE
```

### Simulation Example

Simulate the outcome of a hand against multiple unknown opponents:

```python
from Simulation import Simulation
from Card import Card

playerHand = [Card("AS"), Card("AH")]
sim = Simulation(playerHand=playerHand, numOpps=5)

for _ in range(10000):
    sim.runSim()

wins, ties, losses = sim.getOutcomes()
print("Equity (win rate):", wins / sim.numSims)
```

### Partial Information Example

You can simulate scenarios where some community or opponent cards are known:

```python
from Simulation import Simulation
from Card import Card

playerHand = [Card("AS"), Card("AH")]

# Flop known
communityCards = [
    Card('AD'),
    Card('AC'),
    Card('9C'),
]

# Two opponent hands known
opponentHands = [
    [Card('KH'), Card('KC')],
    [Card('7D'), Card('8D')]
]

sim = Simulation(
    playerHand=playerHand,
    knownComCards=communityCards,
    knownOppCards=opponentHands,
    numOpps=5
)

for _ in range(10000):
    sim.runSim()

print("Equity:", sim.wins / sim.numSims)
```

## Full Example Output

The `example_usage.py` file demonstrates usage with many hand types and simulation cases.

### Hand Identification Output Example

```
Two Pair Example
------------------------------
Main Hand: [[AS], [AC], [KC], [KD], [TC]]
Hand Type: TWO_PAIR
```

### Simulation Output Example

```
Case 1: 6 Opponents, All Community Cards Unknown
--------------------------------------------------
Player's Hand: [[AS], [AH]]
Opponents: 6
Equity: 0.6421
```

```
Case 2: 3 Opponents, All Community Cards Known
--------------------------------------------------
Player's Hand: [[AS], [AH]]
Community Cards: [[AD], [AC], [TC], [7S], [4H]]
Opponents: 3
Equity: 1.0000
```

```
Case 3: 9 Opponents, Only Flop Known
--------------------------------------------------
Player's Hand: [[TS], [TC]]
Community Cards: [[AD], [AC], [9C]]
Opponents: 9
Equity: 0.2940
```

```
Case 4: 5 Opponents, 2 Known Opponent Hands, 4 Community Cards Known
--------------------------------------------------
Player's Hand: [[TS], [TC]]
Community Cards: [[AD], [AC], [9C], [3S]]
Known Opponent Hands: [[AS, KC], [JH, 2D]]
Opponents: 5
Equity: 0.5650
```

## Customization

This engine can be extended or modified to support:

- Omaha or other poker variants
- Tracking hand histories or odds over time
- Visualizing hand strengths and equity curves
- Building bots or training AI poker agents
- Integration into online poker apps or games

## Author

Developed by Alex Behm. Contributions, feedback, and suggestions are welcome.
