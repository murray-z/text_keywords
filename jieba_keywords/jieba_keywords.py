# -*- coding: utf-8 -*-


import jieba
import jieba.analyse


STOPWORDS = '../data/stop_words.txt'

# 设置停用词
jieba.analyse.set_stop_words(STOPWORDS)


class JiebaKeywords():
    def tfidf_keywords(self, text, topk=10):
        return jieba.analyse.extract_tags(text, topK=topk, withWeight=True)


    def textrank_keywords(self, text, topk=10):
        return jieba.analyse.textrank(text, topK=topk, withWeight=True)


    def similarity(self, text, topk=10, method='tfidf'):
        """
        :param text: 文本内容
        :param topk: 返回关键词数目
        :param method: 方法： “tfidf|textrank”
        :return:
        """
        if method not in ['tfidf', 'textrank']:
            return "method should in ['tfidf', 'textrank'] !"

        if method == 'tfidf':
            return self.tfidf_keywords(text, topk=topk)

        if method == 'textrank':
            return self.textrank_keywords(text, topk=topk)


if __name__ == '__main__':
    text = """

    近日，一款名为“拼少少”的社交电商对外宣布即将上线，不仅和拼多多一样涉及的是社交电商领域，而且名字、商标也类似。这是在蹭“大哥”拼多多的热度？

    记者调查后发现，和拼多多平台上海量的商家不同，拼少少的模式是优选商家入驻，学习小米有品，优选商品，做极致单品，让消费者无需过多的选择，总结其模式为“优选单品+社交+低价”，从品控上解决拼多多山寨、假冒等问题。

    目前，平台还处于内测阶段，其官方回应明年上线。

    """
    similarity = JiebaKeywords()

    print(similarity.similarity(text, method='tfidf'))

    print(similarity.similarity(text, method='textrank'))


