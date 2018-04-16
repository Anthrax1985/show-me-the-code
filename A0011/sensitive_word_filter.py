

words_list = []

def word_check():
    element = input('请输入你想检查的词语')
    print('Freedom') if element in words_list else print('Human Rights')


def get_words():
    with open('filtered_words.txt', 'r') as f:
        words = f.read()
        words_list.extend(words.split('\n'))
    print(words_list)

def word_recover():
    element = input('请输入你想检查的词语')
    # 最搓实现
    for word in words_list:
        element = element.replace(word, '*'*len(word))
    print(element)


if __name__ == '__main__':
    get_words()    # A0011
    # word_check() # A0012
    word_recover()