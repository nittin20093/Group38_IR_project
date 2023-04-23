import React from 'react'

import Navbar from '../components/Navbar'
import '../styles/City.css'
import { useLocation } from 'react-router-dom'
import { Link } from 'react-router-dom'
import axios from 'axios'
import { useEffect } from 'react'

import Footer from '../components/Footer'




const City = () => {
    const location = useLocation();
    const propsdata = location.state;
    console.log(propsdata)
    const getdata =  async()=>{
        try{
            const data = await axios.post('http://192.168.53.147:5000/similarity', {
                ...propsdata
            })
            console.log(data)
        } catch (error) {
            console.log(error)
        }
    }
    useEffect(() => {
        getdata()
    }, [])



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
                            Enjoy!
                        </div>
                    </div>

                </div>
                <div className='sidebar2'>
                    <h1 className='title'>Select some of the photos</h1>
                    <div className='select'>
                        photos
                    </div>



                </div>
            </div>
            <Footer></Footer>
        </div>
    )
}

export default City