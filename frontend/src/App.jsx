import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [properties, setProperties] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    // Fetch properties from our backend API
    const fetchProperties = async () => {
      try {
        const response = await axios.get('/api/properties')
        setProperties(response.data.properties)
        setLoading(false)
      } catch (err) {
        console.error('Error fetching properties:', err)
        setError('Failed to load properties. Please try again later.')
        setLoading(false)
      }
    }

    fetchProperties()
  }, [])

  return (
    <div className="container">
      <header>
        <h1>StealHouse</h1>
        <p>Find your perfect rental property</p>
      </header>
      
      <main>
        {loading ? (
          <p>Loading properties...</p>
        ) : error ? (
          <p className="error">{error}</p>
        ) : (
          <div className="property-list">
            <h2>Available Properties</h2>
            {properties.map(property => (
              <div key={property.id} className="property-card">
                <h3>{property.title}</h3>
                <p className="address">{property.address}</p>
                <div className="property-details">
                  <p>€{property.price} per month</p>
                  <p>{property.size} m² • {property.bedrooms} BR • {property.bathrooms} BA</p>
                </div>
              </div>
            ))}
          </div>
        )}
      </main>
    </div>
  )
}

export default App
