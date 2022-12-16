
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
            <div className='p-3'> 
            The data returned by providing an initial searching scope and additional filters is returned as "rows" from the database.
            Each row has a series of values on it representing the data pertaining to one map played as def or attack rounds, or as a combined set for the map.
            </div>
            <QuereyBox />
            <GraphZone />
        </div>
            <div className='basis-1/5'> big dumb guy on the right </div>
    </div>
);}

