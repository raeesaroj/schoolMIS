import React, { Component } from 'react';

import './raised-div.css';
import Welcome from './welcome';
import Philosophy from './philosophy';
import Testimonial from './testimonial';
import Article from './article';

class RaisedDiv extends Component {
  render() {
    return (
      <div className="raised-div">
        <Welcome />
        <Philosophy />
        <Article />
        <Testimonial />
      </div>
    );
  }
}

export default RaisedDiv;
