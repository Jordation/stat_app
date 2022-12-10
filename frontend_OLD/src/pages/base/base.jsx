import {
    Link,

} from "react-router-dom";

export default function BasePage() {
    return (
        <div id="wrapper">
            <header id="nav-header">
                <nav id="nav-header-inner">
                    <div className="nav-item">
                        Custom Graphs
                        <Link to={`custom`}>
                            <div>
                                its a box
                            </div>
                        </Link>
                    </div>
                </nav>
            </header>
            <div id="site-cols">
                <div id="l"> </div>
                <div id="c"> </div>
                <div id="r"> </div>
            </div>
        </div>
    )
}