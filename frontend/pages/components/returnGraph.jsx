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

const labels = ['Trill', 'Maple', 'pl1xx', 'dizzyLife', 'Autumn', 'LEW', 'Arken', 'skrawl', 'Fweshest', 'andy']
const dataset = [334, 292, 236, 151, 137, 222, 189, 191, 176, 92]
const dataset2 = [33, 29, 23, 15, 13, 22, 18, 19, 17, 9]

const bardata = {
      labels,
      datasets: [
          {
              id: 1, label: 'ACS', data: dataset
          }
          ]
  }
const bardata2 = {
      labels,
      datasets: [
          {
              id: 2, label: 'Kills', data: dataset2
          }
          ]
  }
  
const options = {
    responsive: false,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: '',
      },
    },
  };

function fakeProps(number){
    let values = {options: options, data: {}}
    values.options = options
    if(number > 1){
        values.data = bardata2
    } else {
        values.data = bardata
    }
    return values
}

                      /*<Bar data={bardata} datasetIdKey="id" options={options}/>*/
export default function ReturnGraph(props){
    ChartJS.register(
        CategoryScale,
        LinearScale,
        BarElement,
        Title,
        Tooltip,
        Legend
      );

    let fakeprops = fakeProps(props.number)

    return(
        <div>
            <Bar data={fakeprops.data} datasetIdKey="id" options={fakeprops.options}/>
        </div>
    )


}