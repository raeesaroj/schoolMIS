import React, { Component } from 'react';
import { Icon } from 'react-materialize';
import ScrollAnimation from 'react-animate-on-scroll';

import './policy.css';

class Policy extends Component {
  render () {
    return (
      <div className="policy-main">
        <div className="policy-width">
          <h1 className="policy-head">School Admission Policy Statement</h1>
          <h4 className="policy-des">Godawari Residential School exists to offer Multiple Intelligence (MI) & Neuro Linguistic Programming (NLP) based education in a calming environment of Godawari, Lalitpur.  Students will, be carefully selected and will do DMI test upon acceptance in order to know the natural potentiality of the student.  GRS is dedicated to the teaching of human values, & the practical education based on student's energy & interest. The School Board determines the policies of the school. Student, parents, and staff are expected to cooperate fully with the school policies as mentioned below.</h4>
          <h4 className="policy-des">Acceptance of a student will be based on school records, a personal interview with parents and student, testing results, and/or recommendations concerning character, attitude, general promise, and holistic development.</h4>

          <h1 className="policy-head">Admission Policy</h1>
          <h4 className="policy-des">We at GRS know that a successful school experience occurs when parents give evidence of being:</h4><br /><br />
          <div className="row">
            <div className="col-md-3">
              <ScrollAnimation animateIn="fadeInUp" offset={50}>
              <div className="policy-col">
                <p className="policy-icon"><Icon>school</Icon></p>
                <p className="policy-col-des">supportive of the School</p>
              </div>
              </ScrollAnimation>
            </div>
            <div className="col-md-3">
              <ScrollAnimation animateIn="fadeInUp" delay={250} offset={50}>
              <div className="policy-col">
                <p className="policy-icon"><Icon>build</Icon></p>
                <p className="policy-col-des">desirous of a strong academic program</p>
              </div>
              </ScrollAnimation>
            </div>
            <div className="col-md-3">
              <ScrollAnimation animateIn="fadeInUp" delay={500} offset={50}>
              <div className="policy-col">
                <p className="policy-icon"><Icon>check_circle</Icon></p>
                <p className="policy-col-des">supportive of the child taking responsibility for his/her behavior, self-management and learning</p>
              </div>
              </ScrollAnimation>
            </div>
            <div className="col-md-3">
              <ScrollAnimation animateIn="fadeInUp" delay={750} offset={50}>
              <div className="policy-col">
                <p className="policy-icon"><Icon>event_seat</Icon></p>
                <p className="policy-col-des">committed to the programs and activities that support the school</p>
              </div>
              </ScrollAnimation>
            </div>
          </div>
        </div>
      </div>
    )
  }
}

export default Policy;
