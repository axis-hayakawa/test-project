import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';

type TestData = {
  id: number;
  test_name: string;
  age: string;
};

const App: React.FC = () => {
  const [testData, setTestData] = useState<TestData[]>([]);

  useEffect(() => {
    axios.get<TestData[]>('http://localhost:5000/api/test')
      .then(res => setTestData(res.data))
      .catch(err => console.error('API fetch error:', err));
  }, []);

  return (
    <div className="container">
      <h1>Test Data</h1>
      <table className="data-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Age</th>
          </tr>
        </thead>
        <tbody>
          {testData.map(item => (
            <tr key={item.id}>
              <td>{item.id}</td>
              <td>{item.test_name}</td>
              <td>{item.age}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default App;