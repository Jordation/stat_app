
import React, { useState } from 'react';
import GraphZone from "../../components/ui/multiGraph";
function UrlToGraphs() {
    const [graphParams, setGraphParams] = useState({});
    const [url, setUrl] = useState("");
    const [y_val, set_y_val] = useState("");
    const getData = () => {
        console.log(y_val)
        fetch('http://localhost:5000/loadStats', {
            method: 'POST',
            body: JSON.stringify({ url: url, y_field: y_val })
          }
        )
    .then(response => response.json())
    .then((response) => {
            console.log(response)
            setGraphParams(response)
            console.log(graphParams)
            }
        )
    }

    return(
        <div>
            <input type="text" onChange={e => setUrl(e.target.value)}/>
            <label>select fields to search: </label>
            <select id="y field" onChange={e => set_y_val(e.target.value)}>
                <option value="Kills">Kills</option>
                <option value="ACS">ACS</option>
                <option value="First Bloods">FB</option>
                <option value="Headshot %">HS%</option>
            </select>
            <input type="submit" value="generate graph" onClick={getData}/>
            <br/>
            <GraphZone params = {graphParams}/>
        </div>
        // figure out how to take params and load graphs AFTER some  async
        // no doubt
    )
}


export default UrlToGraphs;