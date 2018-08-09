import React, { Component } from 'react';
import { Input, Button } from 'react-materialize';

import './getintouch.css';

class GetInTouch extends Component {
  render() {
    return(
      <div className="getintouch-main">
        <div className="row">
          <div className="col-md-8">
            <h1 className="getintouch-head">Get in Touch</h1>
            <Input className="getintouch-input" label="Name*" validate />
            <Input className="getintouch-input" type="email" label="Email*" validate />
            <Input className="getintouch-input" type="textarea" label="Message*" validate />
            <Button waves='light' className="contact-us-btn">SUBMIT</Button>
          </div>
          <div className="col-md-4">
            <h3 className="getintouch-subhead">Connect with us:</h3>
            <p className="getintouch-p">For support or any questions:</p>
            <p className="getintouch-p">Call us: <a href="callto:015560310">+977-01-5560310</a></p>
            <p className="getintouch-p">Email us at <a href="mailto:info@grs.edu.np">info@grs.edu.np</a></p>
            <h3 className="getintouch-subhead">Godawari Residential School GRS</h3>
            <p className="getintouch-p">Godawari 10, Lalitpur</p>
            <p className="getintouch-p">Nepal</p>
          </div>
        </div>
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d10868.749908914204!2d85.35728161853312!3d27.615356835435605!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39eb199dccead41d%3A0x1b365aa5ea2f78fb!2sGodawari+Residential+School!5e0!3m2!1sen!2snp!4v1521045113033" title="GRS Map" width="100%" height="450" frameBorder="0" style={{ border: '0', paddingTop: '50px' }} allowFullScreen></iframe>
      </div>
    )
  }
}

export default GetInTouch;
