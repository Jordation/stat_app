import Link from 'next/link'




export default function DefaultNav({ title }) {
return ( 
<div className='nav-wrapper'>
    <nav>
        <ul>
            <Link href="/create"  text="CREATE CUSTOM !" classname="NAVITEM">CREATE CUSTOM !</Link>
            <Link href="/playground"  text="fk around" classname="NAVITEM">fk around</Link>
            <Link href="/"  text="here i mthink" classname="NAVITEM">here i mthink</Link>
        </ul>
    </nav>
</div>
)}