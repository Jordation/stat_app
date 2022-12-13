import Link from 'next/link'

const navs = [
    {
        text: "Home",
        link: "/",
    },
    {
        text: "Custom Graphing",
        link: "/custom",
    },
    {
        text: "Playground",
        link: "/flexbox",
    }
]


function NavItem(props){
return(
    <div className='nav-item w-24 h-20 text-center text-orange-300'>
        <Link href={props.link}>{props.text}</Link>
    </div>

)
}

export default function DefaultNav() {
return (
            <nav id="nav-header" className='flex justify-around flex-nowrap bg-emerald-900 text-white py-4'>
            {navs.map(item => <NavItem key={item.text} link={item.link} text={item.text}/>)}
            </nav>
    )
}