from Bio import SeqIO
from Bio.Align import PairwiseAligner


def align(seq_a, seq_b, fname, mode):
    aligner = PairwiseAligner()

    aligner.mode = mode
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -1

    # Perform the alignment
    alignments = aligner.align(seq_a.seq, seq_b.seq)

    # Get the best alignment (highest score)
    best_alignment = alignments[0]

    # Write the alignment to a file and calculate the score
    with open(fname, 'w') as file:
        file.write(str(best_alignment))
        file.write(f"\nAlignment Score: {best_alignment.score}")

    # Print the score to the console
    print(f"The alignment score is: {best_alignment.score}")


# Read sequences from FASTA files
tyr_human = SeqIO.read("NC_000011.10[human][TYR].fa", "fasta")
mc1r_human = SeqIO.read("NC_000016.10[human][MC1R].fa", "fasta")
tyr_mouse = SeqIO.read("NC_000073.7[mouse][Tyr].fa", "fasta")
mc1r_mouse = SeqIO.read("NC_000074.7[mouse][Mc1r].fa", "fasta")

align(tyr_human, tyr_mouse, "Alignment[TYR][Stretcher].txt", "global")
align(tyr_human, tyr_mouse, "Alignment[TYR][Water].txt", "local")
align(mc1r_human, mc1r_mouse, "Alignment[MC1R][Stretcher].txt", "global")
align(mc1r_human, mc1r_mouse, "Alignment[MC1R][Water].txt", "local")
