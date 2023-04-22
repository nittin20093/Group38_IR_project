import React, { useState } from 'react'

import Navbar from '../components/Navbar'
import '../styles/City.css'
import { Link,useLocation } from 'react-router-dom'
import Footer from '../components/Footer'

const City = (props) => {
    const location = useLocation();
    const propsdata = location.state;
    console.log(propsdata)
    const [Select,setSelect] = useState();

  
   
  return (
    <div className='citypage'>
        <Navbar></Navbar>
        <div className='hero'>
            <div className='sidebar1'>
                <div className='sidebar'>
                <div className='sidebaroptions '>
                    <Link to="/hotels/city">Select The City</Link>
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
                    <span>{propsdata.city}</span>
                </div>
                <div className='oneline'>
                    <h1 className='title'>What is your budget ?</h1>
                    <div>
                        <select value={Select} onChange={e=>setSelect(e.target.value)}>
                            <option value="None">Choose from the list </option>
                            <option value="under 1000">under Rs 1000 per day</option>
                            <option value="1000-2500">Rs 1000 - Rs 2500 per day</option>
                            <option value="2500-5000">Rs 2500 - Rs 5000 per day</option>
                            <option value="5000-10000">Rs 5000 - Rs 10000 per day</option>
                            <option value="above 10000">Rs 10000- above per day</option>
                        </select>
                        
                    </div>
                    <Link to="/hotels/amenities" state={{city:propsdata.city, budget:Select}}>submit</Link>
                </div>
                
                

            </div>
        </div>
       <Footer></Footer>
    </div>
  )
}

export default City