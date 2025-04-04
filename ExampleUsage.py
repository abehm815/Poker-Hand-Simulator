from HandIdentifier import HandIdentifier
from Simulation import Simulation
from Card import Card

def handIdentifierUsage():
    print('\nHand Identifier Usage')
    print('_' * 50)

    #Pair example
    hand = [
        Card('QS'),
        Card('5C'),
        Card('QC'),
        Card('KD'),
        Card('3H'),
        Card('6H'),
        Card('TC'),
    ]
    id = HandIdentifier(hand)
    print(id.mainHand)
    print(id.type)

    #Two pair example 
    hand = [
        Card('AS'),
        Card('AC'),
        Card('KC'),
        Card('KD'),
        Card('5H'),
        Card('6H'),
        Card('TC'),
    ]
    id = HandIdentifier(hand)
    print(id.mainHand)
    print(id.type)

    #Three of a kind example
    hand = [
        Card('7S'),
        Card('AS'),
        Card('KH'),
        Card('JC'),
        Card('5C'),
        Card('7H'),
        Card('7C'),
    ]

    id = HandIdentifier(hand)
    print(id.mainHand)
    print(id.type)

    #Four of a kind example
    hand = [
        Card('8S'),
        Card('AS'),
        Card('8H'),
        Card('JC'),
        Card('5C'),
        Card('8H'),
        Card('8C'),
    ]
    id = HandIdentifier(hand)
    print(id.mainHand)
    print(id.type)

    #Full House example
    hand = [
        Card('KS'),
        Card('KS'),
        Card('8H'),
        Card('JC'),
        Card('KC'),
        Card('JH'),
        Card('8C'),
    ]
    id = HandIdentifier(hand)
    print(id.mainHand)
    print(id.type)

    #Straight Example
    hand = [
        Card('4S'),
        Card('5S'),
        Card('8H'),
        Card('JC'),
        Card('KC'),
        Card('6H'),
        Card('7C'),
    ]
    id = HandIdentifier(hand)
    print(id.mainHand)
    print(id.type)

    #Flush Example
    hand = [
        Card('AH'),
        Card('5S'),
        Card('JH'),
        Card('4C'),
        Card('KH'),
        Card('TH'),
        Card('7H'),
    ]
    id = HandIdentifier(hand)
    print(id.mainHand)
    print(id.type)

    #Straight Flush Example
    hand = [
        Card('AH'),
        Card('5S'),
        Card('4H'),
        Card('3H'),
        Card('5H'),
        Card('2H'),
        Card('7S'),
    ]
    id = HandIdentifier(hand)
    print(id.mainHand)
    print(id.type)

    #Royal Flush Example
    hand = [
        Card('AH'),
        Card('KS'),
        Card('KH'),
        Card('JH'),
        Card('QH'),
        Card('TH'),
        Card('7S'),
    ]
    id = HandIdentifier(hand)
    print(id.mainHand)
    print(id.type)

def simulationUsage():
    print('\nSimulation Usage')
    print('_' * 50)
    

    print('\nCase 1: 6 opponents, all unknown community cards')
    print('_' * 30)
    playerHand = [
        Card("AS"),
        Card("AH")
    ]
    s = Simulation(playerHand=playerHand, numOpps=6)
    #Run 1000 simulations
    for i in range(1000):
        s.runSim()
    equity = s.wins / s.numSims
    print(f"Player's Hand: {playerHand}")
    print(f"Opponents: 6")
    print(f"equity: {equity}")

    #Use case two, 3 opponents, all community cards known
    print('\nCase 2: 3 opponents, all community cards known')
    print('_' * 30)
    playerHand = [
        Card("AS"),
        Card("AH")
    ]

    comCards = [
        Card('AD'),
        Card('AC'),
        Card('TC'),
        Card('7S'),
        Card('4H'),

    ]
    s = Simulation(playerHand=playerHand, knownComCards=comCards, numOpps=3)
    #Run 1000 simulations
    for i in range(1000):
        s.runSim()
    #Print equity and player's hand and the community cards
    equity = s.wins / s.numSims
    print(f"Player's Hand: {playerHand}")
    print(f"Community Cards: {comCards}")
    print(f"Opponents: 3")
    print(f"equity: {equity}")

    #Use case three, 9 opponents, only three community cards known (flop)
    print('\nCase 3: 9 Opponents, only three community cards known (Flop)')
    print('_' * 30)
    playerHand = [
        Card("TS"),
        Card("TC")
    ]

    comCards = [
        Card('AD'),
        Card('AC'),
        Card('9C'),
    ]
    s = Simulation(playerHand=playerHand, knownComCards=comCards, numOpps=9)
    #Run 8000 simulations
    for i in range(1000):
        s.runSim()
    #Print equity and player's hand and the community cards
    equity = s.wins / s.numSims
    print(f"Player's Hand: {playerHand}")
    print(f"Community Cards: {comCards}")
    print(f"Opponents: 9")
    print(f"equity: {equity}")

    print('\nCase 4: 5 opponents, two opponents hands are known, 4 community cards are known')
    print('_' * 30)
    playerHand = [
        Card("TS"),
        Card("TC")
    ]

    comCards = [
        Card('AD'),
        Card('AC'),
        Card('9C'),
        Card('3S'),
    ]

    oppCards = [
        [Card('AS'), Card('KC')],
        [Card('JH'), Card('2D')],
    ]

    s = Simulation(playerHand=playerHand, knownComCards=comCards, knownOppCards=oppCards, numOpps=5)
    #Run 8000 simulations
    for i in range(1000):
        s.runSim()
    #Print equity and player's hand and the community cards
    equity = s.wins / s.numSims
    print(f"Player's Hand: {playerHand}")
    print(f"Community Cards: {comCards}")
    print(f"Opponents: 9")
    print(f"equity: {equity}")

if __name__ == "__main__":
    handIdentifierUsage()
    simulationUsage()