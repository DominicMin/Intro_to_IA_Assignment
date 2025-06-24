import React, { useState } from 'react'
import ChatBubble from '../components/ChatBubble'

export default function CampusAssistant() {
  const [message, setMessage] = useState('Hello, how can I help you?')

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center">
      <h1 className="text-3xl font-bold mb-4 text-blue-600">Welcome to Campus Assistant</h1>
      
      <ChatBubble text={message} />
      
      <button
        className="mt-4 px-4 py-2 bg-blue-500 text-white rounded"
        onClick={() => setMessage('Your request has been received.')}
      >
        Click Me
      </button>
    </div>
  )
}
