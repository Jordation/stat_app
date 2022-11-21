import React, { useState } from 'react';
import SimpleBar from '../graphTemplates/simpleBar'


function GraphZone(props) {
    return (
        <div className="graphZone">
            {SpawnGraphs(props.params)}
        </div>
    );
}

function SpawnGraphs(data) {
    return (<SimpleBar specs={data}/>);
}

export default GraphZone;