
import React, { useEffect, useState } from 'react';
import GeneralButton from '../components/button';
import ModGraph from './modularGraph';

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
function fakeGraph(){

	let entryData = FAKEdata();
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

const GraphZone = () => {
var init_data = fakeGraph();
const graph_types = ['bar', 'line', 'pie']
const [currKey, setCurrKey] = useState("Graph_I")
const [graphs, setGraphs] = useState([])

const handleSubmitClick = () => {
	let newkey = (currKey + "I")
	setCurrKey(newkey);
	let new_data = fakeGraph();
	graphs.push(<ModGraph key={newkey} cfg={new_data} type={graph_types[rn(1,3)]}/>)
	setGraphs([...graphs])
}

const handleDelClick = () => {
	let len = graphs.length
	graphs.pop((len-1))
	setGraphs([...graphs])
}
//
return(
	<div>
		<GeneralButton onClick={handleSubmitClick} btntext="add graph"/>
		<GeneralButton onClick={handleDelClick} btntext="remove graph"/>
		<div className='flex flex-wrap flex-initial'>
			{[...graphs]}
		</div>
	</div>
)
}
export default GraphZone;