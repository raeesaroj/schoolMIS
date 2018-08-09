import React, { Component } from 'react';
import { Carousel } from 'react-bootstrap';

import './testimonial.css';
import Rajesh from '../../assets/rajesh.JPG';
import Sharad from '../../assets/sharad.JPG';
import Shiva from '../../assets/shiva.JPG';
import Vidhya from '../../assets/vidhya.JPG';

class Testimonial extends Component {
  render() {
    return (
      <div className="testimonial-main">
        <h2 className="testimonial-head">
          Parents Word About GRS
        </h2>
        <Carousel>
          <Carousel.Item>
            <div className='row carousel-row'>
              <div className='col-md-4'>
                <img
                  src={Shiva}
                  id="carousel-img"
                  width="300px"
                  height="300px"
                  alt="Shiva Shrestha" />
              </div>
              <div className='col-md-8'>
                <blockquote>
                  Om Sai ! My elder son Shakti Shrestha studied in St. Xaviers Godawari under the care of Mr. Joseph Niraula who was the principal at that time. GRS has adopted Xavier Education System which emphasizes on Academic Excellence and Character Formation. I am very happy that I admitted my son Sai Sunder Shrestha in GRS. In a very short time he has improved in studies as well as in character and behavior. GRS gives personal care and attention to students. All the best to GRS!
                </blockquote>
                <cite className='carousel-cite'>
                  &#8212; Shiva Shrestha
                </cite>
              </div>
            </div>
          </Carousel.Item>
          <Carousel.Item>
            <div className='row carousel-row'>
              <div className='col-md-4'>
                <img
                  src={Vidhya}
                  id="carousel-img"
                  width="300px"
                  height="300px"
                  alt="Vidhya Khanal (Gyawali)" />
              </div>
              <div className='col-md-8'>
                <blockquote>
                  My husband and I decided to admit my son in GRS when we knew that Mr. Josh Niraula is the principal. My husband had attended one of his international training programs and he was very impressed by his thoughts and ideas. Besides, GRS is under Xavier Education System which we believe will help my son to acquire the best education and solid character formation.
                </blockquote>
                <cite className='carousel-cite'>
                  &#8212; Vidhya Khanal (Gyawali)
                </cite>
              </div>
            </div>
          </Carousel.Item>
          <Carousel.Item>
            <div className='row carousel-row'>
              <div className='col-md-4'>
                <img
                  src={Rajesh}
                  id="carousel-img"
                  width="300px"
                  height="300px"
                  alt="Rajesh Nakarmi" />
              </div>
              <div className='col-md-8'>
                <blockquote>
                  I started my school in St. Xaviers Godawari and the environment of Godawari is always in my heart. Since the principal Mr. Josh Niraula and some teachers are from SXG, I believe that they will inculcate Xavier Education values in my son. My son Suryansh now takes interest in studies and as the school captain, he has learned the leadership qualities. I am happy that my son is getting what I got. I wish GRS success!
                </blockquote>
                <cite className='carousel-cite'>
                  &#8212; Rajesh Nakarmi
                </cite>
              </div>
            </div>
          </Carousel.Item>
          <Carousel.Item>
            <div className='row carousel-row'>
              <div className='col-md-4'>
                <img
                  src={Sharad}
                  id="carousel-img"
                  width="300px"
                  height="300px"
                  alt="Sharad Rana Magar" />
              </div>
              <div className='col-md-8'>
                <blockquote>
                  Despite its early challenges GRS has proved that it is committed to provide modern quality education. My son Digvijay is happy and is always eager to go to school. For me this proves that the school takes proper care of students. Happy students means happy school. Besides, my son has improved a lot in language and numerical knowledge and skills. My good wishes to GRS!
                </blockquote>
                <cite className='carousel-cite'>
                  &#8212; Sharad Rana Magar
                </cite>
              </div>
            </div>
          </Carousel.Item>
        </Carousel>
      </div>
    );
  }
}

export default Testimonial;
