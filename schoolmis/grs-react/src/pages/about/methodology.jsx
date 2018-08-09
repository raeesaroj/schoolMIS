import React, { Component } from 'react';
import ScrollAnimation from 'react-animate-on-scroll';

import './methodology.css';
import Method1 from '../../assets/light.svg';
import Method2 from '../../assets/medical.svg';
import Method3 from '../../assets/mindmap.png';
import Method4 from '../../assets/neurology.svg';

class Methodology extends Component {

  constructor(props) {
    super(props);
    this.state = {
      isHidden1: true,
      isHidden2: true,
      isHidden3: true,
      isHidden4: true,
    }
    this.showHide1 = this.showHide1.bind(this);
    this.showHide2 = this.showHide2.bind(this);
    this.showHide3 = this.showHide3.bind(this);
    this.showHide4 = this.showHide4.bind(this);
  }

  showHide1() {
    this.setState({ isHidden1: !this.state.isHidden1 });
  }

  showHide2() {
    this.setState({ isHidden2: !this.state.isHidden2 });
  }

  showHide3() {
    this.setState({ isHidden3: !this.state.isHidden3 });
  }

  showHide4() {
    this.setState({ isHidden4: !this.state.isHidden4 });
  }

  render() {
    let classHide1 = this.state.isHidden1 ? "hide-div" : "show-div";
    let classHide2 = this.state.isHidden2 ? "hide-div" : "show-div";
    let classHide3 = this.state.isHidden3 ? "hide-div" : "show-div";
    let classHide4 = this.state.isHidden4 ? "hide-div" : "show-div";

    return(
      <div className="methodology-main">
        <h1 className="methodology-head">
          Teaching Methodology
        </h1>
        <h4 className="methodology-des">
          GRS uses Accelerated Learning Methodology using the following modern tools and
          techniques:
          <div className="row">
            <div className="col-lg-6 col-md-6">
              <ScrollAnimation animateIn="fadeInUp">
                <img
                  className="methodology-img"
                  src={Method1}
                  alt="Methodology" onClick={this.showHide1} />
                <h1 className="method-head" onClick={this.showHide1}>
                Smart Class
              </h1>
              <p className={"method-p " + classHide1}>
                All classrooms have smart boards and audio-visual facilities so that
                students have access to the state of art learning technology.
              </p>
              </ScrollAnimation>
            </div>
            <div className="col-lg-6 col-md-6">
              <ScrollAnimation animateIn="fadeInUp">
                <img
                  className="methodology-img"
                  src={Method2}
                  alt="Methodology" onClick={this.showHide2} />
                <h1 className="method-head" onClick={this.showHide2}>
                (NLP) Neuro Linguistic Programing
              </h1>
              <p className={"method-p " + classHide2}>
                First time in Nepal NLP is made integral part
                of education in GRS. The school Principal Joseph B Niraula is the first Nepali to be
                certified as NLP trainer. NLP uses sensory based teaching/learning techniques to
                model excellence and help students make success a habit in all their endeavours.
              </p>
              </ScrollAnimation>
            </div>
            <div className="col-lg-6 col-md-6">
              <ScrollAnimation animateIn="fadeInUp">
                <img
                  className="methodology-img"
                  src={Method3}
                  alt="Methodology" onClick={this.showHide3} />
                <h1 className="method-head" onClick={this.showHide3}>
                Multiple Intelligence
              </h1>
              <p className={"method-p " + classHide3}>
                In the beginning of school each child is scientifically tested
                using the modern Dermatoglyphics Test and closely supervised during the year.
                Howard Gardner the father of MI has proved that each child has a unique blend of
                intelligences. Hence each child should be allowed to learn using his/her natural talent.
              </p>
              </ScrollAnimation>
            </div>
            <div className="col-lg-6 col-md-6">
              <ScrollAnimation animateIn="fadeInUp">
                <img
                  className="methodology-img"
                  src={Method4}
                  alt="Methodology" onClick={this.showHide4} />
                <h1 className="method-head" onClick={this.showHide4}>
                Mind Mapping
              </h1>
              <p className={"method-p " + classHide4}>
                A powerful graphic technique which provides a universal key to
                unlock the potential of the brain. It is used to generate, visualize, structure and classify
                ideas, and as an aid to studying and organizing information, solving problems, making
                decisions.
              </p>
              </ScrollAnimation>
            </div>
          </div>
        </h4>
      </div>
    )
  }
}

export default Methodology;
