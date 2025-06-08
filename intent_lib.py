import json

intent_lib=[
  {
    "intent_name": "query_facility_location",
    "description": "查询特定校园设施（如教学楼、图书馆、体育馆）的具体位置。",
    "example_utterances": [
      "请问A3图书馆在哪里？",
      "健身房怎么走？",
      "我想知道一号食堂的位置。",
      "校园诊所在哪个区？"
    ]
  },
  {
    "intent_name": "query_facility_hours",
    "description": "查询特定校园设施的开放或关闭时间。",
    "example_utterances": [
      "图书馆几点开门？",
      "食堂的营业时间是什么？",
      "游泳馆周末开放吗？",
      "A1教学楼晚上几点锁门？"
    ]
  },
  {
    "intent_name": "query_facility_features",
    "description": "查询特定设施提供的服务、特色或内部布局。",
    "example_utterances": [
      "体育馆里有什么？",
      "图书馆A3有什么特别的地方吗？",
      "教学楼的自习室在哪一层？",
      "那个咖啡厅卖什么？"
    ]
  },
  {
    "intent_name": "book_facility",
    "description": "用户希望预定某个可预约的设施（如会议室、琴房、运动场地）。",
    "example_utterances": [
      "我想预定一个羽毛球场",
      "怎么预约图书馆的研讨室？",
      "帮我订一个明天的会议室。",
      "可以预定钢琴房吗？"
    ]
  },
  {
    "intent_name": "query_course_info",
    "description": "查询关于课程的详细信息，如上课地点、时间、教师等。",
    "example_utterances": [
      "人工智能这门课在哪里上？",
      "周二上午我有什么课？",
      "王教授的数据库原理是几点的课？",
      "查一下CS101的课程信息。"
    ]
  },
  {
    "intent_name": "query_exam_schedule",
    "description": "查询考试的时间和地点。",
    "example_utterances": [
      "期末考试时间表出来了吗？",
      "线性代数的期末考试在哪个教室？",
      "我想查一下我的考试安排。",
      "什么时候考大学物理？"
    ]
  },
  {
    "intent_name": "find_professor_office",
    "description": "寻找特定教授或教职员工的办公室位置。",
    "example_utterances": [
      "请问张三教授的办公室在哪？",
      "计算机系的系主任办公室怎么走？",
      "我想找一下李老师。",
      "辅导员的办公室在几楼？"
    ]
  },
  {
    "intent_name": "query_canteen_menu",
    "description": "查询食堂或餐厅的菜单或特色菜。",
    "example_utterances": [
      "今天二食堂有什么好吃的？",
      "清真食堂今天有大盘鸡吗？",
      "A3咖啡厅有什么推荐的饮品？",
      "早餐有什么可选的？"
    ]
  },
  {
    "intent_name": "query_campus_events",
    "description": "查询校园内即将发生的活动、讲座或比赛。",
    "example_utterances": [
      "这周有什么活动吗？",
      "最近有篮球比赛吗？",
      "我想知道下个月有什么名人讲座。",
      "校园招聘会是什么时候？"
    ]
  },
  {
    "intent_name": "query_club_info",
    "description": "查询学生社团的相关信息。",
    "example_utterances": [
      "学校里有哪些有趣的社团？",
      "怎么加入吉他社？",
      "动漫社的活动地点在哪里？",
      "我想了解一下机器人俱乐部。"
    ]
  },
  {
    "intent_name": "query_wifi_access",
    "description": "询问如何连接校园Wi-Fi网络。",
    "example_utterances": [
      "怎么连接校园网？",
      "Wi-Fi密码是多少？",
      "图书馆有Wi-Fi吗？",
      "我的笔记本连不上网怎么办？"
    ]
  },
  {
    "intent_name": "query_printing_service",
    "description": "查询在哪里以及如何使用打印服务。",
    "example_utterances": [
      "我在哪里可以打印文件？",
      "图书馆的打印机怎么用？",
      "打印一份多少钱？",
      "A4楼有打印店吗？"
    ]
  },
  {
    "intent_name": "query_transportation_info",
    "description": "查询校园巴士的路线、时刻表或站点。",
    "example_utterances": [
      "校巴几点一班？",
      "去B区的校车在哪里坐？",
      "校园巴士的路线图有吗？",
      "末班校车是几点？"
    ]
  },
  {
    "intent_name": "query_parking_info",
    "description": "查询校园停车规定、停车场位置或收费标准。",
    "example_utterances": [
      "访客车辆可以停在哪里？",
      "A区地下停车场怎么收费？",
      "哪里有空的停车位？",
      "学生可以申请停车位吗？"
    ]
  },
  {
    "intent_name": "query_medical_services",
    "description": "查询校医院或诊所的服务、位置和工作时间。",
    "example_utterances": [
      "校医院在哪里？",
      "我发烧了该去哪看病？",
      "怎么预约心理咨询？",
      "医务室晚上有人吗？"
    ]
  },
  {
    "intent_name": "report_lost_and_found",
    "description": "用户报告丢失物品或查询失物招领处。",
    "example_utterances": [
      "我的校园卡丢了怎么办？",
      "失物招领处在哪里？",
      "我在A1教学楼捡到了一个钱包。",
      "有没有人看到我的雨伞？"
    ]
  },
  {
    "intent_name": "query_payment_info",
    "description": "查询关于学费、住宿费或其他费用的缴纳信息。",
    "example_utterances": [
      "学费什么时候交？",
      "怎么给校园卡充值？",
      "在哪里交电费？",
      "支持什么支付方式？"
    ]
  },
  {
    "intent_name": "query_library_services",
    "description": "查询图书馆的特定服务，如借书、续借、数据库使用等。",
    "example_utterances": [
      "一本书可以借多久？",
      "怎么续借我的书？",
      "如何使用知网数据库？",
      "借书需要什么证件？"
    ]
  },
  {
    "intent_name": "query_dormitory_info",
    "description": "查询关于宿舍的规定、设施或申请流程。",
    "example_utterances": [
      "宿舍几点关门？",
      "可以申请调换宿舍吗？",
      "宿舍有空调吗？",
      "假期可以留宿吗？"
    ]
  },
  {
    "intent_name": "find_atm_or_bank",
    "description": "寻找自动取款机（ATM）或银行服务点。",
    "example_utterances": [
      "学校里哪里有ATM机？",
      "最近的建行网点在哪里？",
      "我想取点钱。",
      "哪个食堂有取款机？"
    ]
  },
  {
    "intent_name": "query_emergency_contact",
    "description": "查询校园紧急联系电话，如保安处、医疗急救。",
    "example_utterances": [
      "校园保安的电话是多少？",
      "如果发生火灾了打什么电话？",
      "紧急情况联系谁？",
      "校园报警电话。"
    ]
  },
  {
    "intent_name": "ask_capabilities",
    "description": "用户询问聊天机器人能做什么。",
    "example_utterances": [
      "你能做什么？",
      "你有哪些功能？",
      "帮我看看你会什么",
      "帮助"
    ]
  },
  {
    "intent_name": "greeting",
    "description": "用户向机器人打招呼。",
    "example_utterances": [
      "你好",
      "嗨",
      "在吗？",
      "Hello"
    ]
  },
  {
    "intent_name": "goodbye",
    "description": "用户结束对话。",
    "example_utterances": [
      "再见",
      "拜拜",
      "没事了，谢谢",
      "退出"
    ]
  },
  {
    "intent_name": "thank_you",
    "description": "用户表示感谢。",
    "example_utterances": [
      "谢谢你",
      "太感谢了",
      "好的，多谢",
      "Thanks"
    ]
  },
  {
    "intent_name": "affirmation",
    "description": "用户给出肯定的回答。",
    "example_utterances": [
      "是的",
      "对",
      "没错",
      "OK"
    ]
  },
  {
    "intent_name": "negation",
    "description": "用户给出否定的回答。",
    "example_utterances": [
      "不是",
      "不对",
      "我不是这个意思",
      "No"
    ]
  },
  {
    "intent_name": "ask_human_handoff",
    "description": "用户希望与人工客服或工作人员交谈。",
    "example_utterances": [
      "能帮我转接人工吗？",
      "我想和真人说话。",
      "你有同事的联系方式吗？",
      "机器人解决不了，找人来。"
    ]
  },
  {
    "intent_name": "provide_feedback",
    "description": "用户对机器人的服务提供反馈。",
    "example_utterances": [
      "你这个回答不对。",
      "你很有用！",
      "我觉得你可以改进一下。",
      "我要投诉。"
    ]
  },
  {
    "intent_name": "chitchat",
    "description": "与校园生活无关的闲聊。",
    "example_utterances": [
      "你叫什么名字？",
      "今天天气怎么样？",
      "给我讲个笑话吧。",
      "你几岁了？"
    ]
  },
  {
    "intent_name": "query_opening_hours_general",
    "description": "宽泛地询问开放时间，未指定具体设施。",
    "example_utterances": [
      "开放时间是几点？",
      "什么时候开门？",
      "这里几点下班？"
    ]
  }
]

