import React from 'react'
import Formsidebar from '../components/Formsidebar'
import Navbar from '../components/Navbar'
import '../styles/City.css'
import { Link } from 'react-router-dom'
const City = () => {
  return (
    <div className='citypage'>
        <Navbar></Navbar>
        <div className='hero'>
            <div className='sidebar1'>
                <Formsidebar></Formsidebar>
            </div>
            <div className='sidebar2'>
                <h1 className='title'>Select the city you want to visit ?</h1>
                <div className='select'>
                    <div className='card'>
                        <Link to={'/hotels/budget'} state={{'city':'Delhi'}}>
                            <img src="https://www.holidify.com/images/bgImages/DELHI.jpg" alt=""/>
                            <span>Delhi</span>
                        </Link>
                    </div>
                    <div className='card'>
                        <Link to={'/hotels/budget'} state={{'city':'Bangalore'}}>
                            <img src="https://www.holidify.com/images/bgImages/DELHI.jpg" alt=""/>
                            <span>Bangalore</span>
                        </Link>

                    </div>
                    <div className='card'>
                        <Link to={'/hotels/budget'} state={{'city':'Goa'}}>   
                            <img src="https://www.holidify.com/images/bgImages/DELHI.jpg" alt=""/>
                            <span>Goa</span>
                        </Link>

                    </div>
                    
                </div>
                

            </div>
        </div>
       
    </div>
  )
}

export default City