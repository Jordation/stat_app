
import React, { useState } from 'react';
import GraphZone from "./components/ui/multiGraph";
function UrlToGraphs() {

    const [url, setUrl] = useState("");

    const getData = () => {
        fetch('http://localhost:5000/loadStats', {
            method: 'POST',
            body: JSON.stringify({ url: url })
          }
        )
    .then(response => response.json())
    .then((response) => {
            console.log(response.data)
            }
        )
    }
    return(
        <div>
            <input type="text" onChange={e => setUrl(e.target.value)}/>
            <input type="submit" value="load data" onClick={getData}/>
            <br/>
            <input type="text" onChange={e => setUrl(e.target.value)}/>
            <input type="submit" value="generate graphs" onClick={getData}/>
        </div>
        // figure out how to take params and load graphs AFTER some  async
        // no doubt
    )
}


export default UrlToGraphs;