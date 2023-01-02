
import React, { useRef, useState } from "react"
import { useForm } from "react-hook-form";
import DefaultHead from '../components/defaultHead'
import OneGraph from '../components/graphing/OneGraph'
import QuereyBox from '../components/quereyBox'

// map length of datasets to id, label to target.x[n], data to target.x[n], backgroundColor: 'rgba(255, 37, 102, 1)' 

function rand_rgb() { // random colour
    let r = Math.floor(Math.random() * 256);
    let g = Math.floor(Math.random() * 256);
    let b = Math.floor(Math.random() * 256);
    return `rgb(${r}, ${g}, ${b})`;
}

const makeDataSets = (rows, targets) => {
    return targets.x.map((x_target, index) => {
        return{
        id: index,
        label: x_target,
        data: rows.map(row => row[x_target]),
        backgroundColor: rand_rgb()
        }
    }
)
}

function makeConfig(rows, targets){
    console.log(rows)
    let config = {
        data: {
            labels: rows.map(row => row[targets.y]),
            datasets: makeDataSets(rows, targets),
            },
        }
    // eventually options config'd in here too, abstraction not final so its a default constant in other file 
    console.log(config)
    return config;    


}

//



export default function Create() {


    const {register,  handleSubmit } = useForm({});
    const [GraphConfig, setGraphConfig] = useState([])

    const onSubmit = data => {
        let querey = formQuerey(data);
        fetch('http://localhost:5000/loadStats',
        {method: "POST", body: JSON.stringify({querey: querey})})
        .then(response => response.json())
        .then(response => console.log(response))
        .then(response => setGraphConfig(makeConfig(response)))
        .catch(error => console.error(error))
    }

    const testerup = data => {
        fetch('http://localhost:5000/randQuerey',
        {method: "POST", body: JSON.stringify({querey: 'its a quazza'})})
        .then(response => response.json())
        .then(response => setGraphConfig(makeConfig(response.rows, response.used_querey.targets)))
        .catch(error => console.error(error))
    }

    const onclickPurge = () => {
        setGraphConfig(() => [])
    }

    //data={graph_config.data} targets={graph_config.targets}

    return(
<div className='PageWrapper'>
    <DefaultHead />
    <div>empty</div>
    <div>header text</div>
    <div>nav bar</div>
    <div className='Explanation-Graphs'>
        <div className='ExplanationText'><QuereyBox register={register} onSubmit={testerup} handleSubmit={handleSubmit}/></div>
        
        <div className="OneGraph">
            <OneGraph graph_config={GraphConfig} />
        </div>

        <div className="OneGraph">
        2
        </div>

        <div className="OneGraph">
        3
        </div>

    </div>
</div>
);}



