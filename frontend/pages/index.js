
import Head from 'next/head'
import Link from 'next/link'

export default function BasePage() {
    return (
        <div>
          <Head>
            <title>VLR-Buddy Stat Tools</title>
            <meta name="description" content="analysis-tool" />
            <link rel="icon" href="/firing_gun.ico" />
          </Head>
          <div id="wrapper">
              <header id="nav-header">
                  <nav id="nav-header-inner">
                      <div className="nav-item">
                          <Link href="/custom">
                              <div>
                                  Custom Graphs
                              </div>
                          </Link>
                      </div>
                      <div className="nav-item">
                          <Link href="/flexbox">
                              <div>
                                  Playground
                              </div>
                          </Link>
                      </div>
                  </nav>
              </header>
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
