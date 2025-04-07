import React from 'react'
import { Box, Paper, Typography } from '@mui/material'
import ChatMessage from './ChatMessage'
import ChatInput from './ChatInput'

interface Message {
  text: string
  isUser: boolean
}

interface ChatWindowProps {
  messages: Message[]
  input: string
  isLoading: boolean
  onInputChange: (value: string) => void
  onSubmit: (e: React.FormEvent) => void
}

const ChatWindow: React.FC<ChatWindowProps> = ({
  messages,
  input,
  isLoading,
  onInputChange,
  onSubmit,
}) => {
  return (
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
          <ChatMessage
            key={index}
            text={message.text}
            isUser={message.isUser}
          />
        ))}
        {isLoading && (
          <Box sx={{ alignSelf: 'flex-start' }}>
            <Typography>Thinking...</Typography>
          </Box>
        )}
      </Paper>

      <ChatInput
        input={input}
        isLoading={isLoading}
        onInputChange={onInputChange}
        onSubmit={onSubmit}
      />
    </Box>
  )
}

export default ChatWindow
