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
            const data = await axios.post('http://192.168.53.147:5001/ranked_with_filter', {
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
    const datafetched ={
        "data": {
            "ranked_filtered_idxs": "[561, 196, 390, 425, 44, 534, 474, 420, 85, 155, 313, 394, 517, 139, 144, 266, 149, 377, 468, 289, 314, 95, 288, 429, 355, 38, 98, 202, 242, 450, 305, 304, 22, 80, 328, 122, 223, 366, 107, 379, 382, 496, 150, 408, 218, 225, 239, 346, 414, 400, 167, 127, 62, 421, 51, 283, 180, 73, 50, 343, 290, 213, 118, 181, 113, 263, 161, 153, 301, 197, 235, 64, 92, 622, 273, 19, 83, 135, 42, 418, 11, 216, 16, 9, 252, 211, 40, 349, 131, 30, 158, 519, 260, 641, 286, 36, 78, 255, 321, 35, 12, 120, 257, 178, 27, 163, 147, 431, 17, 352, 93, 103, 94, 236, 356, 70, 445, 143, 222, 448, 563, 164, 451, 170, 87, 595, 582, 175, 327, 176, 89, 597, 182, 475, 316, 90, 599, 59, 332, 546, 101, 340, 241, 422, 391, 386, 344, 84, 278, 151, 237, 554, 339, 303, 401, 280, 556, 55, 219, 478, 351, 159]"
        },
        "status": 200,
        "statusText": "OK",
        "headers": {
            "content-length": "801",
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
            "url": "http://192.168.53.147:5001/ranked_with_filter",
            "data": "{\"city\":\"Delhi\",\"budget\":{\"min\":2500,\"max\":5000},\"amenities\":[],\"rating\":\"3\"}"
        },
        "request": {}
    }
    const photos = datafetched.data.ranked_filtered_idxs.replace(/[\[\]']+/g,'').split(',').map(Number);
    console.log(datafetched.data.ranked_filtered_idxs.replace(/[\[\]']+/g,'').split(',').map(Number))
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