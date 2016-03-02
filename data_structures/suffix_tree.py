_end = '_end_'

lines = int(raw_input().strip())
trie = {}


def add(t, word):
    if len(word) == 0:
        return t
    letter = word[0]
    if letter in t:
        t[letter] = add(t[letter], word[1:])
        return t
    else:
        t[letter] = add({}, word[1:])
        return t


def find(found, word, vocabulary):
    if len(word) > 0:
        letter = word[0]
        if letter in vocabulary:
            return find(found, word[1:], vocabulary[letter])
        else:
            return found
    else:
        if vocabulary == {}:
            return 1
        for letter in vocabulary.keys():
            found += find(found, word, vocabulary[letter])
        return found


for i in xrange(0, lines):
    cmd = raw_input().split(" ")
    if cmd[0] == "add":
        trie = add(trie, cmd[1].strip())
    elif cmd[0] == "find":
        print find(0, cmd[1].strip(), trie)
