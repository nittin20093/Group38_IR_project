import React, { useState } from 'react'
import Navbar from '../components/Navbar'
import '../styles/City.css'
import { Link, useLocation } from 'react-router-dom'
import Footer from '../components/Footer'
import Select from 'react-select'


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
    const [Selects, setSelects] = useState();
    console.log(propsdata)
    const handlechange = (selectedoption) => {
        const data = selectedoption.map(items => items.value)
        setSelects(data)
    }
    
    const delhi = ['Lever handle on door', 'Detached', 'Mountain view', 'Visual alarm', 'Private pool', 'Free laundry service', 'Smartphone device', 'BBQ facilities', 'Separate living room', 'Bathtub', 'Pets allowed in room', 'Video game console', 'sofa', 'Free bottled water', 'Linens', 'Desk', 'Telephone', 'Closet', 'Fan', 'Shower', 'Towels', 'Toiletries', 'Free Wi-Fi', 'TV', 'Air conditioning']
    const goa = ['Private beach access', 'Scale', 'Electric blanket', 'DVD/CD player', 'Separate shower/bathtub', 'Complimentary tea', 'Whirlpool bathtub', 'Smartphone device', 'Washing machine', 'Street view', 'Shoeshine kit', 'Bathroom phone', 'Work desk', 'Satellite/cable channels', 'Complimentary bottled water', 'Balcony/terrace', 'Linens', 'Closet', 'Shower', 'Towels', 'Fan', 'Toiletries', 'Free Wi-Fi in all rooms!', 'Free Wi-Fi', 'Air conditioning']
    const bangalore = ['Pool view', 'Separate living room', 'Board games', 'Books/DVDs/music for children', 'Additional bathroom', 'Whirlpool bathtub', 'Board games/puzzles', 'Shower chair', 'Carbon monoxide detector', 'Dishwasher', 'Street view', 'iPod docking station', 'Clothes rack', 'Free bottled water', 'Linens', 'Desk', 'Telephone', 'Satellite/cable channels', 'Fan', 'Shower', 'Closet', 'Towels', 'Toiletries', 'Free Wi-Fi', 'Air conditioning']
    
    const options = []
    if(propsdata.city === "Delhi"){
        delhi.forEach((items)=>(
            options.push({value:items, label:items}))
        )
    }
    if(propsdata.city === "Goa"){
        goa.forEach((items)=>(
            options.push({value:items, label:items}))
        )
    }
    
    if(propsdata.city === "Bangalore"){
        bangalore.forEach((items)=>(
            options.push({value:items, label:items}))
        )
    }
    
    // if (propsdata.city == "goa"){
    //     goa.map(item =>{
    //         optiondata.append({value:item})
    //     }) 
    // }
    // if (propsdata.city == "bangalore"){
    //     bangalore.map(item =>{
    //         optiondata.append({value:item})
    //     }) 
    // }


    
    // [
    //     { value: 'pickup', label: 'pickup' },
    //     { value: 'drop', label: 'drop' },
    //     { value: 'breakfast', label: 'breakfast' },
    //     { value: 'lunch', label: 'lunch' },
    //     { value: 'smoking room', label: 'smoking room' },
    // ]

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
                            <Link to="/hotels/city" style={{ textDecoration: 'none', color:'Black' }}>Select The City</Link>
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
                        <span className='previnfoheading'>City - <span className='previnfovalue'>{propsdata.city}</span></span>
                        <span className='previnfoheading'>Budget - <span className='previnfovalue'>{propsdata.budget}</span></span>
                    </div>
                    <div className='oneline'>
                        <h1 className='sidebar2title'>What amenities you want ?</h1>
                        <div className='selectwithbtn'>
                            <div className='selectamen'>
                                <Select
                                    defaultValue={[]}
                                    onChange={handlechange}
                                    isMulti
                                    name="colors"
                                    options={options}
                                    className=""
                                    classNamePrefix="select"
                                    styles={styles}
                                />
                            </div>
                            <Link to="/hotels/rating" state={{ ...propsdata, ...{ amenities: Selects } }}><button class="btn btn-success">SUBMIT</button></Link>
                        </div>


                    </div>



                </div>
            </div>
            <Footer></Footer>
        </div>
    )
}

export default City