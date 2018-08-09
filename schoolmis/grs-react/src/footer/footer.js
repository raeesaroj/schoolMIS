import React, { Component } from 'react';
import { Icon } from 'antd';
import { Footer } from 'react-materialize';

import './footer.css';

class GRSFooter extends Component {
  render() {
    return (
      <div className="footer-main">
        <Footer copyrights={  <p className="footer-des">© Copyright 2018. Designed & built with&nbsp;<span className="footer-love"><Icon type="heart" /></span>&nbsp;by <a href="https://bitsinnovation.com/" target="_blank" rel="noopener noreferrer" className="bits-link">BitsInnovation</a></p>}
          links={
            <ul>
              <li><a className="grey-text text-lighten-3" href="/">Home</a></li>
              <li><a className="grey-text text-lighten-3" href="/about">About</a></li>
              <li><a className="grey-text text-lighten-3" href="/admission">Admission</a></li>
              <li><a className="grey-text text-lighten-3" href="/contact">Contact</a></li>
            </ul>
          }
          className='example'
        >
            <h5 className="white-text">Godawari Residential School</h5>
            <p className="grey-text text-lighten-4">(GRS)</p>
        </Footer>
      </div>
    );
  }
}

export default GRSFooter;
