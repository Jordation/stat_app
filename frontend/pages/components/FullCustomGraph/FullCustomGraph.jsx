import TestingGraph from "../graphing/TestingGraph"
import PopoutForm from "./PopoutForm"
import React, { useState } from "react"

const FullCustomGraph = () => {



    const [popout_active, set_popout_active] = useState(false)
    const [data_return, set_data_return] = useState(null)

    const current_querey = {something: 'filterval'}

    return (
    <div className="CustomGraphRow">
        <div className="CustomGraph">
            {data_return && <TestingGraph data={data_return}/> }
        </div>

        {popout_active && <PopoutForm />}

        <div className="CustomQuerey">
            {JSON.stringify(current_querey)}
            <button onClick={() => set_popout_active(!popout_active)}>clicketh</button>
        </div>
    </div>
    )
}

export default FullCustomGraph