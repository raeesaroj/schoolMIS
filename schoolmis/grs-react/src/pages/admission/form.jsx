import React, { Component } from 'react';
import { Icon } from 'react-materialize';
import ScrollAnimation from 'react-animate-on-scroll';

import './form.css';
import DownloadImg from '../../assets/1.JPG';

class AdmissionForm extends Component {
  render () {
    return (
      <div className="form-main">
        <h1 className="form-head">Admission Form</h1>
        <p className="form-des">Download the Admission Form here</p>
        <ScrollAnimation animateIn="fadeInUp" offset={50}>
          <p className="form-des">
            <a href={DownloadImg} download="GRS Admission Form">
              <button className="form-download">
                <Icon>file_download</Icon>
              </button>
            </a>
          </p>
        </ScrollAnimation>
      </div>
    )
  }
}

export default AdmissionForm;
