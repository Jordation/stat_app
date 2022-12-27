import React, { useRef, useState } from "react"
import { useForm } from "react-hook-form";
import Graph from "./Graph";
import Querey from "./Querey";



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



const OneGraph = ({ graph_config }) => {

return (
    <div>
        <div><Querey /></div>
        <div><Graph options={default_options} data={graph_config.data} /></div>
    </div>

    )
}

export default OneGraph