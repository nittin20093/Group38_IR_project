import React from 'react'
import Formsidebar from '../components/Formsidebar'
import Navbar from '../components/Navbar'
import '../styles/City.css'

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
                        <img src="https://www.holidify.com/images/bgImages/DELHI.jpg" alt=""/>
                        <span>DELHI</span>
                    </div>
                    <div className='card'>
                        <img src="https://www.holidify.com/images/bgImages/DELHI.jpg" alt=""/>
                        <span>DELHI</span>
                    </div>
                    <div className='card'>
                        <img src="https://www.holidify.com/images/bgImages/DELHI.jpg" alt=""/>
                        <span>DELHI</span>
                    </div>
                    <div className='card'>
                        <img src="https://www.holidify.com/images/bgImages/DELHI.jpg" alt=""/>
                        <span>DELHI</span>
                    </div>
                    <div className='card'>
                        <img src="https://www.holidify.com/images/bgImages/DELHI.jpg" alt=""/>
                        <span>DELHI</span>
                    </div>
                </div>
                

            </div>
        </div>
       
    </div>
  )
}

export default City