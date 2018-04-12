import random
import string

def generator():
    print('App store 激活码生成 200')
    # 激活码格式 10位 并且没有规律
    length = 10
    charset = string.ascii_letters + string.digits
    codes = {''.join([random.choice(charset) for j in range(length)]) for i in range(200)}
    print(codes)
    print('lenth:', len(codes))
    output(codes)


def output(data):
    count = 0
    with open('result.txt', 'w') as f:
        for item in data:
            count += 1
            f.write('No.%s %s \n' % (str(count).ljust(3), item))


if __name__ == '__main__':
    generator()
