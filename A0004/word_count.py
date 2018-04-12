import operator
def word_count():
    issue = ''
    with open('sample.txt', 'r') as f:
        issue += f.read()
    # 处理标点
    issue = issue.replace(',', ' ')
    issue = issue.replace('"', ' ')
    issue = issue.replace('.', ' ')
    issue = issue.replace('\n', ' ')

    words = issue.split(' ')
    word_counter = {}

    for word in words:

        if word == '' or word == ' ':
            continue

        if "'" in word:
            print(word)
            word = word.split("'")[0]

        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1

    print(sorted(word_counter.items(), key= lambda x:x[1] ,reverse = True))


if __name__ == '__main__':
    word_count()