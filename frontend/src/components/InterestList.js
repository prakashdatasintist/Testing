import React, { useEffect, useState } from 'react';
import axios from 'axios';

function InterestList() {
  const [interests, setInterests] = useState([]);

  useEffect(() => {
    axios.get('/api/interests/')
      .then(response => setInterests(response.data))
      .catch(error => console.error('Error fetching interests:', error));
  }, []);

  return (
    <div>
      <h2>Interest List</h2>
      <ul>
        {interests.map(interest => (
          <li key={interest.id}>{interest.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default InterestList;
