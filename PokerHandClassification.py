def findPokerHand(hand):

    ranks = []
    suits = []
    PossibleRanks=[]
    Hands = {"High Card":1, "One Pair":2, "Two Pair":3, "Three of a Kind":4, "Straight":5, 
    "Flush":6, "Full House":7, "Four of a Kind":8, "Straight Flush":9, "Royal Flush":10}

    for card in hand:
        rank = card[:-1]
        suit = card[-1]

        if rank == 'A':
            rank = 14
        elif rank == 'K':
            rank = 13
        elif rank == 'Q':   
            rank = 12
        elif rank == 'J':
            rank = 11

        ranks.append(int(rank))
        suits.append(suit)

    if not ranks:
        return "No cards detected"

    if RoyalFlush(ranks, suits):
        PossibleRanks.append(Hands["Royal Flush"])
    elif StraightFlush(ranks, suits):
        PossibleRanks.append(Hands["Straight Flush"])
    elif FourOfAKind(ranks, suits):
        PossibleRanks.append(Hands["Four of a Kind"])
    elif FullHouse(ranks, suits):
        PossibleRanks.append(Hands["Full House"])
    elif Flush(ranks, suits):
        PossibleRanks.append(Hands["Flush"])
    elif Straight(ranks, suits):
        PossibleRanks.append(Hands["Straight"])
    elif ThreeOfAKind(ranks, suits):
        PossibleRanks.append(Hands["Three of a Kind"])
    elif TwoPair(ranks, suits):
        PossibleRanks.append(Hands["Two Pair"])
    elif OnePair(ranks, suits):
        PossibleRanks.append(Hands["One Pair"])
    else:
        PossibleRanks.append(Hands["High Card"])

    
    

    value = max(PossibleRanks)
    for name, val in Hands.items():
        if val == value:
            print(f"Hand: {name}")
            return name


# Check for Royal Flush
def RoyalFlush(ranks, suits):

    sorted_ranks = sorted(ranks, reverse=True)
    if sorted_ranks == [14, 13, 12, 11, 10] and len(set(suits)) == 1:
        return True
    return False

# Check for Straight Flush
def StraightFlush(ranks, suits):
    if Flush(ranks, suits) and Straight(ranks, suits):
        return True
    return False

# Check for FourOfAKind
def FourOfAKind(ranks, suits):
    if max(ranks.count(rank) for rank in ranks) == 4:
        return True
    return False

# Check for FullHouse
def FullHouse(ranks, suits):
    counts = [ranks.count(rank) for rank in set(ranks)]
    if sorted(counts) == [2, 3]:
        return True
    return False

# Check for Flush
def Flush(ranks, suits):
    if len(ranks) >= 5 and len(set(suits)) == 1:
        return True
    return False

# Check for Straight
def Straight(ranks, suits):
    sorted_ranks = sorted(ranks)
    
    if set(sorted_ranks) != {10, 11, 12, 13, 14}:
        sorted_ranks = [1 if r == 14 else r for r in sorted_ranks]
        sorted_ranks = sorted(sorted_ranks)
    
    if sorted_ranks[-1] - sorted_ranks[0] == 4 and len(set(sorted_ranks)) == 5:
        return True
    return False

# Check for ThreeOfAKind
def ThreeOfAKind(ranks, suits):
    if max(ranks.count(rank) for rank in ranks) == 3:
        return True
    return False

# Check for TwoPair
def TwoPair(ranks, suits):
    pairs = [rank for rank in set(ranks) if ranks.count(rank) == 2]
    if len(pairs) == 2:
        return True
    return False

# Check for OnePair
def OnePair(ranks, suits):
    if max(ranks.count(rank) for rank in ranks) == 2:
        return True
    return False





if __name__ == "__main__":
    findPokerHand(["AH", "KH", "QH", "JH", "10H"])  # Royal Flush
    findPokerHand(["QC", "JC", "10C", "9C", "8C"])  # Straight Flush
    findPokerHand(["9D", "9H", "9S", "9C", "3D"])   # Four of a Kind
    findPokerHand(["KH", "KS", "KC", "8D", "8H"])   # Full House
    findPokerHand(["2H", "5H", "7H", "JH", "KH"])   # Flush
    findPokerHand(["2C", "3C", "4C", "5C", "6S"])   # Straight
    findPokerHand(["QD", "QS", "QC", "7H", "2S"])   # Three of a Kind
    findPokerHand(["10H", "10C", "7S", "7D", "3H"]) # Two Pair
    findPokerHand(["5D", "5H", "9C", "JH", "2S"])   # One Pair
    findPokerHand(["AH", "9C", "7D", "5S", "2H"])   # High Card
