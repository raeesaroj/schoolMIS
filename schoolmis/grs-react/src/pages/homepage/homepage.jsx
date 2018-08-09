import React, { Component } from 'react';
import swal from 'sweetalert2';

import NavBar from '../../navbar/navbar';
import SliderHome from './slider';
import RaisedDiv from './raised-div';
import GRSFooter from '../../footer/footer';
import './homepage.css';
import Logo from '../../assets/grs-logo1.png';

class Home extends Component {

  componentDidMount() {
    swal({
      showConfirmButton: false,
      title: 'Admission Open',
      html: '<div class="appeal-main">' +
              '<div class="row">' +
                  '<p class="swalbtn-p">Multiple Intelligence (MI) & Neuro Linguistic Programming (NLP) based school announces Admission Open for Grade I – IX</p>' +
                  '<p class="swalbtn-p">Forms available from school office on all working days from 9.00 am to 4.00 pm</p>' +
                  '<p class="swalbtn-p"><a href="/admission#admission-form"><button class="swal-btn">Download Form</button></a></p>' +
              '</div>' +
            '</div>',
      imageUrl: Logo,
      imageHeight: 150,
      showCloseButton: true,
      focusCloseButton: false,
      allowEnterKey: false,
      padding: '25px',
      width: '50%',
    });
  }

  render() {
    return (
      <div className="homepage-main">
        <NavBar />
        <div className="notice-board">
          <a href="tel:1618015560310">161-801-5560-310</a>
          <h4>
            Notice Board Service
          </h4>
        </div>
        <SliderHome />
        <RaisedDiv />
        <GRSFooter />
      </div>
    );
  }
}

export default Home;
