
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
const ModGraph = ({ data, options, ctype }) => {

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

const graphClasses = "h-1/2 w-full"

switch(ctype) {
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
        return (<div>catastrophy</div>)
  }
}
export default ModGraph;