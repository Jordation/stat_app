
import GeneralButton from "./button";
import { useState } from "react"
import { useForm } from "react-hook-form";

const filters = {
    on_map: "",
    on_agent: "",
    on_team: "",
    x_target: "",
    y_target: "",
    side_target: ""
}

const query = {
    scope_type: "",
    scope_value: "",
    filters
}

export default function QuereyBox(){

    const {register,  handleSubmit } = useForm(query);
    const [curr_form, setcurr_form] = useState("hey")
    const onSubmit = data => setcurr_form(JSON.stringify(data))

return(
<div className="flex flex-wrap">
    <div className="w-full">{curr_form}</div>
    <form onSubmit={handleSubmit(onSubmit)} className="grid grid-flow-row gap-1 basis-full w-full">
        <div className="flex">
            <select {...register("scope_type")} className="border rounded p-2 m-1 border-black text-center basis-1/2 w-full text-ellipsis">
                <option value="all">all</option>
                <option value="from_event">from event</option>
                <option value="from_series">from series</option>
                <option value="from_map">from map</option>
                <option value="from_player">from player</option>
            </select>
            <input {...register("scope_value")}type={"text"} className="border rounded p-2 m-1 border-black text-center basis-1/2 w-full text-ellipsis"/>
        </div>    
        <div className="flex">
            <select {...register("filter_type")} className="border rounded p-2 m-1 border-black text-center basis-1/2 w-full text-ellipsis">
                <option value="on_map">Filter results by map played</option>
                <option value="on_agent">Filter results by agent played</option>
                <option value="on_team">Filter results by team</option>
                <option value="vs_team">Search for results vs a specific team </option>
                <option value="x_target">x axis target value</option>
                <option value="y_target">y axis target value</option>
                <option value="side_target">Filter by side played</option>
            </select>
            <input {...register("filter_value")}type={"text"} className="border rounded p-2 m-1 border-black text-center basis-1/2 w-full text-ellipsis"/>
        </div>
        <div className="border rounded p-2 m-1 border-black text-center text-ellipsis w-1/2 justify-center flex ">
        <input type="submit"/>
        </div>
    </form>
</div>
)
}