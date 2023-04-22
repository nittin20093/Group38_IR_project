import React from 'react'
import { Link } from 'react-router-dom'


const Formsidebar = (props) => {
  return (
        <div className='sidebar'>
            <div className='sidebaroptions active'>
                <Link to="/hotels/city">Select The City</Link>
            </div>
            <div className='sidebaroptions '>
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
                Select Hotels
            </div>
            <div className='sidebaroptions'>
                Enjoy
            </div>
        </div>

  )
}

export default Formsidebar