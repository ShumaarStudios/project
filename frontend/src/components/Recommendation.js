import React, { useState } from 'react';
import axios from 'axios';

const Recommendation = () => {
  const [soilType, setSoilType] = useState('');
  const [cropVariety, setCropVariety] = useState('');
  const [region, setRegion] = useState('');
  const [recommendations, setRecommendations] = useState([]);

  const getRecommendations = () => {
    axios.post('/api/recommendation/suggest', { soil_type: soilType, crop_variety: cropVariety, region })
      .then(response => {
        setRecommendations(response.data);
      })
      .catch(error => {
        alert('Failed to fetch recommendations');
      });
  };

  return (
    <div>
      <h1>Recommendations</h1>
      <input type="text" placeholder="Soil Type" onChange={(e) => setSoilType(e.target.value)} />
      <input type="text" placeholder="Crop Variety" onChange={(e) => setCropVariety(e.target.value)} />
      <input type="text" placeholder="Region" onChange={(e) => setRegion(e.target.value)} />
      <button onClick={getRecommendations}>Get Recommendations</button>
      <div>
        {recommendations.map((rec, index) => (
          <div key={index}>
            <h3>{rec.name}</h3>
            <p>Dosage: {rec.dosage}</p>
            <p>Application Method: {rec.application_method}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Recommendation;
