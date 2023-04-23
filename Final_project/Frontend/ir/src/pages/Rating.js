import { useState } from 'react'
import React from 'react'

import Navbar from '../components/Navbar'
import '../styles/City.css'
import { Link, useLocation } from 'react-router-dom'
import Footer from '../components/Footer'
import Select from 'react-select'

const options = [
    { value: '5', label: 'Min. 5 rating' },
    { value: '4', label: 'Min. 4 rating' },
    { value: '3', label: 'Min. 3 rating' },
    { value: '2', label: 'Min. 2 rating' },
    { value: '1', label: 'Min. 1 rating' },

]

const styles = {
    menuList: (provided, state) => ({
        ...provided,
        paddingTop: 0,
        paddingBottom: 0,
    })
};



const City = () => {
    const location = useLocation();
    const propsdata = location.state;
    const [Selects, setSelects] = useState();
    console.log(propsdata)
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
                        <span className='previnfoheading'>City - <span className='previnfovalue'>{propsdata.city}</span></span>
                        <span className='previnfoheading'>Budget - <span className='previnfovalue'>{propsdata.budget.min} - {propsdata.budget.max}  </span></span>
                        <span className='previnfoheading'>Amenities - <span className='previnfovalue'>{propsdata.amenities.map(items => { return (<span>{items}, </span>) })}</span></span>

                        <span></span>
                    </div>
                    <div className='oneline'>
                        <h1 className='sidebar2title'>What is the Minimum rating of the hotel you want ?</h1>
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
                            <Link to="/hotels/photos" state={{ ...propsdata, ...{ rating: Selects } }}>submit</Link>
                        </div>
                        {/* <div className=''>
                        <select value={Select} onChange={e=>{setSelect(e.target.value)}}>
                            <option value="None">Choose from the list </option>
                            <option value="5"> 5 rating</option>
                            <option value="4-5">4-5 rating</option>
                            <option value="3-4">3-4 rating </option>
                            <option value="2-3">2-3 rating</option>
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