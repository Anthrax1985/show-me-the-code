import os


def code_count(spath):
    result = []
    result.append(('title', 'blank lines', 'comment lines', 'code lines'))
    for file in os.listdir(spath):
        if os.path.splitext(file)[1] != '.py':
            continue
        blank = 0
        code = 0
        comment = 0
        with open(spath + file) as f:
            lines = f.readlines()
            for line in lines:
                # print('%r' % line)
                if len(line.strip('\n')) == 0:
                    blank += 1
                elif line.strip(' ').startswith('#'):
                    comment +=1
                else:
                    code += 1
        result.append((file, blank, comment, code))
    print(result)


if __name__ == '__main__':
    code_count('/Users/sunwen/PycharmProjects/crawlProject/house_lianjia/')