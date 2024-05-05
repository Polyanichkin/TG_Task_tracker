def count_letter(words, letter):
    count = 0
    for word in words:
        if letter in word:
            count += 1
        print(count)


words_dic = ['python', 'c++', 'c', 'scala', 'java']
count_letter(words=words_dic, letter='c')
