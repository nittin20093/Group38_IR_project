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
                <div className='sidebaroptions active'>
                    Minimum Rating
                </div>
                <div className='sidebaroptions '>
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
                <div className='Previnfo'>
                    <span>DELHI</span>
                    <span>Rs 1000 - Rs 2000 per day</span>
                </div>
                <div className='oneline'>
                    <h1 className='title'>What is the Minimum rating you want ?</h1>
                    <div className=''>
                        <select>
                        <option value="fruit"> 5 rating</option>
                        <option value="vegetable">4-5 rating</option>
                        <option value="meat">3-4 rating </option>
                        <option value="meat">2-3 rating</option>
                        </select>

                    </div>
                </div>
                
                

            </div>
        </div>
       
    </div>
  )
}

export default City