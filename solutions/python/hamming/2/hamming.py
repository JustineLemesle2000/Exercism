"""Calcul de la distance de Hamming"""
def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b) :
        raise ValueError("Strands must be of equal length.")
    return sum(ADN != ADN2 for ADN, ADN2 in zip(strand_a, strand_b))
