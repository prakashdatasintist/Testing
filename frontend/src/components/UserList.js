// src/components/UserList.js
import React, { useEffect, useState } from 'react';
import { fetchUsers } from '../api';

function UserList() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetchUsers()
      .then(response => setUsers(response.data))
      .catch(error => console.error('Error fetching users:', error));
  }, []);

  return (
    <div>
      <h2>User List</h2>
      <ul>
        {users.map(user => (
          <li key={user.id}>{user.username}</li>
        ))}
      </ul>
    </div>
  );
}

export default UserList;
