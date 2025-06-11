import json

AI_entity_lib={
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

entity_lib={
    "business_name": [
      "SOI 55 THAI KITCHEN",
      "Klinik Sunsuria Medical",
      "麻辣诱惑",
      "Secret Recipe",
      "啵啵鱼泡泡鸡PaoPaoPot",
      "沙县小吃",
      "柳州传统螺蛳粉 & Monster Boba",
      "颜渌渌GAN'S LOK LOK",
      "KLINIK COSMOMEDIC",
      "秀海福麻辣烫",
      "KK便利店",
      "蜜雪冰城MIXUE",
      "星巴克STARBUCKS",
      "KIMS SALON",
      "7-11便利店",
      "Stella Vet Clinic",
      "迈利斯MILLIES VISION",
      "你好，同学Hey Stationery",
      "食坊EatHami",
      "THE GRIND",
      "薯嘟嘟DU-DU POTATO",
      "闽桂中国超市MING GUI",
      "蜀都风味",
      "三千尺The Flows gourmet",
      "SITRUS",
      "陕西面馆",
      "Nasi Kandar Al-Hajeera",
      "鸡公煲",
      "54 thai mookata",
      "茶餐室",
      "Baskin-Robbins",
      "串串店？",
      "Q EVENT SPACE",
      "大熊熊螺蛳粉",
      "DOBI SANTAI",
      "Bing Dessert Cafe",
      "人民书局",
      "Real Peak Music",
      "AHIMSA YOGA",
      "SENZE CAFF",
      "CHATTO",
      "KOPI SAIGON",
      "GEPREK'ING Fried Chicken",
      "Kafe Lazatnya",
      "拾浮百世"
    ],
    "business_type": [
      "Restaurant",
      "Clinic",
      "Convenience store",
      "Salon",
      "Supermarket",
      "Cafe",
      "Bookstore",
      "Laundry",
      "Yoga studio",
      "Pet clinic",
      "Eyeglasses store",
      "Stationery store",
      "Fruit shop",
      "Ice cream shop",
      "Wedding venue",
      "DJ studio",
      "Beverage shop"
    ],
    "cuisine": [
      "Thai",
      "Chinese",
      "Western",
      "Malaysian",
      "Sichuan",
      "Hunan",
      "Shaanxi"
    ],
    "feature": [
      "Authentic Thai",
      "Curry dishes",
      "Mango sticky rice",
      "Health checkup",
      "Physical therapy",
      "Ultrasound",
      "General practitioner",
      "Spicy dry pot",
      "Spicy hot pot",
      "Braised chicken rice",
      "Sour and spicy noodles",
      "Dumplings",
      "Cold noodles",
      "Small cakes",
      "Cheese tarts",
      "Pasta",
      "Birthday cakes",
      "Claypot fish",
      "Claypot chicken",
      "Shaxian snacks",
      "Luosifen",
      "Clam rice noodles",
      "Skewers",
      "Boiled skewers",
      "Fried skewers",
      "Spicy soup base",
      "24-hour operation",
      "Peach oolong tea",
      "Matcha latte",
      "Double coffee cheesecake",
      "Pandan coconut cake",
      "Hair coloring",
      "Perm",
      "Cold drinks",
      "Instant noodles",
      "Cats",
      "Dogs",
      "Eyeglasses prescription",
      "Vision test",
      "Gift bags",
      "Document printing",
      "Photo printing",
      "Fitness meals",
      "Steak",
      "Pasta",
      "Frozen hotpot ingredients",
      "Chinese seasonings",
      "Snacks",
      "Master Kong instant noodles",
      "White Elephant instant noodles",
      "Milk tea",
      "Beef noodles",
      "Claypot noodles",
      "Strong seasoning",
      "Chewy noodles",
      "Free noodle refills",
      "Fresh fruits",
      "Delivery",
      "Bird's nest pancake",
      "Fried Indomie",
      "Fried chicken",
      "Teh tarik",
      "Cendol",
      "Roti canai",
      "Fried instant noodles",
      "Nasi kandar",
      "Naan bread",
      "Tandoori chicken",
      "Chicken pot",
      "Thai seafood hot pot buffet",
      "Chicken rice",
      "Wonton noodles",
      "Ice cream cakes",
      "Shaved ice",
      "DJ courses",
      "Karaoke",
      "Set meals",
      "Simple meals",
      "Nasi lemak",
      "Fried noodles"
    ],
    "business_status": [
      "Open",
      "Renovating",
      "Coming soon",
      "Not open yet"
    ],
    "bell_location": [
      "Roadside shop",
      "Inner shop",
      "Second floor shop"
    ],
    "campus_building": [
      "B1 Activity Building",
      "A Zone Teaching Buildings"
    ],
    "campus_facility": [
      "Supermarket",
      "Dining Area",
      "ATM",
      "IELTS Office",
      "Yoga Room",
      "Traditional Chinese Medicine Clinic",
      "Clinic",
      "Maintenance Office",
      "Admissions Office",
      "Sports Fields",
      "Stadium",
      "Swimming Pool",
      "Gym",
      "Infirmary",
      "Badminton Court",
      "Teaching Building",
      "Library",
      "Cafe"
    ],
    "campus_location": [
      "East side of campus",
      "South side of campus",
      "LG floor",
      "G floor",
      "1st floor",
      "2nd floor",
      "3rd floor",
      "G floor atrium",
      "Outside G floor",
      "A Zone"
    ],
    "facility_feature": [
      "Largest supermarket on campus",
      "Multiple dining tables",
      "Open space",
      "UnionPay/Visa/MasterCard withdrawals",
      "IELTS language information",
      "Yoga club use",
      "TCM diagnosis and treatment",
      "Free consultation",
      "Medical services",
      "Dormitory maintenance requests",
      "Local student inquiries",
      "Volleyball court",
      "Tennis court",
      "Small football field",
      "Basketball court",
      "Hosts school events",
      "Water depth 1.3m-2m",
      "Swim cap required",
      "Anaerobic and aerobic areas",
      "Cash only",
      "Need to bring your own racket",
      "Classrooms",
      "Faculty offices",
      "Parking lot",
      "Study rooms can be reserved",
      "Movie theater",
      "ZUS coffee"
    ],
    "opening_hour": [
      "Monday to Friday 8:30am-9:30pm",
      "Weekends 9:00am-9:00pm",
      "Monday to Sunday 9:00am-1:00pm, 2:00pm-5:00pm",
      "Tuesday to Sunday 16:00-22:00",
      "9:00am-10:00pm",
      "Monday to Friday 9:00am-10:00pm",
      "Weekends and holidays 9:00am-5:00pm"
    ],
    "handbook_entity":[
    "Birthday Cake Recommendations",
    "Secret Recipe",
    "Baskin Robbins",
    "Baker's Cottage",
    "Lachér Patisserie",
    "On-Campus Clinics",
    "Clinic A (Behind the TCM Center)",
    "Clinic B (Top Floor of B1)",
    "AskA User Guide",
    "Cashless Payment Guide (XMUM)",
    "Health & Wellness Services at XMUM",
    "Library Study Room Booking Guide",
    "KTV Near XMUM",
    "Bicycle Parking Guide",
    "Milk Tea Shops Near XMUM",
    "Classroom Types at XMUM",
    "Search for Books in the Library",
    "Locate Books in the Library",
    "Print in the Library (via Computer)",
    "Print in the Library (via USB)",
    "Scan in the Library",
    "Request a Refund for Self-Service Printing",
    "Use Laundry and Drying Machines",
    "Use the Shoe Washing Machine",
    "Use Dry Cleaning Service",
    "Withdraw Money from an ATM on Campus",
    "Campus Coffee Shops, Coffee Machines, and Vending Machine Locations",
    "School Email and Campus ID",
    "View Timetable",
    "Course Registration",
    "Course Retake (Resit)",
    "Attendance and Leave",
    "Public Holiday Rescheduling",
    "Exam Guide",
    "Contact with Instructors",
    "Course Evaluation (Student Feedback)",
    "Major Transfer Procedures",
    "Contact Information",
    "Clubs and Societies at XMUM"
  ],
    "campus_restaurant":[
    "D6 Canteen",
    "LG Floor",
    "1st Floor", 
    "2nd Floor",
    "夏1城",
    "Tuk Tuk Thai&Taro",
    "大树下",
    "Let's kopitiam",
    "mynews便利店",
    "Takw Mee Tarik",
    "大家旺",
    "蜀之味",
    "大城小厨",
    "华联好凉茶",
    "小云冰室",
    "大拇指",
    "喵喵轻食",
    "大碗面",
    "U&I",
    "小台枫",
    "Restaurant Kabaabish",
    "B1 Canteen",
    "Sapid",
    "Saffron Club",
    "Regiustea皇茶",
    "Poke Bowl Rice",
    "Zone U Bakery",
    "LY3 Canteen",
    "中闽美食",
    "Bean's Express",
    "Mad Plate Express",
    "小九州",
    "膳一城",
    "槟城风味",
    "佳味食轩",
    "中国穆斯林小炒",
    "Uni Hotpot",
    "Cafes",
    "ZUS Coffee",
    "Lakefront Cafe",
    "Cotti Coffee",
    "Bo Ya Xuan Reataurant"
  ],
  	"souvenirs_entity":{
    "categories": [
      "Food Items",
      "Daily Use Items",
      "Essential Medicines"
    ],
    "food_items": [
      "Beryl's Chocolate",
      "Milo",
      "White Coffee",
      "Instant Noodles",
      "Bak Kut Teh Soup Mix",
      "Village Park Sambal Sauce",
      "Ghee Hiang Sesame Oil",
      "Cookies",
      "Toast",
      "Bird's Nest",
      "Tongkat Ali"
    ],
    "daily_use_items": [
      "Legendary Orchid Perfume",
      "Luxury Beauty Skincare",
      "Fipper Slippers",
      "De'Xandra Car Aromatherapy"
    ],
    "medicines": [
      "Tiger Balm Complete Series",
      "Muhi Ointment",
      "Other Southeast Asian Medicinal Oils"
    ],
    "brands": [
      "OldTown White Coffee",
      "Ah Huat",
      "Oriental Kopi (Wah Yeong)",
      "SUPER",
      "AIK CHEONG",
      "A1 Bak Kut Teh",
      "Ghee Hiang",
      "Lexus",
      "Julie's",
      "Gardenia",
      "Sunshine",
      "Chanel",
      "Lancome",
      "Mac",
      "Dior",
      "Kiehl's",
      "De'Xandra",
      "Tiger Balm",
      "Kwan Loong",
      "Po Chai",
      "Axe Brand",
      "Three Legs Brand",
      "Vicks",
      "Five Centipedes Brand",
      "Taisho"
    ],
    "flavors": [
      "Tiramisu raw chocolate",
      "Tiramisu almond white chocolate",
      "White chocolate sandwich cookies",
      "Coconut egg rolls",
      "Tiramisu crispy cookies",
      "Original sambal sauce",
      "Spicy version sambal sauce",
      "Butter toast",
      "Pandan coconut flavor toast",
      "Hokkaido milk toast",
      "Green Tea Forest",
      "Coffee Warm",
      "Forest Dream (Bergamot)"
    ],
    "purchase_locations": [
      "Beryl's specialty stores",
      "Major supermarkets",
      "Convenience stores",
      "Traditional Bak Kut Teh restaurants",
      "Jaya Grocer supermarket",
      "Mercato supermarkets",
      "Bird's nest specialty stores",
      "Health product stores",
      "Mall perfume sections",
      "Airport beauty stores",
      "Mall brand counters",
      "Mall specialty stores",
      "Online shopping platforms",
      "Watsons",
      "Guardian",
      "Major pharmacies"
    ],
    "characteristics": [
      "Malaysian specialty chocolate",
      "Malaysia's national chocolate drink",
      "Malaysian specialty coffee",
      "Malaysian specialty instant noodles",
      "Malaysian specialty soup seasoning",
      "Soul sauce for Nasi Lemak",
      "Penang specialty sesame oil",
      "Malaysian specialty cookies",
      "Malaysian specialty toast",
      "High nutritional value",
      "One of Malaysia's three national treasures",
      "Malaysian local brand perfume",
      "Cheaper prices than domestic",
      "Made from natural rubber",
      "Malaysian local brand",
      "Essential household topical medicine",
      "Anti-itch for mosquito bites"
    ]
  }
}

# entity lib到时候要分类


# for intent in intent_lib:
#     print(intent["intent_name"],"\n")
# with open("data/intent_lib.json","w") as f:
#     json.dump(intent_lib,f)