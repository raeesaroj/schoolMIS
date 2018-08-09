import React, { Component } from 'react';
import ScrollAnimation from 'react-animate-on-scroll';
import { Icon } from 'react-materialize';

import './modeltest.css';
import DownloadImg from '../../assets/1.JPG';

class ModelTest extends Component {
  render () {
    return (
      <div className="modeltest-main">
        <h1 className="modeltest-head">Model Test</h1>
        <p className="modeltest-des">Download the Model Test Form here</p>
        <ScrollAnimation animateIn="fadeInUp" offset={50}>
        <p className="modeltest-des"><a href={DownloadImg} download="Model Test"><button className="modeltest-download"><Icon>file_download</Icon></button></a></p>
        </ScrollAnimation>
      </div>
    )
  }
}

export default ModelTest;
