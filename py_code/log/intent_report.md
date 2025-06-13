## 意图识别训练

初次生成的意图识别模型结果报告：

|                               | precision | recall | f1-score | support | n_train |
| :---------------------------- | --------: | -----: | -------: | ------: | ------: |
| ask_building_include          |         1 |      1 |        1 |       3 |      11 |
| ask_building_location         |         0 |      0 |        0 |       4 |      16 |
| ask_business_info             |       0.8 |  0.444 |    0.571 |       9 |      43 |
| ask_business_location         |     0.333 |    0.4 |    0.364 |       5 |      37 |
| ask_business_time             |     0.833 |  0.357 |      0.5 |      14 |      38 |
| ask_facility_info             |     0.692 |  0.818 |     0.75 |      11 |      61 |
| ask_facility_location         |     0.867 |  0.722 |    0.788 |      18 |      54 |
| ask_facility_time             |     0.875 |  0.438 |    0.583 |      16 |      50 |
| ask_handbook_info             |      0.96 |      1 |     0.98 |      24 |     116 |
| ask_restaurant_location       |     0.855 |  0.983 |    0.915 |      60 |     210 |
| ask_restaurant_price          |     0.907 |   0.98 |    0.942 |      50 |     218 |
| ask_restaurant_recommendation |     0.952 |  0.909 |     0.93 |      44 |     205 |
| ask_restaurant_time           |     0.803 |  0.966 |    0.877 |      59 |     209 |
| accuracy                      |     0.858 |  0.858 |    0.858 |   0.858 |     nan |
| macro avg                     |      0.76 |  0.694 |    0.708 |     317 |     nan |
| weighted avg                  |     0.851 |  0.858 |    0.842 |     317 |     nan |

- 人工结果分析：
  - ask_building_include 结果准确但是**具有很大的偶然性**
  - building-location全军覆没，并且训练数据也不够
  - business-info不咋地，可能是**intent本身太宽泛？**
  - 总之，训练数据至少要干到100条以上，不然无论是训练还是评估都很不准确
    - 几个100条训练量以上的intent效果都不错

### AI 助手分析与建议

用户的分析非常准确，指出了模型性能的核心问题。以下是基于报告和训练数据的进一步分析和具体建议：

#### 1. 问题根源：数据质量与意图定义

报告中的低分项（尤其是 `ask_building_location`、`ask_business_info`、`ask_business_location` 和 `ask_business_time`）共同指向了两个核心问题：

-   **数据量严重不足**:
    -   `ask_building_*` 相关的意图，训练量（`n_train`）仅有 11 和 16，而评估样本（`support`）更是只有 3 和 4。在这样的小样本下，模型完全无法学习到有效特征，导致 `ask_building_location` 的 f1-score 为 0。你的判断“全军覆没”和“偶然性”非常正确。

-   **意图边界模糊，标签不一致**:
    -   你分析的 `business-info不咋地，可能是intent本身太宽泛？` 一针见血。这正是 `ask_business_*` 类别表现糟糕的根本原因。
    -   在数据清理前，大量关于“营业时间”和“位置”的查询被错误地标记为 `ask_business_info` 或 `ask_facility_info`。这导致模型在面对一个包含"where"的查询时，会感到困惑：它应该被分为 `..._location` 还是 `..._info`？这种标签的矛盾和不一致性，使得 precision 和 recall 双双走低。
    -   `ask_business_time` 的 recall 只有 `0.357`，意味着模型只找到了三分之一的"询问业务时间"的查询，很多都被错误地预测到了其他类别（很可能是 `ask_business_info`）。

#### 2. 对近期数据修改的看法

你最近将 `mynews便利店` 的价格查询改回了 `ask_restaurant_price`。从实体建模的角度，这是一个**一致性选择**。虽然"便利店"更接近"商家(business)"，但如果你的系统在其他地方都将其视为"餐厅(restaurant)"，那么在训练数据中保持这种一致性是合理的。**关键在于标准统一**。

然而，将"超市营业时间"的查询标记为 `ask_facility_location` 是一个**明显的标签错误**，这会直接损害模型的性能。建议修正。

#### 3. 后续步骤建议

1.  **增加数据量 (Data Augmentation)**:
    -   对于 `ask_building_*` 这类样本稀疏的意图，必须扩充数据。目标是让每个意图的训练样本量（`n_train`）至少达到80-100条以上。

2.  **严格定义意图边界 (Intent Scoping)**:
    -   坚持我们之前对数据的修正原则：让 `..._info` 意图成为一个"口袋"意图，只处理那些不属于 `..._location`、`..._time`、`..._price` 等具体意图的通用性问题（例如，"有什么服务？"、"联系电话多少？"）。
    -   确保关于 **时间、地点、价格** 的查询，都必须被分配到对应的具体意图，而不是宽泛的 `..._info`。

3.  **保证标签一致性 (Label Consistency)**:
    -   再次检查所有标签，确保一个查询的意图与其文本内容严格对应。"营业时间"就该是 `..._time`，"地址"就该是 `..._location`。这是提升模型性能最直接有效的方法。

通过以上步骤，可以显著提升低分项的 f1-score，并使整体模型更加稳定和可靠。