entity_lib={
  "facility_name": {
    "description": "用户明确提到的具体设施或服务点的标准名称。",
    "examples": [
      "A3图书馆",
      "一号食堂",
      "体育馆",
      "校医院",
      "ZUS Coffee"
    ]
  },
  "location": {
    "description": "用户提到的任何地点、区域或建筑物，可能不完全是标准设施名。",
    "examples": [
      "南门",
      "A区",
      "501教室",
      "逸夫楼",
      "湖边"
    ]
  },
  "facility_type": {
    "description": "设施的类别，当用户没有指定具体某个设施时使用。",
    "examples": [
      "自习室",
      "篮球场",
      "打印店",
      "咖啡馆",
      "健身房"
    ]
  },
  "course_name": {
    "description": "课程的名称。",
    "examples": [
      "人工智能导论",
      "数据库原理",
      "大学物理",
      "公共英语"
    ]
  },
  "course_code": {
    "description": "课程的唯一代码。",
    "examples": [
      "CS101",
      "MA203",
      "PHY101"
    ]
  },
  "professor_name": {
    "description": "教职员工的姓名，包括教授、老师、辅导员等。",
    "examples": [
      "王伟教授",
      "张老师",
      "李助教",
      "辅导员"
    ]
  },
  "department_name": {
    "description": "学院、系或行政部门的名称。",
    "examples": [
      "计算机科学系",
      "教务处",
      "学生事务中心",
      "后勤集团"
    ]
  },
  "date": {
    "description": "具体的日期或相对日期。",
    "examples": [
      "今天",
      "明天",
      "6月10号",
      "下周三",
      "这周末"
    ]
  },
  "time": {
    "description": "具体的时间或相对时间。",
    "examples": [
      "下午3点",
      "晚上8点",
      "9:30am",
      "午饭时间"
    ]
  },
  "time_range": {
    "description": "一个时间段。",
    "examples": [
      "早上8点到10点",
      "全天",
      "下午"
    ]
  },
  "canteen_name": {
    "description": "特指食堂或餐厅的名称。",
    "examples": [
      "一食堂",
      "二食堂",
      "清真餐厅",
      "教工食堂"
    ]
  },
  "dish_name": {
    "description": "具体的菜品或食物名称。",
    "examples": [
      "大盘鸡",
      "牛肉面",
      "拿铁",
      "麻辣香锅"
    ]
  },
  "event_name": {
    "description": "校园活动、讲座或比赛的名称。",
    "examples": [
      "迎新晚会",
      "校园招聘会",
      "AI技术讲座",
      "校长杯篮球赛"
    ]
  },
  "club_name": {
    "description": "学生社团的名称。",
    "examples": [
      "吉他社",
      "机器人俱乐部",
      "辩论队",
      "动漫社"
    ]
  },
  "item_name": {
    "description": "用户提到的具体物品，常用于失物招领等场景。",
    "examples": [
      "校园卡",
      "钱包",
      "雨伞",
      "笔记本电脑",
      "钥匙"
    ]
  },
  "payment_type": {
    "description": "费用的种类。",
    "examples": [
      "学费",
      "住宿费",
      "电费",
      "网费",
      "餐费"
    ]
  },
  "document_type": {
    "description": "证明或文件的类型。",
    "examples": [
      "成绩单",
      "在读证明",
      "学生证",
      "请假条"
    ]
  },
  "transport_tool": {
    "description": "交通工具的名称，特指校园交通。",
    "examples": [
      "校巴",
      "班车",
      "电瓶车"
    ]
  },
  "bus_route_name": {
    "description": "校园巴士的线路名称。",
    "examples": [
      "1号线",
      "环校线",
      "去B区的班车"
    ]
  },
  "booking_duration": {
    "description": "预定时长。",
    "examples": [
      "一个小时",
      "两个小时",
      "一下午",
      "一整天"
    ]
  },
  "academic_term": {
    "description": "学期。",
    "examples": [
      "这学期",
      "下学期",
      "大一上学期",
      "暑期课程"
    ]
  },
  "contact_type": {
    "description": "联系方式的类型。",
    "examples": [
      "电话",
      "邮箱",
      "办公室地址"
    ]
  }
}

# for intent in intent_lib:
#     print(intent["intent_name"],"\n")
# with open("data/intent_lib.json","w") as f:
#     json.dump(intent_lib,f)