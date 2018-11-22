# text keywords

> 文本关键词抽取

## 目录
- data
    - 存放数据

- jieba_keywords
    - 直接利用jieba实现基于tfidf和textrank的文本关键词提取。
    
- rake_keywords
    - 根据[RAKE](https://www.researchgate.net/publication/227988510_Automatic_Keyword_Extraction_from_Individual_Documents)算法提取关键词。
    - step1: 根据停用词划分短语
    - step2: 计算短语中字出现频率(freq)以及字与其他字连接个数(deg)
    - step3: 计算每个字得分(score_word = deg(word)/freq(word))
    - step4: 计算短语得分(score_phrase = sum(score_word in phrase))
    - step5: 根据短语得分排序输出
    - 注意：针对特定领域，最好添加相关重要短语

