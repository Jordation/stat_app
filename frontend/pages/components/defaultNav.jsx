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
    <div className='nav-item w-24 h-10 text-center text-orange-300 text-sm'>
        <Link className='text-center' href={props.link}>{props.text}</Link>
    </div>

)
}

export default function DefaultNav() {
return (
            <nav id="nav-header" className='flex flex-nowrap bg-emerald-900 text-white py-4 justify-center'>
            {navs.map(item => <NavItem key={item.text} link={item.link} text={item.text}/>)}
            </nav>
    )
}