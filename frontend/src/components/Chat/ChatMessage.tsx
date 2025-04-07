import React from 'react'
import { Box, Paper, Typography } from '@mui/material'

interface ChatMessageProps {
  text: string
  isUser: boolean
}

const ChatMessage: React.FC<ChatMessageProps> = ({ text, isUser }) => {
  return (
    <Box
      sx={{
        alignSelf: isUser ? 'flex-end' : 'flex-start',
        maxWidth: '70%',
      }}
    >
      <Paper
        elevation={1}
        sx={{
          p: 2,
          backgroundColor: isUser ? '#e3f2fd' : '#f5f5f5',
        }}
      >
        <Typography>{text}</Typography>
      </Paper>
    </Box>
  )
}

export default ChatMessage
