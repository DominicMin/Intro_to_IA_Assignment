> 论文中Methodology的概念
> 
> 在学术论文或项目报告中，**Methodology (方法论)** 章节是整个工作的“蓝图”和“食谱”。它的核心目的不是简单地罗列你用了什么技术，而是要清晰、系统地阐述**你为了达成研究或项目目标，所遵循的完整步骤、使用的具体方法、以及做出这些选择的理由**。
> 
> 一个好的Methodology章节应该回答以下问题：
> 
> 1. **研究/设计范式 (Overall Approach)**：你的项目是基于什么样的大方向？（例如，是实验性研究、案例分析，还是像你这样，属于**构建性研究/设计科学(Constructive Research/Design Science)**，即目标是构建一个新的人工系统来解决一个实际问题）。
> 2. **数据来源与采集 (Data Collection)**：你的系统（尤其是模型）所依赖的数据从何而来？如何采集和准备？
> 3. **系统架构 (System Architecture)**：你构建的系统由哪些主要模块组成？这些模块之间是如何交互的？
> 4. **实现细节 (Implementation Details)**：你具体使用了哪些算法、模型、工具和技术来实现每个模块？（你提到的关键词就属于这里）。
> 5. **评估方法 (Evaluation Methods)**：你用什么标准和指标来衡量你构建的系统或模型的好坏？（例如，准确率、F1分数等）。
> 
> 最重要的是，Methodology需要有**可复现性(Reproducibility)**，即另一位研究者根据你的描述，应该能够大致重现你的工作流程和实验。

## 手工写的Methodology Outline

1. 研究范式：设计一个结合了retrieval-based & template-based chatbot的特点，能够提供校园相关问题解答，提供情绪价值的chatbot，确实属于**构建性研究/设计科学(Constructive Research/Design Science)**
	研究步骤：采集，整理原始数据——使用LLM生成训练数据——设计，训练意图识别和实体识别的模型——整合至解释器——设计生成器并与解释器连接——连接前端与后端——补充训练数据以优化chatbot输出
2. 数据采集
	1. 原始数据
		我们从学长学姐的微信公众号，学生手册中整理了XMUM及附近Bell Avenue的餐厅，学校内设施，学业相关手续等信息，整理成了较为规整的`JSON`文件
	2. 模型训练数据
		由于后续监督学习需要大量数据，而手工准备数据相当耗费时间，因此我们采取**合成数据 (Synthetic Data)** 的策略，使用本地运行的LLM生成feature-label数据集，并加以**人工检查，修正**用于训练模型。这种策略已在学术界被广泛接纳。
3. 系统架构
	==后端架构==
	1. 训练数据生成器[`py_code/data_generator.ipynb`](./py_code/data_generator.ipynb)
		这个生成器根据我们整理好的原始数据，将intent，entity填入预设的prompt模板中，再传输给本地运行的`Ollama LLM`生成训练数据
	2. 实体识别模型[`py_code/entity_recognition.ipynb`](./py_code/entity_recognition.ipynb)
		实体识别采用`spaCy`训练**序列标注（Sequence Labeling）** 模型 ，**命名实体识别（Named Entity Recognition）** 是序列标注中最常见的问题之一
	3. 意图识别模型[`py_code/intent_classification.ipynb`](./py_code/intent_classification.ipynb)
		我们采用**监督学习**：构建`pipeline`：TF-IDF文本向量化+逻辑回归，训练意图识别模型
	4. 用户输入解释器[`py_code/interpreter.ipynb`](./py_code/interpreter.ipynb)
		我们整合已训练的意图识别，实体识别模型和新引入的`VADER`情感检测模型，构建用户输入解释器。该解释器能提取用户输入中的意图，实体以及情感分数，导出结构化的数据
	5. 回复生成器[`py_code/response_generator.ipynb`](./py_code/response_generator.ipynb) 
		生成器接受解释器提取的意图，实体，情感数据，从知识库中检索答案并填入预设的输出模板
	==前端架构==
4. 实现细节
		合成数据，监督学习，TF-IDF向量化，逻辑回归，NER序列标注，生成模板（正式论文中展开）
5. 评估方法
	1. 实体识别和意图识别的评估方法：**模型评估指标 (Model Evaluation Metrics)**
		从混淆矩阵中的TP, FP, TN, TN 中计算precision，recall，最终计算F1-score和accuracy
	2. 最终chatbot的评估方法：不断对话，尤其提出训练数据以外的问题

## 手工写AI润色后的Methodology Outline

### **3. Methodology (研究方法)**

#### **3.1 Research Design and Paradigm (研究设计与范式)**

