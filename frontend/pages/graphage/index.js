
import React, { useEffect, useState } from "react"

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

const generateData = (amount) => {
    let data = [];
    for (let i = 0; i < amount; i++) {
        data.push({
            l: "word" + i,
            v: Math.floor(Math.random() * 100),
        });
    }
    return data;
}

const Graphage = () => {

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

    const data = generateData(10)


    return(
        <div>
            <h1>Graphage</h1>
        </div>
    )
}

export default Graphage;