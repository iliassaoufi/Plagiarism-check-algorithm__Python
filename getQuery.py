import re


def text_to_query(text):
    sentenceEnders = re.compile('[.!?›«»—]')
    sentenceList = sentenceEnders.split(text)
    nbr_word = 23
    split_text = []
    for sentence in sentenceList:
        if sentence != "":
            if len(sentence) >= nbr_word:
                splited_sebtence = split_by_nbr_word(nbr_word, sentence)
                split_text.extend(splited_sebtence)
            else:
                split_text.append(sentence)

    return split_text


def split_by_nbr_word(n, sentence):
    list = sentence.split()
    nbr_split = int(len(list)/n)+1
    result = []

    for k in range(nbr_split):
        temp = list[n*k: n*(k+1)]
        if(len(temp) < 1):
            continue
        result.append(" ".join(temp))

    return result


# text = "Le marketing Business to Business (B to B) est le marketing des entreprises qui vendent des biens ou des services à d’autres professionnels. Le marketing B to B est parfois appelé en français marketing d’entreprise à entreprise, marketing industriel, marketing professionnel, ou encore marketing d’affaires. Le marketing B to B n’est, à priori, pas une matière que l’on pourrait imaginer passionnante, or en l’étudiant de plus près, on s e rend compte que l’on a beaucoup à apprendre et combien cela peut être enrichissant."

# print(text_to_query(text))
