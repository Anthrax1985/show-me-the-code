import os
import re




def process_txt(spath):
    words = []
    with open(spath) as f:
        content = f.read()
        reg = re.compile('\b?(\w+)\b?')
        words = reg.findall(content)


    result = {}
    for word in words:
        word = word.lower()

        if word in ['the', 'and', 'to']:
            continue
        elif word in result:
            result[word] += 1
        else:
            result.update({word:1})

    print(spath)
    # print(result)
    print(sorted(result.items(), key=lambda x: x[1], reverse=True))


if __name__ == '__main__':
    for txt in os.listdir('txt'):
        process_txt('txt/' + txt)