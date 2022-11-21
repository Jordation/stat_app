import React from 'react';
import Plot from 'react-plotly.js';

function SimpleBar(props){
    return (
      <Plot
        data={[props.specs]}
        layout={ {width: 800, height: 350, title: 'da plot'} }
      />
    );
  }
export default SimpleBar;