import React, { Component } from 'react';
import { Button } from 'react-materialize';
import ScrollAnimation from 'react-animate-on-scroll';

import './appeal.css';
import GRSLogo from '../../assets/grs-logo1.png';

class Appeal extends Component {
  render() {
    return(
      <div className="appeal-main">
        <h1 className="appeal-head">Admission Appeal</h1>
        <div className="row">
          <div className="col-md-4">
            <p className="appeal-logo"><img src={GRSLogo} alt="GRS Logo" /></p>
          </div>
          <div className="col-md-8">
            <p className="appeal-p">Multiple Intelligence (MI) & Neuro Linguistic Programming (NLP) based school announces Admission Open for Grade I – IX</p>
            <p className="appeal-p">Forms available from school office on all working days from 9.00 am to 4.00 pm</p>
            <ScrollAnimation animateIn="fadeInRight" offset={50}><p className="appeal-p"><a href="/contact"><Button className="appeal-btn" waves='light'>Contact Us</Button></a></p></ScrollAnimation>
          </div>
        </div>
      </div>
    )
  }
}

export default Appeal;
