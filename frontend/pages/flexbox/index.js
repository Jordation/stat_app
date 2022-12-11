
import Head from 'next/head'
import Link from 'next/link'
import React, { useEffect, useState } from "react"
import GraphZone from '../components/graphZone'
import GeneralButton from '../components/button'
import { fakeGraph } from '../components/graphZone'



export default function flexbox() {

return(
<div className='h-full'>
    <Head>
        <title>VLR-Buddy Stat Tools</title>
        <meta name="description" content="analysis-tool" />
        <link rel="icon" href="/firing_gun.ico" />
      </Head>
      
    <div className="flex">
        <div className="flex-1 h-full">
            1
        </div>
        <div className="w-2/3">
            <nav id="nav-header" className='grid grid-cols-3 w-full'>
                <div className="nav-item">
                    <Link href="/custom">Custom Graphs</Link>
                </div>
                <div className="nav-item">
                    <Link href="/flexbox">Playground</Link>
                </div>
                <div className="nav-item col-span-1">
                    <Link href="/">3rd nav item!</Link>
                </div>
            </nav>
            <div className='w-full p-2'>
                other garbage
            </div>
            <div className='p-3'>
                <GraphZone/>
            </div>
        </div>
        <div className="flex-1 h-full">
            3
        </div>
        </div>
</div>
);}
