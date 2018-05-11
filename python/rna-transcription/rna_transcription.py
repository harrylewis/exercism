def to_rna(dna_strand):
    rna = []
    transpose = {"A": "U", "T": "A", "C": "G", "G": "C"}
    for base in list(dna_strand):
        if base not in ["A", "T", "C", "G"]:
            return ""
        rna.append(transpose[base])
    return "".join(rna)
        
