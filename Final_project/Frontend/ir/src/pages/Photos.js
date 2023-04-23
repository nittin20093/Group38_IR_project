import React, { useState } from 'react'

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
    const [selectedPhotos, setSelectPhotos] = useState([]);
    const handleOnClick = (index) => {
        const conditon = selectedPhotos.indexOf(index)
        if (conditon !== -1) {
            const data = selectedPhotos.filter((value) => value !== index)
            setSelectPhotos(data)
        } else {
            setSelectPhotos([...selectedPhotos, ...[index]])
        }
        console.log(selectedPhotos)


    }
    const handlestyle = (index) => {
        const conditon = selectedPhotos.indexOf(index)
        if (conditon !== -1) {
            return true
        } else {
            return false
        }
    }
    const datafetched = {
        "data": {
            "similar_images_indexes": [
                0,
                157,
                619,
                2,4,6,7,9,0,
                157,
                619,
                2,4,6,7,9,0,
                157,
                619,
                2,4,6,7,9,0,
                157,
                619,
                2,4,6,7,9,0,
                157,
                619,
                2,4,6,7,9,0,
                157,
                619,
                2,4,6,7,9,0,
                157,
                619,
                2,4,6,7,9,0,
                157,
                619,
                2,4,6,7,9,0
            ]
        },
        "status": 200,
        "statusText": "OK",
        "headers": {
            "content-length": "39",
            "content-type": "application/json"
        },
        "config": {
            "transitional": {
                "silentJSONParsing": true,
                "forcedJSONParsing": true,
                "clarifyTimeoutError": false
            },
            "adapter": [
                "xhr",
                "http"
            ],
            "transformRequest": [
                null
            ],
            "transformResponse": [
                null
            ],
            "timeout": 0,
            "xsrfCookieName": "XSRF-TOKEN",
            "xsrfHeaderName": "X-XSRF-TOKEN",
            "maxContentLength": -1,
            "maxBodyLength": -1,
            "env": {},
            "headers": {
                "Accept": "application/json, text/plain, /",
                "Content-Type": "application/json"
            },
            "method": "post",
            "url": "http://192.168.53.147:5000/similarity",
            "data": "{\"city\":\"Delhi\",\"budget\":\"2500-5000\",\"amenities\":[\"Mountain view\"],\"rating\":\"4\"}"
        },
        "request": {}
    }
    const photos = datafetched.data.similar_images_indexes
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
                    <h1 className='sidebar2title'>Select some of the photos</h1>
                    <div className='selectsomephotos'>
                        {photos.map((item, index) => {
                                return (
                                    <div className={handlestyle(item) ? "activesomephoto somephotocard" : " somephotocard "} key={index} onClick={() => handleOnClick(item)}>
                                        <img src={require('../assets/images/'+ propsdata.city+'/'+ item + '.jpg')} alt=""></img>
                                    </div>
                                )
                        })}
                    </div>
                    <Link to="/hotels/hotels" state={{ ...propsdata, ...{photos:selectedPhotos}}}><button class="btn btn-success">SUBMIT</button></Link>



                </div>
            </div>
            <Footer></Footer>
        </div>
    )
}

export default City