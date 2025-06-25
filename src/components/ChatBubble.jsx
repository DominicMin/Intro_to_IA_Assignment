import React from 'react'

export default function ChatBubble({ text }) {
  return (
    <div className="bg-white shadow p-4 rounded-lg max-w-md">
      <p className="text-gray-800">{text}</p>
    </div>
  )
}