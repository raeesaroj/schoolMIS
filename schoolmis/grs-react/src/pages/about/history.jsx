import React, { Component } from 'react';
import ScrollAnimation from 'react-animate-on-scroll';

import './history.css';
import HistoryImg from '../../assets/2.jpg';

class History extends Component {
  render() {
    return(
      <div className="history-main">
        <div className="row">
          <div className="col-md-6">
            <ScrollAnimation animateIn="fadeInLeft" animateOut="fadeOutLeft">
            <div className="history-section">
              <h1 className="history-head">History</h1>
              <h4 className="history-des">MANAGED BY XAVIER EDUCATION SYSTEM (GRS): a modern and unique school. Spread over 12 ropanies of verdant land in Badegaun Godavari, GRS is managed under the aegis of Xavier Education System Pvt. Ltd and led by me, a former Principal of St. Xavier’s School, Godavari and a team of committed staff and managed by a strong professional management team. School Motto: Love God – Serve Nation (Rising the Next Generation) VISION: To become a Premier Residential School that facilitates conducive learning environment for students who are determined to meet the challenges posed by the increasing pace of scientific, economic and social advancements of the 21st century.</h4>
            </div>
          </ScrollAnimation>
          </div>
          <div className="col-md-6">
            <ScrollAnimation animateIn="fadeInRight" animateOut="fadeOutRight">
            <p className="history-img"><img src={HistoryImg} alt="history" /></p>
            </ScrollAnimation>
          </div>
        </div>
            </div>
    )
  }
}

export default History;
