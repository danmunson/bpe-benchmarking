import sys
from pathlib import Path
from collections import defaultdict

"""
This is meant to be a readable reference implmentation of BPE.

To run: `python3 simple-bpe.py alice29.txt 10`
- this will run 10 iterations of BPE on the data/alice29.txt file

Note that in Python, a tuple is an immutable, hashable sequence, even when nested.
e.g. x = (1, 2, (3, 4)) is a tuple
"""

def find_new_vocab(data: list) -> list:
    """
    find the most frequent 'character' sequence
    """
    pair_counter = defaultdict(int)
    # collect all pairs in a mapping
    for i in range(1, len(data)):
        pair_counter[(data[i-1], data[i])] += 1
    # get the most frequent pairing
    # use the count as a key for the max function, and get the max key
    most_popular = max(pair_counter.items(), key=lambda x : x[1])[0]
    return most_popular

def update_tokens(data: list, new_vocab: tuple) -> list:
    """
    translate old sequence to new one using the updated vocab
    """
    new_data = []
    i = 1
    while i < len(data):
        if (data[i -1], data[i]) == new_vocab:
            new_data.append(new_vocab)
            i += 2
        else:
            new_data.append(data[i - 1])
            i += 1
    return new_data

if __name__ == "__main__":
    input_name, iterations = sys.argv[1:]
    input_path = Path(__file__).parent.parent.joinpath(f'data/{input_name}') # expect "alice29.txt"
    iterations = int(iterations)

    data: list
    with open(input_path, 'rb') as f:
        data = [num for num in f.read()]

    # BPE loop
    for _ in range(iterations):
        data = update_tokens(data, find_new_vocab(data))
    
    new_vocabulary = list(filter(lambda x : type(x) == tuple, set(data)))

    """
    Expected output for 10 iterations:
        (13, 10)
        (32, 32)
        (100, 32)
        (101, 32)
        (105, 110)
        (32, 116)
        (101, 114)
        (116, 32)
        (32, 97)
        ((32, 116), 104)
    """

    print('\n'.join(list(map(str, new_vocabulary))))
