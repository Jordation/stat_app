
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend,
    ArcElement,
    LineElement,
    PointElement,
  } from 'chart.js'
  import { Bar, Pie, Line } from "react-chartjs-2";
const ModGraph = (props) => {

    ChartJS.register(
        CategoryScale,
        LinearScale,
        BarElement,
        Title,
        Tooltip,
        Legend,
        ArcElement,
        LineElement,
        PointElement,
      );
const graphClasses = "basis-1/3"
let data = props.cfg.data
let options = props.cfg.options
switch(props.type) {
    case 'bar':
      return (<div className={graphClasses}>
      <Bar data={data} options={options} datasetIdKey="id"/></div>)
    case 'line':
        return (<div className={graphClasses}>
        <Line data={data} options={options} datasetIdKey="id"/></div>)
    case 'pie':
        return (<div className={graphClasses}>
        <Pie data={data} options={options} datasetIdKey="id"/></div>)
    default:
        return (<div className={graphClasses}>
        <Bar data={data} options={options} datasetIdKey="id"/></div>)
  }
}
export default ModGraph;