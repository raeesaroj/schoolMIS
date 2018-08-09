import React, { Component } from 'react';
import { Slider, Slide } from 'react-materialize';

import SlideA from '../../assets/assembly.png';
import SlideB from '../../assets/futsal.png';
import SlideC from '../../assets/canteen.png';
import SlideD from '../../assets/medical.png';
import SlideE from '../../assets/games.png';
import './slider.css';

class SliderHome extends Component {
  render() {
    return (
      <div className="slider-main">
        <Slider indicators={false} fullscreen={false} >
          <Slide
            src={SlideA}>
            Assembly
          </Slide>
          <Slide
            src={SlideB}>
            Futsal Match
          </Slide>
          <Slide
            src={SlideC}>
            Fresh Canteen Meal
          </Slide>
          <Slide
            src={SlideD}>
            Infirmary Department
          </Slide>
          <Slide
            src={SlideE}>
            Games and Extra Carriculum Activities
          </Slide>
        </Slider>
      </div>
    );
  }
}

export default SliderHome;
