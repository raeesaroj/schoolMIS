import React, { Component } from 'react';
import { Button } from 'react-materialize';
import swal from 'sweetalert2';

import Principal from '../../assets/principal.png';
import './welcome.css';

export default class Welcome extends Component {

  handleClick(){
    swal({
      showConfirmButton: false,
      title: 'Message from the Principal',
      html: '<h1 className="appeal-head">Welcome To GRS</h1>' +
            '<p style="color: #000; text-align: justify; width: 90%; margin: auto; padding-top: 30px;">It is my great pleasure to welcome you to Godawari Residential School (GRS) managed by Xavier Education System. In a short span of just one year the school has earned a good reputation as a modern and progressive school. <br /></p>' +
            '<p style="color: #000; text-align: justify; width: 90%; margin: auto;">In my long career as an educator, first as the Principal of St. Xaviers School Godawari, and later as the founder Principal of Campion Academy and College, I have always encouraged students to harness their God given talents. For this very reason, GRS has adopted teaching - learning methodology based on some of the most recent and progressive mind sharpening systems: Multiple Intelligence (MI), Neuro Linguistic Programing (NLP), and Mind Mapping. I myself, a NLP certified trainer, take special interest to teach students various mind and body techniques which they can apply to produce outstanding results in whatever they do. To make learning more interactive and to appeal to techno-savvy new generation, each classroom is equipped with a Smart Board connected with Internet.<br /></p>' +
            '<p style="color: #000; text-align: justify; width: 90%; margin: auto;">Though rigorous scholastic programs are part of GRS culture, we strive to develop and nurture the different facets of a child. For this the school encourages students to participate in a variety of co-curricular activities: Music, dance, drama, art and various games and sports. Social work and environmental conservation activities are also integral part of GRS.<br /></p>' +
            '<p style="color: #000; text-align: justify; width: 90%; margin: auto;">Inspired by our motto "Love God - Serve Nation" we aim not to just impart knowledge to the students, but also to inculcate in them - inquiring minds, compassionate hearts and a humanitarian spirit. We encourage collaboration not competition. We want each teacher and student to be a partner in each ones progress. Our mission is to produce smart, self-disciplined, conscientious, and confident citizens of Nepal who will excel in the areas of their choice and make parents, teachers and country proud.<br /><br /></p>' +
            '<p style="text-align:left; color: #000; margin-bottom: 0; font-size: 16px; width: 90%; margin: auto;">Principal</p>' +
            '<p style="text-align:left; color: orange; font-size: 20px; width: 90%; margin: auto;">Joseph B Niraula</p>',
      showCloseButton: true,
      imageUrl: Principal,
      backdrop: `blur(5px)`,
      imageHeight: 150,
      focusCloseButton: false,
      allowEnterKey: false,
      padding: '25px',
      customClass: 'message-principal',
      width: '70%',
    });
  }

  render() {
    return(
      <div className="welcome-main">
        <div className="row">
          <div className="col-sm-4">
            <div className="principal-pic">
              <img
                src={Principal}
                alt="Principal"
                title="Principal"
                className="principal-pic-1" />
            </div>
          </div>
          <div className="col-sm-8">
            <h2 className="welcome-head-1">
              Welcome to GRS
            </h2>
            <h2 className="welcome-head-2">
              (Godawari Residential School)
            </h2>
            <p className="welcome-orange">
              The function of education is to teach one to think intensively and to think critically. Intelligence plus character - that is the goal of true education. (Martin Luther King, Jr.)
            </p>
            <br />
            <Button waves='light' className="see-more" onClick={this.handleClick.bind(this)}>Read More</Button>
          </div>
        </div>

        {// <p className="welcome-p">
        //   It is my great pleasure to welcome you to Godawari Residential School (GRS) managed by Xavier Education System. In a short span of just one year the school has earned a good reputation as a modern and progressive school.
        // </p>
        // <br />
        // <p className="welcome-p">
        //   In my long career as an educator, first as the Principal of St. Xavier's School Godawari, and
        //   later as the founder Principal of Campion Academy and College, I have always encouraged
        //   students to harness their God given talents. For this very reason, GRS has adopted teaching
        //   - learning methodology based on some of the most recent and progressive mind sharpening
        //   systems: Multiple Intelligence (MI), Neuro Linguistic Programing (NLP), and Mind Mapping.
        //   I myself, a NLP certified trainer, take special interest to teach students various mind and
        //   body techniques which they can apply to produce outstanding results in whatever they
        //   do. To make learning more interactive and to appeal to techno-savvy new generation, each
        //   classroom is equipped with a Smart Board connected with Internet.<br />
        // <p className="welcome-p">
        //   Though rigorous scholastic programs are part of GRS culture, we strive to develop and
        //   nurture the different facets of a child. For this the school encourages students to participate
        //   in a variety of co-curricular activities: Music, dance, drama, art and various games and
        //   sports. Social work and environmental conservation activities are also integral part of GRS.
        // </p>
        // <br />
        // <p className="welcome-p">
        //   Inspired by our motto 'Love God - Serve Nation' we aim not to just impart knowledge to
        //   the students, but also to inculcate in them - inquiring minds, compassionate hearts and a
        //   humanitarian spirit. We encourage collaboration not competition. We want each teacher
        //   and student to be a partner in each one's progress. Our mission is to produce smart, self-
        //   disciplined, conscientious, and confident citizens of Nepal who will excel in the areas of
        //   their choice and make parents, teachers and country proud.
        // </p>
        // <br />
        // <p style={{ marginLeft: '7.5%', color: '#000', marginBottom: '0', fontSize: '16px' }}>Principal</p>
        // <p style={{ marginLeft: '7.4%', color: 'orange', fontSize: '20px' }}>
        //   Joseph B Niraula
        // </p>
        }
        <br />
        <br />
        {
          //<iframe src="http://saralnepali.com/widgets/nepali-calendar.php" frameborder="0" scrolling="no" marginwidth="0" marginheight="0" style={{ border:'none', overflow:'hidden', width:'100%', height:'1200px' }} allowtransparency="true"></iframe>
        }
      </div>
    )
  }
}
