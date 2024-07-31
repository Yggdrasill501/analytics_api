import { useEffect, useState } from 'react';
import axios from 'axios';

export default function Home() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Replace with your Django backend endpoint
    axios.get('http://localhost:8000/analytics/sessions_by_country/')
      .then(response => {
        setData(response.data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  return (
    <div>
      <h1>Sessions by Country</h1>
      <table>
        <thead>
          <tr>
            <th>Country</th>
            <th>Sessions</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item, index) => (
            <tr key={index}>
              <td>{item.country}</td>
              <td>{item.sessions}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
