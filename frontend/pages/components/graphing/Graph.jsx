import React, { useRef, useState } from "react"
import { useForm } from "react-hook-form";
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend,
    ArcElement,
    LineElement,
    PointElement,
} from 'chart.js'
import { Bar, Pie, Line } from "react-chartjs-2";

ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend,
    ArcElement,
    LineElement,
    PointElement,
    );




const Graph = ( { options, data} ) => {


return (
    <div>
        <Bar options={options} data={data} />;
    </div>
    )
}

export default Graph