本项目采用**构建性研究/设计科学 (Constructive Research / Design Science)** 的研究范式。其核心目标是设计、构建并评估一个新的人工智能系统——一个结合了**检索式(Retrieval-based)**与**模板式(Template-based)**特点的混合式聊天机器人——以解决校园场景下信息获取效率低下和情感交互缺失的实际问题。

本研究的整体流程遵循一个迭代的开发周期：

1. **需求分析与数据采集**: 识别校园场景下的核心信息需求，并收集原始数据。
    
2. **系统设计与构建**: 设计并实现一个包含NLU、对话管理和响应生成模块的系统架构。
    
3. **模型训练与实现**: 利用AI增强数据策略训练核心的NLU模型。
    
4. **系统集成与评估**: 将所有模块集成为一个可工作的原型，并通过定量和定性方法进行评估。
    
5. **迭代优化**: 根据评估结果，补充训练数据并对系统进行优化。
    

#### **3.2 System Architecture (系统架构)**

本聊天机器人系统由前端用户界面和后端处理核心组成。后端核心采用模块化设计，主要由自然语言理解（NLU）单元和响应生成单元构成。

[在这里可以插入一个简单的系统架构流程图：用户输入 -> NLU单元 -> 响应生成单元 -> 用户输出]

**3.2.1 Natural Language Understanding (NLU) Unit (自然语言理解单元)** NLU单元负责将用户的原始文本查询转换为结构化的机器可读数据。它包含三个核心组件：

- **Intent Classification Model (意图识别模型)**: 该模型的目标是识别用户的核心意图。我们将其建模为一个多分类问题，通过**监督学习**实现。其技术栈为一个集成了**TF-IDF文本向量化**和**逻辑回归(Logistic Regression)分类器**的Scikit-learn `Pipeline`。
    
- **Entity Recognition Model (实体识别模型)**: 该模型的目标是从查询中提取关键信息（如地点、时间等）。我们将其建模为一个**序列标注(Sequence Labeling)**问题。具体采用了`spaCy`框架来训练一个自定义的**命名实体识别(Named Entity Recognition, NER)**模型。
    
- **Sentiment Analysis Module (情感分析模块)**: 为了提供更具人文关怀的交互，我们引入了`VADER`情感分析工具。该模块负责评估用户输入的情感倾向，并输出一个包含正面、负面、中性和复合情感分数（compound score）的结构化数据。
    

**3.2.2 Response Generation Unit (响应生成单元)** 该单元负责根据NLU的输出结果生成最终的自然语言回答。

- **Knowledge Base Retriever (知识库检索器)**: 系统的知识存储在一个结构化的`JSON`数据库中。检索器根据NLU识别出的实体和意图，在数据库中查询相关信息。
    
- **Response Templating Engine (响应模板引擎)**: 我们设计了一个多层级的回答模板库。该引擎根据用户的`意图`和`情感分数`动态选择最合适的回答模板，并将从知识库检索到的数据填充到模板的占位符中，最终组装成完整的回答。
    

#### **3.3 Data Collection and Preparation (数据采集与准备)**

高质量的数据是模型性能的基石。我们的数据策略分为两个层面：

- **3.3.1 Knowledge Base Data (知识库原始数据)**: 我们通过查阅学生手册、官方公众号以及其他校园信息渠道，手动整理了关于校园设施、餐厅、学术流程等信息，并将其结构化为一个易于检索的`JSON`文件。
    
- **3.3.2 Model Training Data (模型训练数据)**: 为训练NLU模型，我们采用了**合成数据(Synthetic Data)**策略。具体流程是：首先设计一个**数据生成器 (`data_generator.ipynb`)**，它将预设的意图和实体填入Prompt模板；然后调用本地运行的**Ollama LLM**生成大量的特征-标签对；最后，所有生成的数据都经过**人工抽样检查与修正**，以确保其质量和准确性，最终用于模型训练。
    

#### **3.4 Evaluation Methods (评估方法)**

为了全面衡量本项目的成效，我们采用了定量和定性相结合的评估方法。

- **3.4.1 Quantitative Evaluation (定量评估)**: 主要针对NLU模型的性能。我们使用独立的测试集，并通过`scikit-learn`的`classification_report`工具自动计算一系列**模型评估指标(Model Evaluation Metrics)**，包括基于**混淆矩阵(Confusion Matrix)**计算出的**精确率(Precision)**、**召回率(Recall)**和**F1分数(F1-Score)**，以评估模型在每个类别上的性能。
    
- **3.4.2 Qualitative Evaluation (定性评估)**: 主要针对整个聊天机器人的用户体验和实用性。我们通过与机器人进行多轮、开放式的对话来执行评估，尤其关注其处理训练数据之外的边缘问题(edge cases)的能力，以检验对话的流畅性、答案的准确性和情感交互的有效性。