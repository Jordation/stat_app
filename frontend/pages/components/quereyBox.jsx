
import GeneralButton from "./button";
import { useState } from "react"
import { useForm } from "react-hook-form";





const filter_options =[
    {v: "on_map", t: "Filter results by map played"},
    {v: "on_agent", t: "Filter results by agent played"},
    {v: "on_team", t: "Filter results by team"},
    {v: "vs_team", t: "Search for results vs a specific team"},
]
const scope_options = [
    {v: "all", t: "all"},
    {v: "from_event", t: "from event"},
    {v: "from_series", t: "from series"},
    {v: "from_map", t: "from map"},
    {v: "from_player", t: "from player"},
    
]
const target_options = [
    {v: "x_target", t: "x axis target value"},
    {v: "y_target", t: "y axis target value"},
    {v: "side_target", t: "Filter by atk, "},
]

export default function QuereyBox({register, onSubmit, handleSubmit}){
return(
<div className="flex flex-wrap">
    <form onSubmit={handleSubmit(onSubmit)} className="grid grid-flow-row gap-1 basis-full w-full">
        <div className="flex">
            <select {...register("scope_type")} className="border rounded p-2 m-1 border-black text-center basis-1/2 w-full text-ellipsis">
                {scope_options.map(vals => <option key={vals.v} value={vals.v}>{vals.t}</option>)}
            </select>
            <input {...register("scope_value")}type={"text"} className="border rounded p-2 m-1 border-black text-center basis-1/2 w-full text-ellipsis"/>
        </div>    
        <div className="flex">
            <select {...register("filter_type")} className="border rounded p-2 m-1 border-black text-center basis-1/2 w-full text-ellipsis">
                {filter_options.map(vals => <option key={vals.v} value={vals.v}>{vals.t}</option>)}
            </select>
            <input {...register("filter_value")}type={"text"} className="border rounded p-2 m-1 border-black text-center basis-1/2 w-full text-ellipsis"/>
        </div>

        <div className="flex">
            <div className="flex flex-nowrap justify-around basis-1/2">
                <input {...register("x_target")} type={"text"}  placeholder="x target" className="flex text-center p-2 m-1"/>
                <input {...register("y_target")} type={"text"} placeholder="y target" className="flex text-center p-2 m-1"/>
                <input {...register("side_target")} type={"text"} placeholder="side target" className="flex text-center p-2 m-1"/>
            </div>
            <div className="border rounded p-2 m-1 border-black text-center text-ellipsis basis-1/4 justify-center flex ">
                <input type="submit"/>
            </div>
        </div>
    </form>
</div>
)
}