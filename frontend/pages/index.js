import Head from 'next/head'
import Link from 'next/link'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Bar } from "react-chartjs-2";
ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);
const labels = ['Trill', 'Maple', 'pl1xx', 'dizzyLife', 'Autumn', 'LEW', 'Arken', 'skrawl', 'Fweshest', 'andy']
const dataset = [334, 292, 236, 151, 137, 222, 189, 191, 176, 92]
const bardata = {
    labels,
    datasets: [
        {
            id: 1, label: 'Dataset', data: dataset
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
      text: 'Chart.js Bar Chart',
    },
  },
};
export default function BasePage() {
    return (
        <div>
          <Head>
            <title>VLR-Buddy Stat Tools</title>
            <meta name="description" content="analysis-tool" />
            <link rel="icon" href="/firing_gun.ico" />
          </Head>
          <div id="wrapper">
              <header id="nav-header">
                  <nav id="nav-header-inner">
                      <div className="nav-item">
                          Custom Graphs
                          <Link href="/custom">
                              <div>
                                  its a box
                              </div>
                          </Link>
                      </div>
                  </nav>
              </header>
              <div id="site-cols">
                  <div id="l"> </div>
                  <div id="c">
                      <Bar data={bardata} datasetIdKey="id" options={options}/>
                  </div>
                  <div id="r"> </div>
              </div>
          </div>
        </div>
    )
}