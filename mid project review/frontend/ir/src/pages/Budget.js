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
                <div className='sidebaroptions active'>
                    Budget
                </div>
                <div className='sidebaroptions'>
                    Amenities
                </div>
                <div className='sidebaroptions'>
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
                </div>
                <div className='oneline'>
                    <h1 className='title'>What is your budget ?</h1>
                    <div>

                        <select>
                        <option value="fruit">under Rs 1000 per day</option>
                        <option value="vegetable">Rs 1000 - Rs 2500 per day</option>
                        <option value="meat">Rs 2500 - Rs 5000 per day</option>
                        <option value="meat">Rs 5000 - Rs 10000 per day</option>
                        <option value="meat">Rs 10000- above per day</option>
                        </select>

                    </div>
                </div>
                
                

            </div>
        </div>
       
    </div>
  )
}

export default City