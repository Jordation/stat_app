import React, { useRef, useState } from "react"
import { useForm } from "react-hook-form";


const ComparativeQuerey = ({ text }) => {

const [propTExt, setpropTExt] = useState(text)

return (
    <div>
    {propTExt}
    </div>
    )
}


export default ComparativeQuerey