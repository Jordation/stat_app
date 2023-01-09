import React, { useRef, useState } from "react"
import { set, useForm } from "react-hook-form";
import Graph from "../graphing/Graph";
import ComparativeQuerey from "../graphing/ComparativeQuerey";
import RadarGraph from "../graphing/RadarGraph";







const TestingGraph = ({ data, options, plugins}) => {

return (
        <Graph data={data} options={options} plugins={plugins}/>
    )
}

export default TestingGraph