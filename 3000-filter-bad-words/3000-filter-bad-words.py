
def filterBadwords(badWords, sentence):
    leading = []
    trailing = []
    center = []
    whole = set()
    hashmap = {}
    res = []
    for bad in badWords:
        if bad[0] == "*" and bad[-1] == "*":
            center.append(bad[1:-1])
        elif bad[0] == "*":
            leading.append(bad[1:])
        elif bad[-1] == "*":
            trailing.append(bad[:-1])
        else:
            whole.add(bad)

    for word in sentence.split():
        if word in whole:
            hashmap[word] = "*" * (len(word))
        for bad in leading:
            if (word not in hashmap and len(word) > len(bad) and word[:len(bad)] == bad):
                hashmap[word] = "*" * (len(bad)) + word[len(bad):]
        for bad in trailing:
            if (word not in hashmap and len(word) > len(bad) and word[len(word)-len(bad):] == bad):
                hashmap[word] = word[:len(word) - len(bad)] + "*" * (len(bad))
        for bad in center:
            if (word not in hashmap and len(word) - 2) >= len(bad):
                i = 0
                j = i + len(bad)
                while j < len(word) - 1:
                    if word[i:j] == bad:
                        hashmap[word] = "*" * (len(word))
                        break
                    i += 1
                    j += 1

        if word in hashmap:
            res.append(hashmap[word])
        else:
            res.append(word)

    return "  ".join(res)


if __name__ == "__main__":
    badWord = ["*poop", "poop*", "*poop*", "cunt"]
    sentence = "this is such poopy nonsense man, damn incompoop poop this elpooping shit you cunt"
    print("Input Sentence: ", sentence)
    print("Words to filter: ", badWord)
    censored = filterBadwords(badWord, sentence)
    print("Censored Sentence: ", censored)
