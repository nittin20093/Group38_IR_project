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
            const datas = await axios.post('http://127.0.0.1:5000/similarity', {
                ...propsdata
            })
            const str_datas = JSON.stringify(datas.data.similar_images_indexes);
            console.log(str_datas)
            const myString = str_datas.replace(/[\[\]']+/g,'').split(',').map(Number);
            setphotos_list(myString);
            // console.log(data)
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


    }
    const handlestyle = (index) => {
        const conditon = selectedPhotos.indexOf(index)
        if (conditon !== -1) {
            return true
        } else {
            return false
        }
    }
    const handleprops = ()=>{
        propsdata.selectedPhotos = selectedPhotos
        return {...propsdata}
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
                    <h1 className='sidebar2title'>Select the hotel </h1>
                    <div className='selectsomephotos'>
                        {photos_list.map((item, index) => {
                            if(isNaN(item)){
                                return (<></>)
                            }
                            else
                            return (
                                <div className={handlestyle(index) ? "activesomephoto somephotocard" : " somephotocard "} key={index} onClick={() => handleOnClick(index)}>
                                    <img src={require('../assets/images/'+ propsdata.city+'/'+ item + '.jpg')} alt=""></img>
                                   
                                </div>
                            )
                        })}


                    </div>
                    <Link to="/hotels/hotels" state={() => handleprops()}><button class="btn btn-success">SUBMIT</button></Link>
                    

                </div>
            </div>

        </div>
    )
}

export default City