import React from 'react'
import Formsidebar from '../components/Formsidebar'
import Navbar from '../components/Navbar'
import '../styles/City.css'
import { Link } from 'react-router-dom'
import Footer from '../components/Footer'
const City = () => {
  return (
    <div className='citypage'>
        <Navbar></Navbar>
        <div className='hero'>
            <div className='sidebar1'>
                <Formsidebar></Formsidebar>
            </div>
            <div className='sidebar2'>
                <h1 className='sidebar2title'>Select the city you want to visit ?</h1>
                <div className='cityselect'>
                    <div className='cardcity'>
                        <Link to={'/hotels/budget'} style={{ textDecoration: 'none', color:'Black' }}state={{'city':'Delhi'}}>
                            <img src="https://www.holidify.com/images/bgImages/DELHI.jpg" alt=""/>
                            <span style={{ fontSize: '1.3rem',}}>Delhi</span>
                        </Link>
                    </div>
                    <div className='cardcity'>
                        <Link to={'/hotels/budget'}style={{ textDecoration: 'none', color:'Black' }} state={{'city':'Bangalore'}}>
                            <img src="https://www.holidify.com/images/bgImages/DELHI.jpg" alt=""/>
                            <span style={{ fontSize: '1.3rem',}}>Bangalore</span>
                        </Link>

                    </div>
                    <div className='cardcity'>
                        <Link to={'/hotels/budget'}style={{ textDecoration: 'none', color:'Black' }} state={{'city':'Goa'}}>   
                            <img src="https://www.holidify.com/images/bgImages/DELHI.jpg" alt=""/>
                            <span style={{ fontSize: '1.3rem',}}>Goa</span>
                        </Link>

                    </div>
                    
                </div>
                

            </div>
        </div>
       <Footer></Footer>
    </div>
  )
}

export default City