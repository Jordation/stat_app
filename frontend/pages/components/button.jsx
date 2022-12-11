export default function GeneralButton(props){
    return(
    <button onClick={props.onClick} className="bg-blue-500 text-white px-4 py-2 rounded">
        {props.btntext}
    </button>
    )
}
