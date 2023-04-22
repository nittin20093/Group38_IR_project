import React from 'react'

import Navbar from '../components/Navbar'
import '../styles/City.css'
import { Link } from 'react-router-dom'

const City = () => {
  return (
    <div className='citypage'>
        <Navbar></Navbar>
        <div className='hero'>
            <div className='sidebar1'>
            <div className='sidebar'>
                <div className='sidebaroptions '>
                    <Link to="/hotels/city">Select The City</Link>
                </div>
                <div className='sidebaroptions '>
                    Budget
                </div>
                <div className='sidebaroptions '>
                    Amenities
                </div>
                <div className='sidebaroptions'>
                    Minimum Rating
                </div>
                <div className='sidebaroptions '>
                    Select Some Photos
                </div>
                <div className='sidebaroptions active'>
                    Select hotels
                </div>
                <div className='sidebaroptions'>
                    Enjoy
                </div>
             </div>
            </div>
            <div className='sidebar2'>
                <h1 className='title'>Select the hotel </h1>
                <div className='select'>
                    <div className='card'>
                        <img src="https://images.unsplash.com/photo-1625255052242-7b27595fc76f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTh8fGhvdGVscyUyMHJvb218ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60" alt=""/>
                        <span>SGB Hotel, 3 star, Delhi </span>
                    </div>
                    <div className='card'>
                        <img src="https://images.unsplash.com/photo-1625255052242-7b27595fc76f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTh8fGhvdGVscyUyMHJvb218ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60" alt=""/>
                        <span>SGB Hotel, 3 star, Delhi </span>
                    </div>
                    <div className='card'>
                        <img src="https://images.unsplash.com/photo-1625255052242-7b27595fc76f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTh8fGhvdGVscyUyMHJvb218ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60" alt=""/>
                        <span>SGB Hotel, 3 star, Delhi </span>
                    </div>
                    <div className='card'>
                        <img src="https://images.unsplash.com/photo-1625255052242-7b27595fc76f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTh8fGhvdGVscyUyMHJvb218ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60" alt=""/>
                        <span>SGB Hotel, 3 star, Delhi </span>
                    </div>
                    <div className='card'>
                        <img src="https://images.unsplash.com/photo-1625255052242-7b27595fc76f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTh8fGhvdGVscyUyMHJvb218ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60" alt=""/>
                        <span>SGB Hotel, 3 star, Delhi </span>
                    </div>
                    <div className='card'>
                        <img src="https://images.unsplash.com/photo-1625255052242-7b27595fc76f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTh8fGhvdGVscyUyMHJvb218ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60" alt=""/>
                        <span>SGB Hotel, 3 star, Delhi </span>
                    </div>
                    
                </div>
                

            </div>
        </div>
       
    </div>
  )
}

export default City