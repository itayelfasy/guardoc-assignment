import React, { useState } from 'react'
import {
  Container,
  ThemeProvider,
  createTheme,
  CssBaseline,
} from '@mui/material'
import ChatWindow from './components/Chat/ChatWindow'
import { askQuestion } from './services/api'

interface Message {
  text: string
  isUser: boolean
}

const theme = createTheme({
  palette: {
    mode: 'light',
    primary: {
      main: '#1976d2',
    },
  },
})

function App() {
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState('')
  const [isLoading, setIsLoading] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!input.trim() || isLoading) return

    const userMessage = input.trim()
    setInput('')
    setMessages((prev) => [...prev, { text: userMessage, isUser: true }])
    setIsLoading(true)

    try {
      const response = await askQuestion(userMessage)
      setMessages((prev) => [...prev, { text: response.answer, isUser: false }])
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          text: 'Sorry, there was an error processing your question.',
          isUser: false,
        },
      ])
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container maxWidth="md" sx={{ height: '100vh', py: 4 }}>
        <ChatWindow
          messages={messages}
          input={input}
          isLoading={isLoading}
          onInputChange={setInput}
          onSubmit={handleSubmit}
        />
      </Container>
    </ThemeProvider>
  )
}

export default App
