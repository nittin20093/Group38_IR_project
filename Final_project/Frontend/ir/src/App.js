import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import React, { useEffect } from "react";
import './App.css';


import HomePage from './pages/HomePage';
import City from "./pages/City";
import Budget from "./pages/Budget"
import Amenities from './pages/Amenities'
import Rating from './pages/Rating'
import Photos from './pages/Photos'
import Hotels from './pages/Hotels'
import Enjoy from './pages/Enjoy'
import Hotels1 from './pages/Hotels1'
import Hotels2 from './pages/Hotels2'
import Hotels3 from './pages/Hotels3'

const App = props => {
  
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/hotels/city" element={<City />} />
        <Route path="/hotels/budget" element={<Budget />} />
        <Route path="/hotels/amenities" element={<Amenities />} />
        <Route path="/hotels/rating" element={<Rating />} />-
        <Route path="/hotels/photos" element={<Photos />} />
        <Route path="/hotels/hotels" element={<Hotels />} />
        <Route path="/hotels/hotels1" element={<Hotels1 />} />
        <Route path="/hotels/hotels2" element={<Hotels2 />} />
        <Route path="/hotels/enjoy" element={<Enjoy />} />
      </Routes>
    </div>
  );

}



export default App;
