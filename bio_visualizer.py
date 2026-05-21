import matplotlib.pyplot as plt

dna_sequence = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAGAGTGTCTGATAGCAGC"

counts = {
    "Adenine (A)": dna_sequence.count("A"),
    "Thymine (T)": dna_sequence.count("T"),
    "Cytosine (C)": dna_sequence.count("C"),
    "Guanine (G)": dna_sequence.count("G")
}

labels = list(counts.keys())
values = list(counts.values())

plt.figure(figsize=(8, 5))
plt.bar(labels, values, color=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'], edgecolor='black')

plt.title("Nucleotide Frequency Distribution in DNA Sequence", fontsize=14, fontweight='bold')
plt.xlabel("Nucleotide Base", fontsize=12)
plt.ylabel("Count (Frequency)", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
