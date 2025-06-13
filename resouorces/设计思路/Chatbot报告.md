---
mindmap-plugin: basic
---

# Chatbot Report

## Introduction
- 可以照搬前面的，做点小修改

## Project Methodology
- 可以从design那块提取方法论（比如监督学习，序列标注，LLM辅助生成训练数据等等），具体怎么分我问问AIT的同学

## Design of the System
- 1. intent classification模型
    - 从学生手册，“大马口袋”公众号上截取学校指南内容，整理为json数据库
    - 将所有数据中的intent汇总，分类
    - 使用本地LLM（老师认可这是AI的合理使用）生成监督学习需要的feature-label数据，然后**人工检查合理性**
    - 构建pipeline，训练intent classifier模型
        - pipeline![[Paste image 1749826165134image.png]]
    - 检测训练完的模型
        - 打印分析报告
            - 可以参考py_code\log\intent_report.md这篇文档，里面有我的分析和AI的分析
    - 优化训练数据的数量，质量，结构直到模型准确率满意
- 2. entity recognition模型
    - 2，4部分可以参考这篇文档，我们按照这个思路做：https://docs.google.com/document/d/1IhUxVAQxqd2XG6L4tQdyR6Etp9h2qRVPdf2DcEhOFks/edit?usp=sharing
- 3. VADER情感检测模型
    - 和dsc那个一样，比较简单
- 4. 将上述3个模型整合为NLU解释器
    - 需要构建一个方便查询的知识库
    - 预期的效果：输入文本——检测实体，意图，VADER分数——查询数据库获取答案——将答案填入预设的模板（按不同意图和情感分类）——输出回答
- 5. 可视化前端：问wsr
- 6. 将模型接入前端UI，chatbot就此完成！

## Implementation

## Discussion