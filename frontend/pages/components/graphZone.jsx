
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
					backgroundColor: 'rgba(255, 37, 102, 1)'
					},
				],
			},
			options: options,
		}	
	return cfg;
}

const GraphZone = ({graphs, onClick}) => {

	const [graphArr, setgraphArr] = useState([])

useEffect(() => {
setgraphArr([...graphs])

},[graphs])

return(
	<div>
		<GeneralButton onClick={onClick} btntext="clear graphs" />
		<div className='Graph-Wrapper'>
			{graphArr?.map(config => <ModGraph data={config.data} options={config.options} ctype={"bar"} />)}
		</div>
	</div>
)
}
export default GraphZone;