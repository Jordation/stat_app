import Link from 'next/link'




export default function DefaultNav({ title }) {
return ( 
<div className='nav-wrapper'>
    <nav>
        <ul>
            <Link href="/create"  text="CREATE CUSTOM !" className="NAVITEM">CREATE CUSTOM !</Link>
            <Link href="/playground"  text="fk around" className="NAVITEM">fk around</Link>
            <Link href="/"  text="here i mthink" className="NAVITEM">here i mthink</Link>
        </ul>
    </nav>
</div>
)}