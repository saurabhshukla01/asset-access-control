import React, { useState } from 'react';
import AssetList from './components/AssetList';
import { mockUsers } from './mockUsers';

function App() {
  const [user, setUser] = useState(null);

  const loginAs = (role) => {
    setUser(mockUsers[role]);
  };

  const logout = () => {
    setUser(null);
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>🔐 Asset Access Control</h1>

      {!user ? (
        <div>
          <p>Select a user to login:</p>
          <button onClick={() => loginAs('admin')}>Login as Admin</button>
          <button onClick={() => loginAs('member')}>Login as Member</button>
        </div>
      ) : (
        <div>
          <p>Logged in as <strong>{user.username}</strong> ({user.role})</p>
          <button onClick={logout}>Logout</button>
          <AssetList user={user} />
        </div>
      )}
    </div>
  );
}

export default App;
