
import './App.css';
import React, { useState } from 'react';
import MultiGraph from './components/ui/multiGraph'

function Azpp() {

  const [input, setInput] = useState("");
  const [stats, setStats] = useState({});
  const handleClick = () => {
      fetch('http://localhost:5000/getstatz',{
          method: 'POST',
          body: JSON.stringify({ map_name: input })
        }
      )
    .then(response => response.json())
    .then((response) => {
        console.log(response)
        setStats(response.data)
        }
     )
  }

  return (
    <div className="App">
        <label>return stats for map :</label>
        <input type="text" onChange={e => setInput(e.target.value)}/>
        <input type="submit" value="click it" onClick={handleClick}/>
        <p>{stats ? JSON.stringify(stats) : ""}</p>
        <div> <SimpleBar /> </div>
    </div>
  );
}
function App() {

  return (
      <div>
        <MultiGraph/>
      </div>
  );
}
export default App;