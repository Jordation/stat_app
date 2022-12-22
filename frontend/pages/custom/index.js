
import React, { useState } from 'react';
import DefaultNav from '../components/defaultNav'
import DefaultHead from '../components/defaultHead'

function FormTests() {
    return(
        <div className='flex flex-row overflow-hidden text-purple-100'>
            <DefaultHead />
            <div className='basis-1/6'>123</div>
            <div className='basis-4/6'>
                <DefaultNav/>
                <div className='container flex'>
                    <div className='w-1/2 text-center mx'>
                        <label className='block'>Filter by maps: 
                        <input className='block rounded' type="text"></input>
                        </label>
                    </div>
                    <div className='w-1/3 text-center mx'>
                        <label className=''>Filter by maps: 
                        <input className='rounded' type="text"></input>
                        </label>
                    </div>
                </div>
            </div>
            <div className='basis-1/6'>321</div>
        </div>
    );}
    


export default FormTests;