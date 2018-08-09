import React, { Component } from 'react';

import NavBar from '../../navbar/navbar';
import Procedure from './procedure';
import Policy from './policy';
import Appeal from './appeal';
import AdmissionForm from './form';
import ModelTest from './modeltest';
import GRSFooter from '../../footer/footer';
import './admission.css';

class Admission extends Component {
  render () {
    return (
      <div>
        <NavBar />
          <div className="notice-board">
            <a href="tel:1618015560310">161-801-5560-310</a>
            <h4>
              Notice Board Service
            </h4>
          </div>
        <div className="admission-main">
          <div className="admission-bg" /><br />
          <div id="procedure"><Procedure /></div>
          <div id="policy"><Policy /></div>
          <div id="appeal"><Appeal /></div>
          <div className="row">
            <div className="col-md-6">
              <div id="admission-form"><AdmissionForm /></div>
            </div>
            <div className="col-md-6">
              <div id="modeltest"><ModelTest /></div>
            </div>
          </div>
          <GRSFooter />
        </div>
      </div>
    )
  }
}

export default Admission;
