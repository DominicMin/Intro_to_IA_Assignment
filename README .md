#  Campus Helper - 校园智能助手（前端）

A lightweight and responsive **Campus Assistant Web App**, built using **Vite + React + Tailwind CSS**.  
这是一个使用 Vite + React + Tailwind CSS 构建的轻量级校园问答类前端项目，旨在帮助学生更快捷地获取校园信息和服务。

---

##  技术栈 / Tech Stack

| 类别 | 技术 |
|------|------|
| 框架 | React 18 + Vite |
| 样式 | Tailwind CSS + PostCSS |
| 构建 | Vite |
| 状态管理 | useState + useEffect (内置 React Hook) |
| 请求库 | 可接入 axios（与后端联调）|

---

##  项目结构 / Project Structure

```
campus-helper/
├── public/                  # 静态资源（图标、manifest 等）
├── src/
│   ├── assets/              # 本地图片等资源
│   ├── components/          # 可复用 UI 组件（如 ChatBubble）
│   ├── pages/               # 页面组件（如 CampusAssistant.jsx）
│   ├── routes/              # 路由文件 & 样式 index.css
│   ├── App.jsx              # 应用根组件
│   └── main.jsx             # 应用入口
├── index.html               # HTML 模板
├── tailwind.config.js       # Tailwind 配置
├── postcss.config.js        # PostCSS 配置
└── package.json             # 项目依赖说明
```

---

##  启动项目 / Getting Started

### 1️ 安装依赖

```bash
npm install
```

### 2️ 启动开发服务器

```bash
npm run dev
```

默认将运行在 `http://localhost:5173`，可在浏览器中访问查看效果。

---

##  示例功能 / Example Feature

 页面组件：`CampusAssistant.jsx`  
 可交互气泡框组件：`ChatBubble.jsx`  
 示例交互：点击按钮动态改变对话文本（useState 实现）

---

##  后端联调 / Backend Integration

使用 axios 并封装请求模块，通过如下方式接入后端：

```bash
npm install axios
```

然后在组件中通过 axios 进行 API 请求：

```js
import axios from 'axios'

axios.get('/api/message').then(res => {
  console.log(res.data)
})
```

---

##  Highlights

-  极速构建：Vite 预构建加速，秒开开发服务器
-  原子 CSS：Tailwind 布局灵活，主题可定制
-  模块清晰：页面、组件、样式分离，便于维护
-  易集成：可无缝接入后端 RESTful 接口

---

##  Future Plans

-  用户身份登录 & 权限控制
-  常见问答接口对接（与后端对齐）
-  UI 多语言切换
-  聊天记录存储 & 快速查询
-  部署上线（GitHub Pages / Vercel）

