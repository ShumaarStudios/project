import React, { useState } from 'react';
import axios from 'axios';

const Registration = () => {
  const [name, setName] = useState('');
  const [mobileNumber, setMobileNumber] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleRegister = () => {
    axios.post('/api/auth/register', { name, mobile_number: mobileNumber, email, password })
      .then(response => {
        alert(response.data.message);
      })
      .catch(error => {
        alert('Registration failed');
      });
  };

  return (
    <div>
      <h1>Register</h1>
      <input type="text" placeholder="Name" onChange={(e) => setName(e.target.value)} />
      <input type="text" placeholder="Mobile Number" onChange={(e) => setMobileNumber(e.target.value)} />
      <input type="email" placeholder="Email (optional)" onChange={(e) => setEmail(e.target.value)} />
      <input type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} />
      <button onClick={handleRegister}>Register</button>
    </div>
  );
}

export default Registration;
