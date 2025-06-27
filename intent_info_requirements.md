# Intent信息需求整理

本文档整理了各种intent类型及其所需的信息字段。

## 商家相关Intent

### ask_business_location (查询商家位置)
**所需信息字段：**
- `business_name` - 商家名称
- `location` - 位置信息

### ask_business_time (查询商家营业时间)
**所需信息字段：**
- `business_name` - 商家名称
- `opening_hours` - 营业时间

### ask_business_info (查询商家信息)
**所需信息字段：**
- `business_name` - 商家名称
- `business_info` - 商家详细信息

## 餐厅相关Intent

### ask_restaurant_location (查询餐厅位置)
**所需信息字段：**
- `restaurant_name` - 餐厅名称
- `location` - 位置信息

### ask_restaurant_time (查询餐厅营业时间)
**所需信息字段：**
- `restaurant_name` - 餐厅名称
- `opening_hours` - 营业时间

### ask_restaurant_recommendation (餐厅推荐)
**所需信息字段：**
- `restaurant_name` - 餐厅名称
- `recommendation_reason` - 推荐理由



## 设施相关Intent

### ask_facility_location (查询设施位置)
**所需信息字段：**
- `facility_name` - 设施名称
- `location` - 位置信息

### ask_facility_time (查询设施开放时间)
**所需信息字段：**
- `facility_name` - 设施名称
- `opening_hours` - 开放时间

### ask_facility_info (查询设施信息)
**所需信息字段：**
- `facility_name` - 设施名称
- `facility_info` - 设施详细信息

## 建筑相关Intent

### ask_building_location (查询建筑位置)
**所需信息字段：**
- `building_name` - 建筑名称
- `location` - 位置信息

### ask_building_include (查询建筑包含设施)
**所需信息字段：**
- `building_name` - 建筑名称
- `building_include` - 建筑包含内容

## 手册信息Intent

### ask_handbook_info (查询手册信息)
**所需信息字段：**
- `handbook_info` - 手册信息内容

## 错误处理Intent

### entity_not_found (实体未找到)
**所需信息字段：**
- `query_topic` - 查询主题

### unknown_intent (未知意图)
**所需信息字段：**
- 无特定字段要求

## 所有可能的信息字段汇总

| 字段名                     | 描述     | 使用的Intent                                                                                         |     |
| ----------------------- | ------ | ------------------------------------------------------------------------------------------------- | --- |
| `business_name`         | 商家名称   | ask_business_location, ask_business_time, ask_business_info                                       |     |
| `restaurant_name`       | 餐厅名称   | ask_restaurant_location, ask_restaurant_time, ask_restaurant_recommendation |     |
| `facility_name`         | 设施名称   | ask_facility_location, ask_facility_time, ask_facility_info                  |     |
| `building_name`         | 建筑名称   | ask_building_location, ask_building_include                                  |     |
| `location`              | 位置信息   | ask_business_location, ask_restaurant_location, ask_facility_location, ask_building_location      |     |
| `opening_hours`         | 营业/开放时间   | ask_business_time, ask_restaurant_time, ask_facility_time                                                            |     |
| `business_info`         | 商家详细信息 | ask_business_info                                                                                 |     |
| `facility_info`         | 设施详细信息 | ask_facility_info                                                                                 |     |
| `recommendation_reason` | 推荐理由   | ask_restaurant_recommendation                                                                     |     |
| `building_include`       | 建筑包含内容   | ask_building_include                                                                              |     |
| `handbook_info`         | 手册信息   | ask_handbook_info                                                                                 |     |
| `query_topic`           | 查询主题   | entity_not_found                                                                                  |     |
