# -*- coding: utf-8 -*-
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def read_config():
    with open('./Config/config.txt', 'r', encoding='utf-8') as fConfig:
        value = []
        config = {}
        for line in fConfig.readlines():
            key = line.strip().split('=')[0]
            value = line.strip().split('=')[1]
            config[key] = value
    print(config)
    return config


def main():
    fileNameList = []
    with open('./Input/FileNameList.txt', 'r', encoding='gbk') as fName:
        for line in fName.readlines():
            fileNameList.append(line.strip())

    textList = []
    for i in range(len(fileNameList)):
        with open('./Input/' + fileNameList[i] + '.txt', 'r', encoding='utf-8') as f:
            text = []
            for line in f.readlines():
                text.append(line.strip())
            print(text)
        textList.append(text)
    print(textList)

    freqList = []
    for i in range(len(fileNameList)):
        freq = []
        for j in range(len(textList[i])):
            freq.append(len(textList[i]) - j)
        print(freq)
        freqList.append(freq)
    print(freqList)

    config = read_config()
    for i in range(len(fileNameList)):
        dict = {}
        for j in range(len(textList[i])):
            dict[textList[i][j]] = freqList[i][j]
        print(dict)
        wordcloud = WordCloud(font_path=config['font_path'],
                              background_color=config['background_color'],
                              prefer_horizontal=float(config['prefer_horizontal']),
                              colormap=config['colormap'],
                              width=int(config['width']),
                              height=int(config['height']),
							  relative_scaling=float(config['relative_scaling'])
                              )
        wordcloud.generate_from_frequencies(dict)
        plt.imshow(wordcloud)
        plt.axis('off')
        wordcloud.to_file('./Output/' + fileNameList[i] + '.png')


if '__name__=__main__':
    main()
