import React, { useState } from 'react'

import Navbar from '../components/Navbar'
import '../styles/City.css'
import { Link } from 'react-router-dom'

const City = () => {
    const photos = [1, 2, 3, 4, 5, 6, 7]
    const [selectedPhotos, setSelectPhotos] = useState([]);
    const handleOnClick = (index) => {
        const conditon = selectedPhotos.indexOf(index)
        if (conditon !== -1) {
            const data = selectedPhotos.filter((value) => value !== index)
            setSelectPhotos(data)
        } else {
            setSelectPhotos([...selectedPhotos, ...[index]])
        }


    }
    const handlestyle = (index) => {
        const conditon = selectedPhotos.indexOf(index)
        if (conditon !== -1) {
            return true
        } else {
            return false
        }
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
                        {photos.map((item, index) => {
                            return (
                                <div className={handlestyle(index) ? "activephoto card" : " card "} key={index} onClick={() => handleOnClick(index)}>
                                    <img src={require('../assets/images/' + item + '.png')} alt="" />
                                    <span>SGB Hotel, 3 star, Delhi </span>
                                </div>
                            )
                        })}


                    </div>


                </div>
            </div>

        </div>
    )
}

export default City