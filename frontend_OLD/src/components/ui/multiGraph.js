import React from 'react';
import SimpleBar from '../graphTemplates/simpleBar'


function GraphZone(props) {
    return (
        props.params && <div className="graphZone">
            {SpawnGraph(props.params)}
        </div>
    );
}

function SpawnGraph(data) {
    return (<SimpleBar specs={data}/>);
}

export default GraphZone;