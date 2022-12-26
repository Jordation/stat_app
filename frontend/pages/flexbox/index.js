
import React, { useRef, useState } from "react"
import { useForm } from "react-hook-form";
import GraphZone from '../components/graphZone'
import DefaultNav from '../components/defaultNav'
import DefaultHead from '../components/defaultHead'
import QuereyBox from '../components/quereyBox'

const options = {
	responsive: true,
    scaleFontColor: "#000000",
	plugins: {
	legend: {
		position: 'top',
	},
	title: {
		display: false,
		text: 'im working',
			},
	},
};

function formQuerey(inQuerey){
    let newQuerey = {
        'scope': {
            'all': '',
            'from_event': '',
            'from_series': '',
            'from_map': '',
            'from_player': '',
        },
        'filters': {
            'on_map': '',
            'on_agent': '',
            'on_team': '',
        },
        'targets': {
            'x': '',
            'y': '',
            'max_columns': ''
        }
    }
    newQuerey.scope[inQuerey.scope_type] = inQuerey.scope_value;
    newQuerey.filters.on_map = inQuerey.on_map;
    newQuerey.filters.on_agent = inQuerey.on_agent;
    newQuerey.filters.on_team = inQuerey.on_team;
    newQuerey.targets.x = inQuerey.x;
    newQuerey.targets.y = inQuerey.y;
    newQuerey.targets.max_columns = inQuerey.max_columns;
    return newQuerey;
}

function makeGraph(data, title, graph_targets){

	let entryData = data;
	let cfg = {
		data: {
			labels: entryData.map(row => row.l),
				datasets: [{
					id: 1,
					label: title,
					data: entryData.map(row => row.v),
					backgroundColor: 'rgba(255, 37, 102, 1)'
					},
				],
			},
			options: options,
		}	
	return cfg;
}


export default function flexbox() {


    const graph_targets = useRef({l: 1, x: 1})
    const {register,  handleSubmit } = useForm({});
    const [dataSets, setDataSets] = useState([])

    const onSubmit = data => {
        let querey = formQuerey(data);
        fetch('http://localhost:5000/loadStats',
        {method: "POST", body: JSON.stringify({querey: querey})})
        .then(response => response.json())
        .then(response => {
            console.log(response)
            //let newCFG = makeGraph(response, querey.targets.x);
            //setDataSets(() => [...dataSets, newCFG]) 
        }
    )
}
    

    const onclickPurge = () => {
        setDataSets(() => [])
    }

    return(
<div className='PageWrapper'>
    <DefaultHead />
    <div>empty</div>
    <div>header text</div>
    <div>nav bar</div>
    <div className='Querey-Explanation-Graphs'>
        <div className='Querey-Zone'>
            <QuereyBox register={register} onSubmit={onSubmit} handleSubmit={handleSubmit}/>
            <div>explanation</div>
        </div>
        {dataSets && <GraphZone graphs={dataSets} onClick={onclickPurge}/>}
    </div>
</div>
);}



