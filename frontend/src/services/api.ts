const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8080'

export interface QueryResponse {
  answer: string
}

export const askQuestion = async (question: string): Promise<QueryResponse> => {
  try {
    const response = await fetch(`${API_BASE_URL}/ask_question`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ question }),
    })

    if (!response.ok) {
      throw new Error('Failed to get response from server')
    }

    return await response.json()
  } catch (error) {
    console.error('Error asking question:', error)
    throw error
  }
}
