_count = "count"
lines = int(raw_input().strip())
trie = {}


def add(t, word):
    if len(word) == 0:
        return (t, 1)
    letter = word[0]
    if letter in t:
        t[letter], cumulative_count = add(t[letter], word[1:])
        t[_count] = t[_count] + cumulative_count if _count in t else cumulative_count
        return (t, cumulative_count)
    else:
        t[letter], cumulative_count = add({}, word[1:])
        t[_count] = t[_count] + cumulative_count if _count in t else cumulative_count
        return (t, cumulative_count)


def find(found, word, vocabulary):
    if len(word) > 0:
        letter = word[0]
        if letter in vocabulary:
            return find(found, word[1:], vocabulary[letter])
        else:
            return found
    else:
        return vocabulary[_count]


for i in xrange(0, lines):
    cmd = raw_input().split(" ")
    if cmd[0] == "add":
        trie, cumulative_count = add(trie, cmd[1].strip() + "$")
    elif cmd[0] == "find":
        print find(0, cmd[1].strip(), trie)