
import Head from 'next/head'
import Link from 'next/link'
import React, { useEffect, useState } from "react"

import GraphZone from '../components/graphZone'
import DefaultNav from '../components/defaultNav'
import DefaultHead from '../components/defaultHead'
import QuereyBox from '../components/quereyBox'


export default function flexbox() {
    return(
    <div className='flex flex-row'>
        <DefaultHead />
        <div className='basis-1/5'>big dumb guy on the left</div>
        <div className='basis-3/5'>
        <DefaultNav/>
            <div> 2 </div>
            <QuereyBox />
            <div> <GraphZone /> </div>
        </div>
            <div className='basis-1/5'> big dumb guy on the right </div>
    </div>
);}
// return(
// <div>
//     <DefaultHead />
//     <DefaultNav />
//     <div className='flex justify-self-auto'>
//         <div className="basis-3/5">
//             <div className='w-full p-2'>other garbage</div>
//             <QuereyBox/>
//             <GraphZone/>
//         </div>
//     </div>
// </div>
