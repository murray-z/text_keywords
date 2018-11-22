# -*- coding: utf-8 -*-

import re
import jieba
import jieba.analyse


"""
针对不同领域，最好在“USER_DIC”中添加该领域中特定短语
"""

# 停用词路径
STOPWORDS = '../data/stop_words.txt'

# 用户自定义字典
USER_DIC = '../data/rake_words.txt'

# jieba加载字典
jieba.load_userdict(USER_DIC)


class RakeKeywords():
    def load_stopwords(self, stopwords_path):
        """加载停用词"""
        with open(stopwords_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f]

    def filter_stopwords(self, text):
        """
        对文本进行分词，并过滤停用词
        :param text:
        :return:
        """
        stopwords = self.load_stopwords(STOPWORDS)
        phrases = []
        for word in jieba.lcut(re.sub('[a-zA-Z\s+]', '', text)):
            if word not in stopwords:
                phrases.append(word)
        return phrases

    def construct_matrix(self, phrases):
        """
        根据短语，构建字矩阵
        :param phrases:
        :return:
        """
        matrix = {}
        str_phrases = '|'.join(phrases)
        set_words = list(set(list(''.join(phrases))))

        for word in set_words:
            matrix[word] = [str_phrases.count(word)]
            for other_word in set_words[:set_words.index(word)] + set_words[set_words.index(word):]:
                matrix[word].append(str_phrases.count(word+other_word)+str_phrases.count(other_word+word))
        return matrix

    def calculate_score_words(self, matrix):
        """
        计算每个字得分， score = deg(word) / freq(word)
        :param matrix:
        :return:
        """
        scores = {}
        words = matrix.keys()
        for word in words:
            scores[word] = sum(matrix[word][1:])*1.0/matrix[word][0]
        return scores

    def keywords(self, text, topk=5):
        """
        提取关键词
        :param text:
        :param topk: 返回关键词数量
        :return:
        """
        phrases = self.filter_stopwords(text)
        matrix = self.construct_matrix(phrases)
        scores = self.calculate_score_words(matrix)
        set_phrases = set(phrases)

        # 存放每个短语得分
        score_phrases = {}
        for phrase in set_phrases:
            score = 0
            for word in phrase:
                score += scores[word]
            score_phrases[phrase] = score

        # 对短语进行排序，返回指定个数关键词
        sorted_score_phrase = sorted(score_phrases.items(), key=lambda x: x[1], reverse=True)[:topk]
        return sorted_score_phrase


if __name__ == '__main__':
    text = """深度学习(DL, Deep Learning)是计算机科学机器学习(ML, Machine Learning)领域中一个新的研究方向,它被引入机器学习使其更接近于最初的目标-人工智能(AI, Artificial Intelligence)。深度学习是学习样本数据的内在规律和表示层次,这些学习过程中获得的信息对诸如文字,图像和声音等数据的解释有很大的帮助。它的最终目标是让机器能够像人一样具有分析学习能力,能够识别文字、图像和声音等数据。 深度学习是一个复杂的机器学习算法,在语音和图像识别方面取得的效果,远远超过先前相关技术。它在搜索技术,数据挖掘,机器学习,机器翻译,自然语言处理,多媒体学习,语音,推荐和个性化技术,以及其他相关领域都取得了很多成果。深度学习使机器模仿视听和思考等人类的活动,解决了很多复杂的模式识别难题,使得人工智能相关技术取得了很大进步。将深度学习与各种实际应用研究相结合也是一项很重要的工作。 本文整理和总结了国内外关于深度学习的发展历程和最新的研究成果,对人工神经网络及经典的卷积神经网络所涉及到的概念和算法进行了简要介绍,将卷积神经网络算法进行了改进并应用于光学字符识别(OCR, Optical Character Recognition)和交通标示识别(TSR, Traffic sign recognition)问题,分别在理论和应用层面对卷积神经网络的架构和性能进行研究分析。"""
    rake = RakeKeywords()
    keywords = rake.keywords(text)
    print(keywords)

