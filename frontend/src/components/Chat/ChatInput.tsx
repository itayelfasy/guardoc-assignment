import React from 'react'
import { Box, TextField, Button } from '@mui/material'
import SendIcon from '@mui/icons-material/Send'

interface ChatInputProps {
  input: string
  isLoading: boolean
  onInputChange: (value: string) => void
  onSubmit: (e: React.FormEvent) => void
}

const ChatInput: React.FC<ChatInputProps> = ({
  input,
  isLoading,
  onInputChange,
  onSubmit,
}) => {
  return (
    <Box component="form" onSubmit={onSubmit} sx={{ display: 'flex', gap: 1 }}>
      <TextField
        fullWidth
        variant="outlined"
        placeholder="Ask a question about medical documents..."
        value={input}
        onChange={(e) => onInputChange(e.target.value)}
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
  )
}

export default ChatInput
