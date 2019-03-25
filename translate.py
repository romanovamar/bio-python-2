import sys
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna


# translate.py <sequence>

def frame(seq):
    # moving frame to 3 nucleotides, the same for reverse

    reverse_seq = seq[::-1]
    list = []
    for i in range(3):
        list.append(seq)
        seq = seq[1:]
        list.append(reverse_seq)
        reverse_seq = reverse_seq[1:]
    return list


def to_be_multiple_3(seq):
    # Adding N to make seq divisible by 3

    list = frame(seq)
    frame_list = []
    for f in list:
        if len(f) % 3 == 0:
            frame_list.append(f)
        elif len(f) % 3 == 1:
            f = f + 'NN'
            frame_list.append(f)
        else:
            f = f + 'N'
            frame_list.append(f)
    return frame_list


def translation(seq):
    frame_list = to_be_multiple_3(seq)
    peptides_list = []
    for i in frame_list:
        i = Seq(i, generic_dna)
        peptides_list.append(str(i.translate(to_stop=True)))
    peptides_list = sorted(peptides_list, key=len)
    for f in peptides_list:
        print(f)


def main():
    if len(sys.argv) != 2:
        print('Usage: task.py <dna sequence>')
        exit()
    seq = str(sys.argv[1])
    print(translation(seq))


if __name__ == '__main__':
    main()
