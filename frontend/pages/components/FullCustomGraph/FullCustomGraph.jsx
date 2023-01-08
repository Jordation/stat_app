import TestingGraph from "./TestingGraph"
import PopoutForm from "./PopoutForm"
import React, { useState } from "react"
import { useForm } from "react-hook-form"
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
const default_graph_options = {
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

function CreateGraphData(data){
    console.log(data.x_val)
    
    let datasets = data.data.map(
        (set, index) => {
            let x_targ = data.x_val
            return {
                id: index,
                label: set.dataset,
                data: set.data.map(item => item?.[x_targ]),
                backgroundColor: rand_rgb()
            }
        }
    )

    return {
        labels: data.labels,
        datasets: datasets
    }

}
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
const FullCustomGraph = () => {



    const [popout_active, set_popout_active] = useState(false)
    const [data_for_graph, set_data_for_graph] = useState(null)
    const [current_querey, set_current_querey] = useState({})
    const {register,  handleSubmit } = useForm({});

    const submitQuerey = data => {
        set_current_querey(data);
        fetch('http://localhost:5000/processQuereyFromClient',
        {method: "POST", body: JSON.stringify({querey: data})})
        .then(res => res.json())
        .then(res => set_data_for_graph(CreateGraphData(res.data)))
        .catch(error => console.error(error))
    }

    return (
    <div className="CustomGraphRow">
        <div className="CustomGraph">
            {data_for_graph && <TestingGraph data={data_for_graph} options={default_graph_options} plugins={[plugin]}/> }
            {popout_active && <PopoutForm register={register} handleSubmit={handleSubmit} submitQuerey={submitQuerey}/>}
        </div>
        <div className="CustomQuerey">
            {JSON.stringify(current_querey)}
            <button onClick={() => set_popout_active(!popout_active)}>clicketh</button>
        </div>
    </div>
    )
}

export default FullCustomGraph