import React from 'react';
import SimpleBar from "./simpleBar";


function SpawnGraph(data) {
    return <SimpleBar specs={data}/>;
}

export default function GraphZone(props) {
    return (
        props.params && <div className="graphZone">
            {SpawnGraph(props.params)}
        </div>
    );
}
