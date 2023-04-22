import React from 'react'
import Navbar from '../components/Navbar'
import Footer from "../components/Footer"
import "../styles/HomePage.css"
// import { Link } from 'react-router-dom'

// Deep blue (#001233), light coral red (#FF595A), beige (#CAC0B3)
const HomePage = () => {
    return (
        <div className='homepage'>
            <Navbar></Navbar>
            <div className='hero'>
                <div className='sidepage1'>
                    <div className='photocontainer'>
                        <div className='photo'>
                            HOTELS ?
                        </div>
                    </div>
                    
                </div>
                <div className='loginpage'>
                    <div className='login_box'>
                        <div className='heading-login'>
                            Login
                        </div>
                        <form>
                            <div class="input">
                                <label for="name">Email / Username</label>
                                <input type="text" name="name" id="name"/>
                                <span class="spin"></span>
                            </div>

                            <div class="input">
                                <label for="pass">Password</label>
                                <input type="password" name="pass" id="pass"/>
                                <span class="spin"></span>
                            </div>
                        </form>
                        <div className='or'>
                            OR
                        </div>
                        <div className='buttons'>
                            <div className='google'>
                                <img alt="signinwithgoogle" src="https://img.icons8.com/color/16/000000/google-logo.png"/>
                                Sign In With Google
                            </div>
                            <div className='facebook'>
                                <img alt="signinwithfacebook" src="https://www.facebook.com/images/fb_icon_325x325.png" />
                                Sign In With Facebook
                            </div>
                        </div>
                        
                    </div>
                    
                </div>   
            </div>
            <Footer></Footer>
        </div>
        
      );
    
}

export default HomePage
