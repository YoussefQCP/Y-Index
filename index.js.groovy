import Head from 'next/head'
import { useState } from 'react'

export default function Home() {
  const [input, setInput] = useState('')
  const [response, setResponse] = useState('')

  const askAI = async () => {
    const res = await fetch('/api/ask', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ prompt: input })
    })
    const data = await res.json()
    setResponse(data.reply)
  }

  return (
    <div style={{padding: 20, fontFamily: 'sans-serif'}}>
      <Head><title>Y-AI</title></Head>
      <h1>🤖 Y-AI</h1>
      <p>الذكاء الاصطناعي المبني على نظرية النجم الأسود</p>
      <textarea rows="4" value={input} onChange={(e) => setInput(e.target.value)} />
      <br />
      <button onClick={askAI}>اسأل Y-AI</button>
      <pre>{response}</pre>
    </div>
  )
}
