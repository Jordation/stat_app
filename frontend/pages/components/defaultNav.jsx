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
    <div className='basis-1/4 nav-item w-24 h-12 text-center'>
        <Link className='text-center' href={props.link}>{props.text}</Link>
    </div>

)
}

export default function DefaultNav() {
return (    <div className='flex text-white py-4 justify-evenly'>
            {navs.map(item => <NavItem key={item.text} link={item.link} text={item.text}/>)}
            </div>
    )
}