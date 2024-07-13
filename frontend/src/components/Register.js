import React from 'react';

function Register() {
  return (
    <div>
      <h2>Register</h2>
      <form>
        <label>
          Username:
          <input type="text" name="username" />
        </label>
        <br />
        <label>
          Password:
          <input type="password" name="password" />
        </label>
        <br />
        <label>
          Email:
          <input type="email" name="email" />
        </label>
        <br />
        <button type="submit">Register</button>
      </form>
    </div>
  );
}

export default Register;

// import React, { useState } from 'react';
// import API from '../api';

// function Register({ history }) {
//   const [username, setUsername] = useState('');
//   const [password, setPassword] = useState('');

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     try {
//       await API.post('/users/', { username, password });
//       history.push('/login');
//     } catch (error) {
//       console.error('Registration failed', error);
//     }
//   };

//   return (
//     <form onSubmit={handleSubmit}>
//       <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
//       <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
//       <button type="submit">Register</button>
//     </form>
//   );
// }

// export default Register;
