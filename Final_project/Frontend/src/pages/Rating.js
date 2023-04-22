import { useState } from 'react'
import React from 'react'

import Navbar from '../components/Navbar'
import '../styles/City.css'
import { Link, useLocation } from 'react-router-dom'
import Footer from '../components/Footer'
const City = () => {
    const location = useLocation();
    const propsdata = location.state;
    const [Select,setSelect] = useState();
    console.log(propsdata)
  return (
    <div className='citypage'>
        <Navbar></Navbar>
        <div className='hero'>
            <div className='sidebar1'>
                <div className='sidebar'>
                <div className='sidebaroptions '>
                    <Link to="/hotels/city">Select The City</Link>
                </div>
                <div className='sidebaroptions'>
                    Budget
                </div>
                <div className='sidebaroptions'>
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
                    <span>{propsdata.city}</span>
                    <span>Rs {propsdata.budget} per day</span>
                    <span>{propsdata.amenities}</span>
                </div>
                <div className='oneline'>
                    <h1 className='title'>What is the Minimum rating you want ?</h1>
                    <div className=''>
                        <select value={Select} onChange={e=>{setSelect(e.target.value)}}>
                            <option value="None">Choose from the list </option>
                            <option value="5"> 5 rating</option>
                            <option value="4-5">4-5 rating</option>
                            <option value="3-4">3-4 rating </option>
                            <option value="2-3">2-3 rating</option>
                        </select>

                    </div>
                    <Link to="/hotels/photos" state={{...propsdata, ...{rating:Select}}}>submit</Link>

                </div>
                
                

            </div>
        </div>
        <Footer></Footer>
       
    </div>
  )
}

export default City