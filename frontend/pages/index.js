
import DefaultHead from './components/defaultHead'
import DefaultNav from './components/defaultNav'
export default function BasePage() {
    return (
        <div>
        <DefaultHead />
          <div id="wrapper">
              <DefaultNav />
              <div id="site-cols">
                  <div id="l"> </div>
                  <div id="c">
                  <div/>
                  </div>
                  <div id="r"> </div>
              </div>
          </div>
        </div>
    )
}
