import React, { Component } from 'react';

import NavBar from '../../navbar/navbar';
import GRSFooter from '../../footer/footer';
import GetInTouch from './getintouch';
import './contact.css';

class Contact extends Component {
  render() {
    return(
      <div>
        <NavBar />
        <div className="contact-main">
          <div className="contact-bg">
            <h2 className="contact-head">
              We love to hear from you, and value your Feedback
            </h2>
          </div>
          <GetInTouch />
        </div>
        <GRSFooter />
      </div>
    )
  }
}

export default Contact;
