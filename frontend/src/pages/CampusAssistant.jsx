import React, { useState } from 'react'
import ChatBubble from '../components/ChatBubble'

// API URL配置
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000'

export default function CampusAssistant() {
  const [messages, setMessages] = useState([
    { text: "Hello, I'm the campus assistant. How can I help you?", isBot: true }
  ])
  const [inputValue, setInputValue] = useState('')
  const [isLoading, setIsLoading] = useState(false)

  const sendMessage = async () => {
    if (!inputValue.trim()) return

    // 添加用户消息
    const userMessage = { text: inputValue, isBot: false }
    setMessages(prev => [...prev, userMessage])
    
    const currentInput = inputValue
    setInputValue('')
    setIsLoading(true)

    try {
      // 调用后端API
      const response = await fetch(`${API_URL}/chatbot/ask`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question: currentInput })
      })

      const data = await response.json()
      
      // 添加机器人回复
      const botMessage = { text: data.answer, isBot: true }
      setMessages(prev => [...prev, botMessage])
      
    } catch (error) {
      console.error('Error:', error)
      const errorMessage = { text: "Sorry, the service is temporarily unavailable. Please try again later.", isBot: true }
      setMessages(prev => [...prev, errorMessage])
    } finally {
      setIsLoading(false)
    }
  }

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      sendMessage()
    }
  }

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col">
      <div className="bg-blue-600 text-white p-4 text-center">
        <h1 className="text-2xl font-bold">Campus Assistant</h1>
      </div>
      
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map((message, index) => (
          <div key={index} className={`flex ${message.isBot ? 'justify-start' : 'justify-end'}`}>
            <div className={`max-w-xs lg:max-w-md px-4 py-2 rounded-lg ${
              message.isBot 
                ? 'bg-white text-gray-800 shadow' 
                : 'bg-blue-500 text-white'
            }`}>
              <p>{message.text}</p>
            </div>
          </div>
        ))}
        
        {isLoading && (
          <div className="flex justify-start">
            <div className="bg-white text-gray-800 shadow px-4 py-2 rounded-lg">
              <p>Thinking...</p>
            </div>
          </div>
        )}
      </div>
      
      <div className="p-4 bg-white border-t">
        <div className="flex space-x-2">
          <input
            type="text"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Please enter your question..."
            className="flex-1 border border-gray-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            disabled={isLoading}
          />
          <button
            onClick={sendMessage}
            disabled={isLoading || !inputValue.trim()}
            className="px-6 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 disabled:bg-gray-300 disabled:cursor-not-allowed"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  )
}
