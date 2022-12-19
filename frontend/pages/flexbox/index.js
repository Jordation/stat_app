
import React, { useEffect, useState } from "react"
import { useForm } from "react-hook-form";
import GraphZone from '../components/graphZone'
import DefaultNav from '../components/defaultNav'
import DefaultHead from '../components/defaultHead'
import QuereyBox from '../components/quereyBox'


const options = {
	responsive: true,
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

const filters = {
    on_map: "",
    on_agent: "",
    on_team: "",
    x_target: "",
    y_target: "",
    side_target: ""
}

const querey = {
    scope_type: "",
    scope_value: "",
    filters
}

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
            'vs_team': '',
        },
        'targets': {
            'x': '',
            'y': '',
            'side': ''
        }
    }
    newQuerey.scope[inQuerey.scope_type] = inQuerey.scope_value;
    newQuerey.filters[inQuerey.filter_type] = inQuerey.filter_value;
    newQuerey.targets.x = inQuerey.x_target;
    newQuerey.targets.y = inQuerey.y_target;
    newQuerey.targets.side = inQuerey.side_target;
    return newQuerey;
}
function makeGraph(data){

	let entryData = data;
	let cfg = {
		data: {
			labels: entryData.map(row => row.l),
				datasets: [{
					id: 1,
					label: "data",
					data: entryData.map(row => row.v),
					backgroundColor: 'rgba(53, 162, 235, 0.5)'
					},
				],
			},
			options: options,
		}	
	return cfg;
}


export default function flexbox() {

    const {register,  handleSubmit } = useForm(querey);
    const [dataSets, setDataSets] = useState([])
    const onSubmit = data => {
        console.log(formQuerey(data))
        fetch('http://localhost:5000/loadStats',
        {method: "POST", body: JSON.stringify({querey: formQuerey(data)})})
        .then(response => response.json())
        .then(response => {
            console.log(response)
            let newCFG = makeGraph(response);
            setDataSets(() => [...dataSets, newCFG]) 
        }
    )
}
    

    const onclickPurge = () => {
        setDataSets(() => [])
    }

    return(
    <div className='flex flex-row overflow-hidden'>
        <DefaultHead />
        <div className='basis-1/5'>big dumb guy on the left</div>
        <div className='basis-3/5'>
        <DefaultNav/>
            <div className='p-3'> 
            The data returned by providing an initial searching scope and additional filters is returned as "rows" from the database.
            Each row has a series of values on it representing the data pertaining to one map played as def or attack rounds, or as a combined set for the map.
            </div>
            <QuereyBox register={register} onSubmit={onSubmit} handleSubmit={handleSubmit}/>
            {dataSets && <GraphZone graphs={dataSets} onClick={onclickPurge}/>}
        </div>
            <div className='basis-1/5'> big dumb guy on the right </div>
    </div>
);}

