
import React from 'react';

import { Link } from "react-router-dom";
import '../styles/Navbar.css'



const Navbar = props => {
    return(
        <div className="navbar"> 
            <div className='logo'>
                <Link to="/" style={{ textDecoration: 'none', color:'Black'  }}><span className='Logo'>TRAVEL.<spam className="io">io</spam></span></Link>
            </div>
            <div className="navbar-item">
                <Link to="/"className="home">Home</Link>
                <Link className="products" to='/product'>Products</Link>
                <div className="products">Categories</div>
                <div className="products">Brands</div>
                <div className="products">Pricing</div> 
            </div>

           
                
          
        </div>
   
        

)}

  
export default Navbar;
