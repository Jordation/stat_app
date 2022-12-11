import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend,
  } from 'chart.js'
import { Bar } from "react-chartjs-2";
import React, { useEffect, useState } from 'react';
import GeneralButton from '../components/button';


const options = {
    responsive: true,
  plugins: {
    legend: {
      position: 'top',
    },
    title: {
      display: true,
      text: 'im working',
    },
  },
};



function rn(min, max) { // random number
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }

function FAKEdata(){
    let names = ["One", "Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten",]
    let data = []
    for (let i=0;i<10;++i){
        data.push({l: names[i], v: rn(5,50)})
    } 
    return data
}
const arr = [fakeGraph(0)];
export function fakeGraph(i){
    let entryData = FAKEdata();
    let cfg = {
        data: {
            labels: entryData.map(row => row.l),
            datasets: [
                {
                id: 1,
                label: "data",
                data: entryData.map(row => row.v),
                backgroundColor: 'rgba(53, 162, 235, 0.5)'
                },
        ],
        },
        options: options,
        iter: i
    }
    return cfg;
}

const GraphZone = () => {
ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend
  );

  let i = 1;

const [graphs, setGraphs] = useState(
    arr.map(set => 
    <div key={set.iter}>
    <Bar data={set.data} options={set.options} datasetIdKey="id"/>
    </div>))

const handleClick = () => {
    i++;
    arr.push(fakeGraph(i));
    setGraphs(arr.map(set => 
        <div key={set.iter}>
        <Bar data={set.data} options={set.options} datasetIdKey="id"/>
        </div>))
 
}

return(
    <div>
        <GeneralButton onClick={handleClick} btntext="click"/>
        <div className='grid grid-cols-2 h-full'>
            {graphs}
        </div>
    </div>
)
}
export default GraphZone;