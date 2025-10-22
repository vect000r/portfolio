import { useState, useEffect } from 'react'
import './App.css'

interface ApiResponse {
  message: string
}

function App() {
  const [message, setMessage] = useState<string>('Loading...')
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    fetch('/api/test/')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok')
        }
        return response.json()
      })
      .then((data: ApiResponse) => {
        setMessage(data.message)
      })
      .catch(error => {
        console.error('Error:', error)
        setError('Failed to connect to API')
      })
  }, [])

  return (
    <div className="App">
      <h1>My Portfolio</h1>
      {error ? (
        <p style={{ color: 'red' }}>{error}</p>
      ) : (
        <p>{message}</p>
      )}
    </div>
  )
}

export default App