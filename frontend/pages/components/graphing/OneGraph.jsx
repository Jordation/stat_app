import React, { useRef, useState } from "react"
import { useForm } from "react-hook-form";
import Graph from "./Graph";
import ComparativeQuerey from "./ComparativeQuerey";

const default_options = {
    responsive: true,
    plugins: {
    legend: {
        position: 'top',
    },
    title: {
        display: true,
        text: 'Graph Title',
    },
    },
};
// bar contains  
// data - labels [] and datasets [ { label, data[] bgc } ]
//      backgroundColor: 'rgba(255, 99, 132, 0.5)',


//


//config contains .options (wip) and .data, these are ready to map 1:1 with a graph component 
const OneGraph = ({ graph_config }) => {

return (
    <div>
        <div><ComparativeQuerey text="Querey! of comparison" /></div>
        <div>{graph_config.data && <Graph options={default_options} data={graph_config.data} />}</div>
    </div>

    )
}

export default OneGraph