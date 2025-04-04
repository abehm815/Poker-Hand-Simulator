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
