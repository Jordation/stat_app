import React, { useState } from 'react';
import SimpleBar from '../graphTemplates/simpleBar'

const graph_v1 = {
            type: 'bar',
            x: [1, 2, 3], y: [2, 5, 3]
        }

const graph_v2 = {
            x: [1, 2, 3],
            y: [2, 6, 3],
            type: 'scatter',
            mode: 'lines+markers',
            marker: {color: 'red'},
        }


function MultiGraph(){
    return (
        <div className="background">
            <GraphInputs/>
            <GraphZone amount={6}/>
        </div>
    )
}

function GraphInputs() {
    return(<h1>woop doop</h1>);
}

function GraphZone(props) {
    let arr = [];
    for (let i = 0; i < props.amount; i++){
        arr.push(SpawnGraphs(graph_v1));
        arr.push(SpawnGraphs(graph_v2))
    }
    return (
        <div className="graphZone">
            {arr}
        </div>
    );
}

function SpawnGraphs(data) {
    return (<SimpleBar specs={data}/>);
}

export default MultiGraph;