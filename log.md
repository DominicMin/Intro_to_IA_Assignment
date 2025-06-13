## 意图识别训练

初次生成的模型结果报告：

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

- 结果分析：
