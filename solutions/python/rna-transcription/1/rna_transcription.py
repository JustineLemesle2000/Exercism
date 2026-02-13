def to_rna(dna_strand):
    rna = ["G", "C", "T", "A"]
    res = ""
    for index, item in enumerate(dna_strand) :
        if "G" in dna_strand[index] : 
            res += "C"
        if "C" in dna_strand[index] :
            res += "G"
        if "T" in dna_strand[index] :
            res += "A"
        if "A" in dna_strand[index] :
            res += "U"
    return res 
