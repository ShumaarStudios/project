import React, { useState } from 'react';
import axios from 'axios';

const Login = () => {
  const [mobileNumber, setMobileNumber] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    axios.post('/api/auth/login', { mobile_number: mobileNumber, password })
      .then(response => {
        alert(response.data.message);
      })
      .catch(error => {
        alert('Login failed');
      });
  };

  return (
    <div>
      <h1>Login</h1>
      <input type="text" placeholder="Mobile Number" onChange={(e) => setMobileNumber(e.target.value)} />
      <input type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} />
      <button onClick={handleLogin}>Login</button>
    </div>
  );
}

export default Login;
