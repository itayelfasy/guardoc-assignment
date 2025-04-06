import React, { useState } from 'react'
import {
  Container,
  Box,
  TextField,
  Button,
  Paper,
  Typography,
  ThemeProvider,
  createTheme,
  CssBaseline,
} from '@mui/material'
import SendIcon from '@mui/icons-material/Send'

interface Message {
  text: string
  isUser: boolean
}

const theme = createTheme({
  palette: {
    mode: 'light',
    primary: {
      main: '#2196f3',
    },
    background: {
      default: '#f5f5f5',
    },
  },
})

function App() {
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState('')
  const [isLoading, setIsLoading] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!input.trim()) return

    const userMessage: Message = {
      text: input,
      isUser: true,
    }

    setMessages((prev) => [...prev, userMessage])
    setInput('')
    setIsLoading(true)

    try {
      const response = await fetch('http://localhost:8090/ask_question', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Accept: 'application/json',
        },
        body: JSON.stringify({
          question: input,
        }),
      })

      if (!response.ok) {
        throw new Error('Network response was not ok')
      }

      const data = await response.json()

      if (data.error) {
        throw new Error(data.error)
      }

      const assistantMessage: Message = {
        text: data.answer,
        isUser: false,
      }

      setMessages((prev) => [...prev, assistantMessage])
    } catch (error) {
      console.error('Error:', error)
      const errorMessage: Message = {
        text: 'Sorry, there was an error processing your request. Please try again.',
        isUser: false,
      }
      setMessages((prev) => [...prev, errorMessage])
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container maxWidth="md" sx={{ height: '100vh', py: 4 }}>
        <Box sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
          <Typography
            variant="h4"
            component="h1"
            gutterBottom
            align="center"
            sx={{ mb: 4 }}
          >
            Medical Document Assistant
          </Typography>

          <Paper
            elevation={3}
            sx={{
              flex: 1,
              mb: 2,
              p: 2,
              overflow: 'auto',
              display: 'flex',
              flexDirection: 'column',
              gap: 2,
            }}
          >
            {messages.map((message, index) => (
              <Box
                key={index}
                sx={{
                  alignSelf: message.isUser ? 'flex-end' : 'flex-start',
                  maxWidth: '70%',
                }}
              >
                <Paper
                  elevation={1}
                  sx={{
                    p: 2,
                    backgroundColor: message.isUser ? '#e3f2fd' : '#f5f5f5',
                  }}
                >
                  <Typography>{message.text}</Typography>
                </Paper>
              </Box>
            ))}
            {isLoading && (
              <Box sx={{ alignSelf: 'flex-start' }}>
                <Typography>Thinking...</Typography>
              </Box>
            )}
          </Paper>

          <form onSubmit={handleSubmit}>
            <Box sx={{ display: 'flex', gap: 1 }}>
              <TextField
                fullWidth
                variant="outlined"
                placeholder="Ask a question about medical documents..."
                value={input}
                onChange={(e) => setInput(e.target.value)}
                disabled={isLoading}
              />
              <Button
                type="submit"
                variant="contained"
                disabled={isLoading || !input.trim()}
                sx={{ minWidth: '100px' }}
              >
                <SendIcon />
              </Button>
            </Box>
          </form>
        </Box>
      </Container>
    </ThemeProvider>
  )
}

export default App
