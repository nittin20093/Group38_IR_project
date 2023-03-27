
import React,{ useState,useEffect } from 'react';

import { Link } from "react-router-dom";
import '../styles/Navbar.css'



const Navbar = props => {
    return(
       <div className='hero'>
        <div className="navbar">
            
            <Link to="/"><div className='logo1'>Travel . io</div></Link>
            
            <div className="navbar-item">
                <Link to="/"className="home">Home</Link>
                <Link className="products" to='/product'>Products</Link>
                <div className="products">Categories</div>
                <div className="products">Brands</div>
                <div className="products">Pricing</div> 
            </div>

           
                
          
        </div>
       </div>
        

)}

  
export default Navbar;
