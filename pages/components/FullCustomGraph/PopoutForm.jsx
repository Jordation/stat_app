
import FullCustomQuerey from "./FullCustomQuerey"

const non_numeric_ops = [
    {option: 'Player', value: 'player'},
    {option: 'Agent', value: 'agent'},
    {option: 'Team', value: 'team'},
    {option: 'Map', value: 'mapname'},
]
const numeric_ops = [
    {option: 'ACS', value: 'acs'},
    {option: 'Rating', value: 'lol u have to add this still'},
    {option: 'Kills', value: 'k'},
    {option: 'Deaths', value: 'd'},
    {option: 'Assists', value: 'a'},
    {option: 'First Bloods', value: 'fb'},
    {option: 'First Deaths', value: 'fd'},
    {option: 'Headshot %', value: 'hsp'},
    {option: 'Average Damage/Round', value: 'adr'},
    {option: 'KAST', value: 'kast'},
]

const side_ops = [
    {option: "Combined Stat-line", value: 'combined'},
    {option: "Attack Stat-lines", value: 'attack'},
    {option: "Defence Stat-lines", value: 'defence'}
]

const PopoutForm = ({register, handleSubmit, submitQuerey}) => {
    return(
        <div className="PopoutForm">
        <form onSubmit={handleSubmit(submitQuerey)}>
            <label className="label">Graph Y Target</label>
            <select {...register('graph_shape.y')}>
                {non_numeric_ops.map(op => <option key={op.value}  value={op.value}>{op.option}</option>)}
            </select>
            <label className="label">Graph X Target</label>
            <select {...register('graph_shape.x')}>
                {numeric_ops.map(op => <option key={op.value}  value={op.value}>{op.option}</option>)}
            </select>
            <label className="label">Group datasets by</label>
            <select {...register('graph_shape.dataset_group_by')}>
                {non_numeric_ops.map(op => <option key={op.value}  value={op.value}>{op.option}</option>)}
            </select>
            
            <div className='input-group'>
                <label className='label'>Data grouping targets</label>
                <input className="input" type={'text'} placeholder="Separate with commas" {...register('data_shape.group_targets')}/>
                <label className='label'>Order results by</label>
                <input className="input" type={'text'} placeholder="Separate with commas" {...register('data_shape.order_by')}/>
            </div>
            <div className="input-group">
                <label className="label">Initial row search requirements</label>
                <label className="label">From Maps:</label>
                <input className="input" type={'text'} placeholder="Separate with commas" {...register('row_reqs.on_mapname')}/>
                <label className="label">Playing Agents:</label>
                <input className="input" type={'text'} placeholder="Separate with commas" {...register('row_reqs.on_agent')}/>
                <label className="label">On Team::</label>
                <input className="input" type={'text'} placeholder="Separate with commas" {...register('row_reqs.on_team')}/>
                <label className="label">Specific Players:</label>
                <input className="input" type={'text'} placeholder="Separate with commas" {...register('row_reqs.on_player')}/>
            </div>

            <select {...register('side')}>
                {side_ops.map(op => <option key={op.value}  value={op.value}>{op.option}</option>)}
            </select>

            <input type='submit'/>
        </form>
        </div>
    )
}

export default PopoutForm