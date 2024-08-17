import React, { useState, useEffect } from 'react';
import HelloWorld from './HelloWorld';
import axios from 'axios';

function App() {
  const [currentTime, setCurrentTime] = useState('');
  const [currentDate, setCurrentDate] = useState('');
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/')
    .then(response => {
      setCurrentTime(response.data.time);
      setCurrentDate(response.data.date)
    })
    .catch(error => {
      console.log(error);
    });
  }, [])
  return (
    <div className="App">
      <header className="App-header">
        <p>The date is {currentDate} and the time is {currentTime}.</p>
      </header>
      <HelloWorld />
    </div>
  );
}

export default App;