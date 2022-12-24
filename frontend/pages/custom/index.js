

import DefaultNav from '../components/defaultNav'
import DefaultHead from '../components/defaultHead'
import QuereyBox from '../components/quereyBox';

import React, { useEffect, useState } from "react"
import { useForm } from "react-hook-form";
import GraphZone from '../components/graphZone'



const target_options = [
    { op: "Player Name", val: "player"},
    { op: "Agent Name", val: "agent"},
    { op: "Team", val: "team"},
    { op: "ACS", val: "acs"},
    { op: "Kills", val: "k"},
    { op: "Deaths", val: "d"},
    { op: "Assists", val: "a"},
    { op: "KAST", val: "kast"},
    { op: "First Bloods", val: "fb"},
    { op: "First Deaths", val: "fd"},
    { op: "Map Name", val: "mapname"},
]

function formQuerey(inQuerey){
    let newQuerey = {
        'scope': {
            'all': '',
            'from_event': '',
            'from_series': '',
            'from_map': '',
            'from_player': '',
        },
        'filters': {
            'on_map': '',
            'on_agent': '',
            'on_team': '',
        },
        'targets': {
            'x': '',
            'y': '',
            'max_columns': ''
        }
    }
    newQuerey.scope[inQuerey.scope_type] = inQuerey.scope_value;
    newQuerey.filters.on_map = inQuerey.on_map;
    newQuerey.filters.on_agent = inQuerey.on_agent;
    newQuerey.filters.on_team = inQuerey.on_team;
    newQuerey.targets.x = inQuerey.x;
    newQuerey.targets.y = inQuerey.y;
    newQuerey.targets.max_columns = inQuerey.max_columns;
    return newQuerey;
}

const QuereyBoxx = () => {
    const { register, handleSubmit } = useForm();
    
    const onSubmit = data => console.log(formQuerey(data))
    
    return(
        <div className='Querey-Box'>
        <form onSubmit={handleSubmit(onSubmit)}>
        <div className='input-holder'>
            <select {...register("scope_type")} className='Form-Item'>
                <option value="all">All Data</option>
                <option value="from_event">Filter by event</option>
                <option value="from_series">Filter by series</option>
                <option value="from_player">Filter by player</option>
            </select>
            <label>Scope Value
                <input {...register("scope_value")} type="text" className='Form-Item'/>
            </label>
            </div>
            <div className="input-holder">
            <label>Map Filters
                <input {...register("on_map")} type="text" placeholder="split filters with commas" className='Form-Item' />
            </label>
            </div>

            <div className="input-holder">
            <label>Agent Filters
                <input {...register("on_agent")} type="text" placeholder="split filters with commas" className='Form-Item' />
            </label>
            </div>

            <div className="input-holder">
            <label>Team Filters
                <input {...register("on_team")} type="text" placeholder="split filters with commas" className='Form-Item' />
            </label>
            </div>

            <div className="input-holder">
            <label>X Value
                <select {...register("x")} className='Form-Item' >
                {target_options.map((values) => <option value={values.val}>{values.op}</option>)}
                </select>
            </label>
            </div>

            <div className="input-holder">
            <label > Y Value
                <select {...register("y")} className='Form-Item' >
                {target_options.map((values) => <option value={values.val}>{values.op}</option>)}
                </select>
            </label>
            </div>

            <div className="input-holder">
            <label> Max Columns 
                <input {...register("max_columns")} type="number" className='Form-Item' />
            </label>
            </div>
            <div className='input-holder'>
            <input type="submit" className='Form-Item'/>
            </div>
        </form>
        </div>
    )
}

const FormTests = () => {

    
    return(
        <div className='PageWrapper'>
            <div>one</div>
            <div>two</div>
            <div>navywavy</div>
            <div className='Querey-Explanation-Graphs'>
                <div className='Querey-Zone'>
                    <QuereyBox />
                    <div>explanation</div>
                </div>
                <div>six</div>
            </div>
        </div>
    );}
    


export default FormTests;