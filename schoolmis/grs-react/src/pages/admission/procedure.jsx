import React, { Component } from 'react';
import ScrollAnimation from 'react-animate-on-scroll';

import './procedure.css';

class Procedure extends Component {
  render() {
    return(
      <div className="procedure-main">
        <h1 className="procedure-head">GRS Follows the Following Admission Procedure:</h1>
        <div className="row">
          <div className="col-md-4">
            <ScrollAnimation animateIn="fadeInUp">
            <div className="procedure-section">
              <h3 className="procedure-sub-head">All application forms must be duely completed & accompanied by:</h3>
              <p className="procedure-p">Recent original or certified copy of the end-of-academic year report.</p>
              <p className="procedure-p">A certified copy of the applicant's birth certificate</p>
              <p className="procedure-p">Child's Photos ( 3 copies of latest 2'' x 2'' ID picture )</p>
            </div>
            </ScrollAnimation>
          </div>
          <div className="col-md-4">
            <ScrollAnimation animateIn="fadeInUp" delay={250}>
            <div className="procedure-section">
              <h3 className="procedure-sub-head">Important:</h3>
              <p className="procedure-p">Beginning of Enrollment period : 1st of Chaitra (March - 15 - 2018)</p>
              <p className="procedure-p">Deadline of submission of requirements : 29th  Baishakha (May 11- 2018 )</p>
              <p className="procedure-p">Entrance Test and Interview Schedule : 1st of Chaitra (March 15 2018 onwards )</p>
              <p className="procedure-p">Deadline for Enrollment period : Not later than 29th  Baishakha (May 11- 2018)</p>
            </div>
            </ScrollAnimation>
          </div>
          <div className="col-md-4">
            <ScrollAnimation animateIn="fadeInUp" delay={500}>
            <div className="procedure-section">
              <h3 className="procedure-sub-head">Entrance Exam & Results:</h3>
              <p className="procedure-p">Subjects of the entrance exam – Nepali, English, Math & Science.</p>
              <p className="procedure-p">Entrance Exam & Interview of the Child.</p>
              <p className="procedure-p">Parents Interview.</p>
              <p className="procedure-p">Entrance Exam result: if selected, shall be notified by school administration.</p>
            </div>
            </ScrollAnimation>
          </div>
        </div>
      </div>
    )
  }
}

export default Procedure;
