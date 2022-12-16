
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


const filters = {
    on_map: "",
    on_agent: "",
    on_team: "",
    x_target: "",
    y_target: "",
    side_target: ""
}

const querey = {
    scope_type: "",
    scope_value: "",
    filters
}

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
            'vs_team': '',
            'x_target': '',
            'y_target': '',
            'side_target': '',
        }
    }
    newQuerey.scope[inQuerey.scope_type] = inQuerey.scope_value;
    newQuerey.filters[inQuerey.filter_type] = inQuerey.filter_value;
    newQuerey.filters.x_target = inQuerey.x_target;
    newQuerey.filters.y_target = inQuerey.y_target;
    newQuerey.filters.side_target = inQuerey.side_target;
    return newQuerey;
}
export default function QuereyBox(){

    const {register,  handleSubmit } = useForm(querey);
    const [curr_form, setcurr_form] = useState("hey")
    const onSubmit = data => {
        setcurr_form(formQuerey(data));
        fetch('http://localhost:5000/loadStats',
        {method: "POST", body: JSON.stringify({querey: curr_form})})
        .then(response => response.json())
        .then(response => console.log(response))
    }
    


return(
<div className="flex flex-wrap">
    <div className="w-full">{JSON.stringify(curr_form)}</div>
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