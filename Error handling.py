import re
import sys
import random



def process_line(seq_id, prev, mutation, pos_mutation):
    #print(f"{seq_id: >22} {prev}->{mutation} {pos_mutation}")
    pass

def process_file(filename, SNP):

    try:

        with open(filename) as f:
            print("SEQ_ID | MUTATIONS | POSITION-OF-MUTATION")
            num_of_mut = int(re.sub('\D', '', str(SNP)))

            for line in f:
                line = line.strip()
                seq_id = re.split(r'\s+', line)[0]
                
                if num_of_mut > len(line):
                    print('X in SNPX is bigger than the length of the shortest string in a file')
                    num_of_mut = len(line)

                for num in range(1, num_of_mut + 1):

                    pos_mutation = random.randint(1, len(line) - 1)
                    prev = line[pos_mutation]
                    mutation = ''.join(random.sample('ACTG', 1))

                    process_line(seq_id, prev, mutation, pos_mutation)

    except FileNotFoundError:
        print('No such file')
        exit()


def main():
    if len(sys.argv) < 3:
        print("Usage: script.py <path-to-seqs> <define SNP>")
        exit()
    filename = sys.argv[1]
    SNP = sys.argv[2]
    process_file(filename, SNP)


if __name__ == '__main__':
    main()
