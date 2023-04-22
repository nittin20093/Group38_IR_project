import "../styles/Footer.css"
import { Link } from "react-router-dom";

const Footer = () => {
  return (
    <div className="footer">
      <div className="frame-parent">
        <div className="bachira-parent">
          <b className="bachira">
          <Link to="/"><div className='logo'>Travelio</div></Link>
          </b>
          <div className="bachira-is-an-container">
            <p className="bachira-is-an">
              Travelio is an online hostel recomender system
            </p>
            <p className="bachira-is-an">
              travelio provide cheap, high quality, products to
            </p>
            <p className="customers">customers</p>
          </div>
        </div>
        <div className="for-beginner-parent">
          <b className="for-beginner">For Beginner</b>
          <div className="about-parent">
            <div className="about">About</div>
            <div className="about">Career</div>
            <div className="about">Promotion</div>
          </div>
        </div>
        <div className="for-beginner-parent">
          <b className="for-beginner">Overview</b>
          <div className="about-parent">
            <div className="about">Product</div>
            <div className="about">Categories</div>
            <div className="about">Pricing</div>
          </div>
        </div>
        <div className="for-beginner-parent">
          <b className="for-beginner">Explore Us</b>
          <div className="about-parent">
            <div className="about">Our Career</div>
            <div className="about">Privacy</div>
            <div className="about">{`Terms & Conditions`}</div>
          </div>
        </div>
        <div className="for-beginner-parent">
          <b className="for-beginner">Connect Us</b>
          <div className="about-parent">
            <div className="about">support@travelio.com</div>
            <div className="about">021 - 555 -456</div>
            <div className="about">Sudirman, South Jakarta</div>
          </div>
        </div>
      </div>
      <div className="copyright-2023">
        Copyright 2023 • All Rights Reserved Bachira by Giatinaja
      </div>
    </div>
    );
};

export default Footer;
