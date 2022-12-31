import React, { useRef, useState } from "react"
import { useForm } from "react-hook-form";
import {
    Chart as ChartJS,
    RadialLinearScale,
    PointElement,
    LineElement,
    Filler,
    Tooltip,
    Legend,
} from 'chart.js'
import { Radar } from "react-chartjs-2";


ChartJS.register(
    RadialLinearScale,
    PointElement,
    LineElement,
    Filler,
    Tooltip,
    Legend,
    );


const RadarGraph = ( { options, data, plugin} ) => <Radar options={options} data={data} plugins={plugin} datasetIdKey="id"/>

export default RadarGraph
