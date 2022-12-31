import React, { useRef, useState } from "react"
import { useForm } from "react-hook-form";
import Graph from "./Graph";
import ComparativeQuerey from "./ComparativeQuerey";
import RadarGraph from "./RadarGraph";

export const CHART_COLORS = {
    red: 'rgba(255, 99, 132, .7)',
    orange: 'rgba(255, 159, 64, .7)',
    yellow: 'rgba(255, 205, 86, .7)',
    green: 'rgba(75, 192, 192, .7)',
    blue: 'rgba(54, 162, 235, .7)',
    purple: 'rgba(153, 102, 255, .7)',
    grey: 'rgba(201, 203, 207, .7)'
};

const plugin = {
    id: 'customCanvasBackgroundColor',
    beforeDraw: (chart, args, options) => {
    const {ctx} = chart;
    ctx.save();
    ctx.globalCompositeOperation = 'destination-over';
    ctx.fillStyle = options.color || '#00ffff';
    ctx.fillRect(0, 0, chart.width, chart.height);
    ctx.restore();
    }
};

const default_options = {
    plugins: {
        color: '#fff',
        subtitle: {
            display: true,
            text: 'Custom Chart Subtitle',
            color: '#fff'
        },
        legend: {
            position: 'top',
            labels: {
                color: '#fff'
            }
        },
        title: {
            display: true,
            color: '#fff',
            text: 'STACKS',
        },
        customCanvasBackgroundColor:{
            color: 'darkblue',
        },
    },
    scales: {
        x: {
            ticks: {color: "#fff",}
        },
        y: {
            ticks: {color: "#fff",}
        }
    },
    responsive: true,
    interactions:{
        intersect: false
    },
};



const testing_data = {
    labels: ['k', 'd', 'a',],
    datasets: [
        {
            id: 1,
            label: 'p1',
            data: [25,12,8],
            backgroundColor: CHART_COLORS.red,
            color: '#ffffff'
        },
        {
            id: 2,
            label: 'p2',
            data: [32,18,2],
            backgroundColor: CHART_COLORS.green,
            color: '#ffffff'
        },
    ]
}

const TestingGraph = ({  }) => {

return (
    <div>
        <div>THIS IS A TESTING COMPONENT!</div>
        <div><Graph options={default_options} data={testing_data} plugins={[plugin]}/></div>
    </div>

    )
}

export default TestingGraph