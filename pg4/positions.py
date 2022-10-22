def get_positions(sentence, word_list):
    try:
        return str(word_list.index(sentence.split()[0])) + " " + str(word_list.index(sentence.split()[1]))
    except:
        return ' '
