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
                <div className='sidebar'>
                <div className='sidebaroptions '>
                    Select The City
                </div>
                <div className='sidebaroptions '>
                    Budget
                </div>
                <div className='sidebaroptions '>
                    Amenities
                </div>
                <div className='sidebaroptions '>
                    Minimum Rating
                </div>
                <div className='sidebaroptions active'>
                    Select Some Photos
                </div>
                <div className='sidebaroptions'>
                    Select hotels
                </div>
                <div className='sidebaroptions'>
                    Enjoy
                </div>
             </div>

            </div>
            <div className='sidebar2'>
                <h1 className='title'>Select some of the photos</h1>
                    <div className='select'>
                        <div className='card'>
                            <img src="https://images.unsplash.com/photo-1512918580421-b2feee3b85a6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8aG90ZWxzJTIwcm9vbXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60" alt=""/>
                        </div>
                        <div className='card'>
                            <img src="https://images.unsplash.com/photo-1512918580421-b2feee3b85a6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8aG90ZWxzJTIwcm9vbXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60" alt=""/>
                        </div> <div className='card'>
                            <img src="https://images.unsplash.com/photo-1512918580421-b2feee3b85a6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8aG90ZWxzJTIwcm9vbXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60" alt=""/>
                        </div> <div className='card'>
                            <img src="https://images.unsplash.com/photo-1512918580421-b2feee3b85a6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8aG90ZWxzJTIwcm9vbXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60" alt=""/>
                        </div> <div className='card'>
                            <img src="https://images.unsplash.com/photo-1512918580421-b2feee3b85a6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8aG90ZWxzJTIwcm9vbXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60" alt=""/>
                        </div> <div className='card'>
                            <img src="https://images.unsplash.com/photo-1512918580421-b2feee3b85a6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8aG90ZWxzJTIwcm9vbXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60" alt=""/>
                        </div> 
                    </div>
                    
                

            </div>
        </div>
       
    </div>
  )
}

export default City