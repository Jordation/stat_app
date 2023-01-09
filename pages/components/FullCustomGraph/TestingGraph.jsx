import React, { useRef, useState } from "react"
import { set, useForm } from "react-hook-form";
import BarGraphComponent from "./BarGraphComponent"

const TestingGraph = ({ data, options, plugins}) => {

return (
        <BarGraphComponent data={data} options={options} plugins={plugins}/>
    )
}

export default TestingGraph