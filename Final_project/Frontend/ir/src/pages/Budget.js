import React, { useState } from 'react'

import Navbar from '../components/Navbar'
import '../styles/City.css'
import { Link, useLocation } from 'react-router-dom'
import Footer from '../components/Footer'
import Select from 'react-select'
const options = [
    { value: {min:0, max:1000}, label: 'under Rs 1000 per day' },
    { value: {min:1000, max:2500}, label: 'Rs 1000 - Rs 2500 per day' },
    { value: {min:2500, max:5000}, label: 'Rs 2500 - Rs 5000 per day' },
    { value: {min:5000, max:10000}, label: 'Rs 5000 - Rs 10000 per day' },
    { value: {min:10000, max:100000}, label: 'Rs 10000 - above per day ' },
]
const styles = {
    menuList: (provided, state) => ({
        ...provided,
        paddingTop: 0,
        paddingBottom: 0,
    })
};

const City = (props) => {
    const location = useLocation();
    const propsdata = location.state;
    console.log(propsdata)
    const [Selects, setSelects] = useState({ value: "" });
    const handlechange = (selectedoption) => {
        setSelects(selectedoption.value)
    }


    return (
        <div className='citypage'>
            <Navbar></Navbar>
            <div className='hero'>
                <div className='sidebar1'>
                    <div className='sidebar'>
                        <div className=' main'>
                            PROCEDURE
                        </div>
                        <div className='sidebaroptions '>
                            <Link to="/hotels/city" style={{ textDecoration: 'none', color: 'Black' }}>Select The City</Link>
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
                        <span className='previnfoheading'>City - <span className='previnfovalue'>{propsdata.city}</span></span>
                    </div>
                    <div className='oneline'>
                        <h1 className='sidebar2title'>What is your budget ?</h1>
                        <div className='selectwithbtn'>
                            <div className='selectamen'>
                                <Select
                                    defaultValue={[]}
                                    onChange={handlechange}
                                    name="colors"
                                    options={options}
                                    className=""
                                    classNamePrefix="select"
                                    styles={styles}
                                />
                            </div>
                            <Link to="/hotels/amenities" state={{ city: propsdata.city, budget: Selects }}><button class="btn btn-success">SUBMIT</button></Link>
                        </div>
                        {/* <div>
                        <select value={Select} onChange={e=>setSelect(e.target.value)}>
                            <option value="None">Choose from the list </option>
                            <option value="under 1000">under Rs 1000 per day</option>
                            <option value="1000-2500">Rs 1000 - Rs 2500 per day</option>
                            <option value="2500-5000">Rs 2500 - Rs 5000 per day</option>
                            <option value="5000-10000">Rs 5000 - Rs 10000 per day</option>
                            <option value="above 10000">Rs 10000- above per day</option>
                        </select>
                        
                    </div> */}

                    </div>



                </div>
            </div>
            <Footer></Footer>
        </div>
    )
}

export default City