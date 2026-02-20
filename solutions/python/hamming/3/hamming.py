"""Calcul de la distance de Hamming"""
def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b) :
        raise ValueError("Strands must be of equal length.")
    return sum(adn != adn2 for adn, adn2 in zip(strand_a, strand_b))
