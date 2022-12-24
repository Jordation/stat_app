
import GeneralButton from "./button";
import { useState } from "react"
import { useForm } from "react-hook-form";


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

export default function QuereyBox({register, onSubmit, handleSubmit}){
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
                {target_options.map((values) => <option key={values.val} value={values.val}>{values.op}</option>)}
                </select>
            </label>
            </div>

            <div className="input-holder">
            <label > Y Value
                <select {...register("y")} className='Form-Item' >
                {target_options.map((values) => <option key={values.val} value={values.val}>{values.op}</option>)}
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