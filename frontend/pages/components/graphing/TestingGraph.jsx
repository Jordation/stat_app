import React, { useRef, useState } from "react"
import { set, useForm } from "react-hook-form";
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

function rand_rgb() { // random colour
    let r = Math.floor(Math.random() * 256);
    let g = Math.floor(Math.random() * 256);
    let b = Math.floor(Math.random() * 256);
    return `rgb(${r}, ${g}, ${b})`;
}

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
            color: '#333333',
        },
    },
    scales: {
        x: {
            ticks: {color: "#fff"},
            grid: { color: "#fff" }
        },
        y: {
            ticks: {color: "#fff"},
            grid: { color: "#fff" },
            linewidth: 10
        }
    },
    responsive: true,
    interactions:{
        intersect: false
    },
};



const testing_data = {
    labels: ['one', 'two', 'three'],
    datasets: [
        {
            id: 1,
            label: 'one',
            data: [1,2,3],
            backgroundColor: 'red',
        },
        {
            id: 2,
            label: 'two',
            data: [3,2,1],
            backgroundColor: 'blue',
        },
    ]
}



function makelabel(group) {
    
}

function CreateGraphData(data){
    let datasets = data.data.map(
        (set, index) => {
            return {
                id: index,
                label: set.group,
                data: set.data.map(item => item?.fd),
                backgroundColor: rand_rgb()
            }
        }
    )

    return {
        labels: data.labels,
        datasets: datasets
    }

}

const TestingGraph = ({ data }) => {

    const [graph_data, set_graph_data] = useState(CreateGraphData(data))

return (
        <Graph options={default_options} data={graph_data} plugins={[plugin]}/>
    )
}

export default TestingGraph