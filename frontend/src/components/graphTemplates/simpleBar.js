import React from 'react';
import Plot from 'react-plotly.js';

function SimpleBar(props){
    return (
      <Plot
        data={[props.specs]}
        layout={ {width: 320, height: 240, title: 'A Fancy Plot'} }
      />
    );
  }
export default SimpleBar;