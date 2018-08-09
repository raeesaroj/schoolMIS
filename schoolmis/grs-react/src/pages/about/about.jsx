import React, { Component } from 'react';

import NavBar from '../../navbar/navbar';
import History from './history';
import Mission from './mission';
import Methodology from './methodology';
import GRSFooter from '../../footer/footer';

import './about.css';

class About extends Component {
  render() {
    return(
      <div>
        <NavBar />
          <div className="notice-board">
            <a href="tel:1618015560310">161-801-5560-310</a>
            <h4>
              Notice Board Service
            </h4>
          </div>
        <div className="about-main">
          <div className="about-bg" />
          <div id="history"><History /></div>
          <div id="mission"><Mission /></div>
          <div id="methodology"><Methodology /></div>
        </div>
        <GRSFooter />
      </div>
    )
  }
}

export default About;
