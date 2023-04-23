
import Footer from '../components/Footer'
import React, { useEffect, useState } from 'react'
import Navbar from '../components/Navbar'
import '../styles/City.css'
import { Link, useLocation } from 'react-router-dom'
import axios from 'axios'

const City = () => {
    const [data_rec , setData_rec] = useState({});
    const [photos_list , setphotos_list] = useState([1]);
    const location = useLocation();
    const propsdata = location.state;
    console.log(propsdata)
    const getdata =  async()=>{
        try{
            const datas = await axios.post('http://127.0.0.1:5000/get_hotel_links', {
                ...propsdata
            })
            const str_datas = JSON.stringify(datas.data.similar_images_indexes);
            console.log(str_datas)
            const myString = str_datas.replace(/[\[\]']+/g,'').split(',');
            console.log(myString)
            setphotos_list(myString);
            // console.log(data)
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
                <div className='sidebaroptions '>
                    Select hotels
                </div>
                <div className='sidebaroptions active'>
                    Enjoy
                </div>
             </div>
            </div>
            <div className='sidebar2'>
                <h1 className='title'>Enjoy </h1>
                <div className='enjoy'>
                    {propsdata.indexes.map((items, index) =>{
                        return (
                            <>
                            <div>
                                <div onClick={()=>{window.location(photos_list[index])}}>
                                    <div className={" somephotocard "} key={index} >
                                        <img src={require('../assets/images/'+ propsdata.city+'/'+ items + '.jpg')} alt=""></img>
                                    
                                </div><a href={photos_list[index]}>{photos_list[index]}</a></div>
                                
                               {items}
                            </div>
                           
                            </>
                        )
                    })}
                    
                    
                </div>
                

            </div>
        </div>
       <Footer></Footer>
    </div>
  )
}

export default City