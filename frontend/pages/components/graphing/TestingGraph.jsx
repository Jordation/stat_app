import React, { useRef, useState } from "react"
import { set, useForm } from "react-hook-form";
import Graph from "./Graph";
import ComparativeQuerey from "./ComparativeQuerey";
import RadarGraph from "./RadarGraph";







const TestingGraph = ({ data, options, plugins}) => {

return (
        <Graph data={data} options={options} plugins={plugins}/>
    )
}

export default TestingGraph