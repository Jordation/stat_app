
import React, { useRef, useState } from "react"

import DefaultHead from './components/defaultHead'

import TestingGraph from "./components/FullCustomGraph/TestingGraph";
import PopoutForm from "./components/FullCustomGraph/PopoutForm";
import FullCustomGraph from "./components/FullCustomGraph/FullCustomGraph";

export default function PlayGround() {


    return(
    <div className='PageWrapper'>
        <DefaultHead />
        <div>empty</div>
        <div>header text</div>
        <div>nav bar</div>
        
        <div className="GraphArea">

        <FullCustomGraph />

        </div>
    </div>
);}


