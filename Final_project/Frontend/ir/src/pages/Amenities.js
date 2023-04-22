import React, { useState } from 'react'
import Navbar from '../components/Navbar'
import '../styles/City.css'
import { Link,useLocation } from 'react-router-dom'
import Footer from '../components/Footer'
const City = (props) => {
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
                <div className='sidebaroptions '>
                    Budget
                </div>
                <div className='sidebaroptions active'>
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
                    <span>Rs {propsdata.budget} per day</span>
                </div>
                <div className='oneline'>
                    <h1 className='title'>What amenities you want ?</h1>
                    <div className=''>

                        <select value={Select} onChange={e=>{setSelect(e.target.value)}}>
                            <option value="None">Choose from the list </option>
                            <option value="breakfast ,lunch ,wifi , smoking room ,free pickup, free drop">breakfast ,lunch ,wifi , smoking room ,free pickup, free drop</option>
                            <option value="breakfast , lunch , free pickup,">breakfast , lunch , free pickup,</option>
                            <option value="breakfast , lunchRs">breakfast , lunchRs </option>
                            <option value="Breakfast "> Breakfast </option>
    
                        </select>

                    </div>
                    <Link to="/hotels/rating" state={{...propsdata, ...{amenities:Select}}}>submit</Link>

                </div>
                
                

            </div>
        </div>
       <Footer></Footer>
    </div>
  )
}

export default City