import React, { Component } from 'react';
import ScrollAnimation from 'react-animate-on-scroll';

import './mission.css';
import MissionImg from '../../assets/3.JPG';
import VisionImg from '../../assets/3.JPG';

class Mission extends Component {
  render() {
    return(
      <div className="mission-vision">
        <div className="row">
          <div className="col-md-6">
            <ScrollAnimation animateIn="fadeInLeft" animateOut="fadeOutLeft">
            <p className="mission-img"><img src={MissionImg} alt="Mission" /></p>
            </ScrollAnimation>
          </div>
          <div className="col-md-6">
            <ScrollAnimation animateIn="fadeInRight" animateOut="fadeOutRight">
            <div className="mission-main">
              <div className="mission-card">
                <h1 className="mission-head">Mission</h1>
                <h4 className="mission-des">We the members of GRS, inspired by Xavier Education System and its Motto: Love
                  God - Serve Nation aspire to impart world class education and encourage students
                  to harness their God given talents, channel them to restructure their future to become
                  self-confident, self-disciplined and self-reliant citizens through the love of God and
                  service to the Nation within a safe, secure and friendly environment of Xavier Education System.
                </h4>
              </div>
            </div>
            </ScrollAnimation>
          </div>
          <div className="col-md-6">
            <ScrollAnimation animateIn="fadeInLeft" animateOut="fadeOutLeft">
            <div className="vision-main">
              <div className="mission-card">
                <h1 className="mission-head">Vision</h1>
                <h4 className="mission-des">To become a Premier Residential School that facilitates conducive
                  learning environment for students who are determined to meet the
                  challenges posed by the increasing pace of scientific, economic and
                  social advancements of the 21st century.
                </h4>
              </div>
            </div>
            </ScrollAnimation>
          </div>
          <div className="col-md-6">
            <ScrollAnimation animateIn="fadeInRight" animateOut="fadeOutRight">
            <p className="mission-img"><img src={VisionImg} alt="Vision" /></p>
            </ScrollAnimation>
          </div>
        </div>
      </div>
    )
  }
}

export default Mission;
