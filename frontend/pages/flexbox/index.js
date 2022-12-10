import Head from 'next/head'
import Link from 'next/link'
import React from "react"

export default function flexbox() {
    return(
    <div>
        <Head>
            <title>VLR-Buddy Stat Tools</title>
            <meta name="description" content="analysis-tool" />
            <link rel="icon" href="/firing_gun.ico" />
          </Head>
          
        <div className="flex">
            <div className="flex-1">
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
                    <GrapZoner />
                </div>
            </div>
            <div className="flex-1">
                3
            </div>
            </div>
    </div>
    )
}

function GrapZoner() {
    return(
        <div className="grid grid-cols-2 gap-10 w-full p-2">
            <div>
                one
            </div>
            <div>
                two
            </div>
            <div>
                three
            </div>
            <div>
                four
            </div>
            <div>
                five
            </div>
        </div>
    )
}