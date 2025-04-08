import React, { useEffect, useState } from 'react';

function AssetList({ user }) {
  const [assets, setAssets] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    if (!user) return;

    fetch("http://127.0.0.1:8000/api/assets/", {
      headers: {
        "X-User": user.username,
      }
    })    
    .then((res) => {
      if (!res.ok) throw new Error('Unauthorized or Forbidden');
      return res.json();
    })
    .then((data) => {
      setAssets(data);
    })
    .catch((err) => {
      setError(err.message);
    });
  }, [user]);

  if (!user) return null;

  if (error) return <p style={{ color: 'red' }}>{error}</p>;

  return (
    <div style={{ marginTop: '1.5rem' }}>
      <h2>Assets</h2>
      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr style={{ backgroundColor: '#f0f0f0' }}>
            <th style={styles.th}>#</th>
            <th style={styles.th}>Asset Name</th>
            {user.role === 'ADMIN' && <th style={styles.th}>Secret Key</th>}
          </tr>
        </thead>
        <tbody>
          {assets.map((asset, index) => (
            <tr key={asset.id} style={{ borderBottom: '1px solid #ddd' }}>
              <td style={styles.td}>{index + 1}</td>
              <td style={styles.td}>{asset.name}</td>
              {user.role === 'ADMIN' && <td style={styles.td}>{asset.secret_key}</td>}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

const styles = {
  th: {
    textAlign: 'left',
    padding: '10px',
    borderBottom: '2px solid #ccc',
  },
  td: {
    padding: '10px',
    textAlign: 'left',
  },
};

export default AssetList;
