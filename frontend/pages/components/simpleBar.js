import React from 'react';

import dynamic from "next/dynamic";
const Plot = dynamic(() => import("react-plotly.js"), { ssr: false, })

export default function SimpleBar(props){
    return (
        <div>
          <Plot
            data={[props.specs]}
            layout={ {width: 800, height: 350, title: 'players and kills in match'} }
          ></Plot>
        </div>
    );
  }