import React, { useState } from 'react'
import axios from 'axios'

function ChatApp() {
  const [input, setInput] = useState('')
  const [messages, setMessages] = useState([])

  const handleSend = async () => {
    if (!input.trim()) return

    const userMsg = { sender: 'user', text: input }
    setMessages(prev => [...prev, userMsg])
    setInput('')

    try {
      const res = await axios.post('http://localhost:5000/chatbot/ask', {
        question: input
      })

      const botMsg = { sender: 'bot', text: res.data.answer }
      setMessages(prev => [...prev, botMsg])
    } catch (err) {
      console.error('请求失败：', err)
      const errorMsg = { sender: 'bot', text: ' 请求失败，请稍后重试。' }
      setMessages(prev => [...prev, errorMsg])
    }
  }

  return (
    <div className="p-6 max-w-xl mx-auto min-h-screen bg-white">
      <h1 className="text-2xl font-bold mb-4 text-center">🎓 校园问答机器人</h1>

      <div className="space-y-3 h-64 overflow-y-auto mb-4 bg-gray-100 p-4 rounded shadow">
        {messages.map((msg, i) => (
          <div key={i} className={`text-sm ${msg.sender === 'bot' ? 'text-blue-700' : 'text-green-700'}`}>
            {msg.sender === 'bot' ? '🤖' : '🧑‍🎓'} {msg.text}
          </div>
        ))}
      </div>

      <div className="flex gap-2">
        <input
          value={input}
          onChange={e => setInput(e.target.value)}
          className="border border-gray-300 p-2 flex-1 rounded focus:outline-blue-400"
          placeholder="请输入你的问题..."
        />
        <button
          onClick={handleSend}
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          发送
        </button>
      </div>
    </div>
  )
}

export default ChatApp
