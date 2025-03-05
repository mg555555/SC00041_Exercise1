
from Bio import SeqIO
import matplotlib.pyplot as plt
import sys
import os

def gc_content(seq):
    """Calculate GC content percentage in a DNA sequence."""
    gc_count = seq.count("G") + seq.count("C")
    return (gc_count / len(seq)) * 100 if len(seq) > 0 else 0

input_fasta = sys.argv[1]
output_file = sys.argv[2]
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Read sequence from FASTA
record = next(SeqIO.parse(input_fasta, "fasta"))
sequence = str(record.seq)

# Compute GC content in sliding windows
window_size = 50
gc_values = [gc_content(sequence[i:i+window_size]) for i in range(0, len(sequence), window_size)]

# Plot GC content
plt.figure(figsize=(8,4))
plt.plot(gc_values, marker="o", linestyle="-", color="green")
plt.xlabel("Window number")
plt.ylabel("GC Content (%)")
plt.title("GC Content Across DNA Sequence")
plt.grid(True)
plt.savefig(output_file)

print(f"Plot saved at {output_file}")
