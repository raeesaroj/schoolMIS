import React, { Component } from 'react';
import { Navbar, NavItem } from 'react-materialize';
import { Menu, Dropdown, Icon } from 'antd';
import { NavLink } from 'react-router-dom';
import { HashLink } from 'react-router-hash-link';

import './navbar.css';
import GRSlogo from '../assets/grs-logo1.png';

const SubMenu = Menu.SubMenu;

const aboutUs = (
  <Menu>
    <Menu.Item>
      <HashLink to="/about#history">History</HashLink>
    </Menu.Item>
    <Menu.Item>
      <HashLink to="/about#mission">Mission & Vision</HashLink>
    </Menu.Item>
    <Menu.Item>
      <HashLink to="/about#methodology">Methodology</HashLink>
    </Menu.Item>
    <Menu.Item>
      <HashLink to="/about#">Spacious Greenary Environment</HashLink>
    </Menu.Item>
    <Menu.Item>
      <HashLink to="/about#">Newsletter</HashLink>
    </Menu.Item>
  </Menu>
);

const admissions = (
  <Menu>
    <Menu.Item>
      <HashLink to="/admission#procedure">Procedure</HashLink>
    </Menu.Item>
    <Menu.Item>
      <HashLink to="/admission#policy">Policy</HashLink>
    </Menu.Item>
    <Menu.Item>
      <HashLink to="/admission#appeal">Appeal</HashLink>
    </Menu.Item>
    <Menu.Item>
      <HashLink to="/admission#admission-form">Admission Form</HashLink>
    </Menu.Item>
    <Menu.Item>
      <HashLink to="/admission#modeltest">Model Test</HashLink>
    </Menu.Item>
    <Menu.Item>
      <HashLink to="/admission#">Class Time</HashLink>
    </Menu.Item>
    <Menu.Item>
      <HashLink to="/admission#">Uniform</HashLink>
    </Menu.Item>
  </Menu>
);

const programs = (
  <Menu>
    <Menu.Item>
      <HashLink to="#">Curriculum</HashLink>
    </Menu.Item>
    <Menu.Item>
      <HashLink to="#">High Schools</HashLink>
    </Menu.Item>
    <SubMenu title="ECA">
      <Menu.Item>
        <HashLink to="#">Music</HashLink>
      </Menu.Item>
      <Menu.Item>
        <HashLink to="#">Drama</HashLink>
      </Menu.Item>
      <Menu.Item>
        <HashLink to="#">Art</HashLink>
      </Menu.Item>
      <Menu.Item>
        <HashLink to="#">Dance</HashLink>
      </Menu.Item>
    </SubMenu>
    <Menu.Item>
      <HashLink to="#">Abacus</HashLink>
    </Menu.Item>
    <Menu.Item>
      <HashLink to="#">MI Lab</HashLink>
    </Menu.Item>
  </Menu>
);

const facitities = (
  <Menu>
    <Menu.Item>
      <HashLink to="#">E-ClassRoom</HashLink>
    </Menu.Item>
    <Menu.Item>
      <HashLink to="#">Science Lab</HashLink>
    </Menu.Item>
    <Menu.Item>
      <HashLink to="#">Computer Lab</HashLink>
    </Menu.Item>
    <Menu.Item>
      <HashLink to="#">Library</HashLink>
    </Menu.Item>
    <Menu.Item>
      <HashLink to="#">Sports</HashLink>
    </Menu.Item>
    <Menu.Item>
      <HashLink to="#">Transportations</HashLink>
    </Menu.Item>
    <Menu.Item>
      <HashLink to="#">School Meals</HashLink>
    </Menu.Item>
    <Menu.Item>
      <HashLink to="#">Day Care/Hostel</HashLink>
    </Menu.Item>
    <Menu.Item>
      <HashLink to="#">Auditorium</HashLink>
    </Menu.Item>
    <Menu.Item>
      <HashLink to="#">Infirmary</HashLink>
    </Menu.Item>
  </Menu>
);

class NavBar extends Component {
  // constructor(props) {
  //   super(props);
  //   this.state = {
  //     isHide:true
  //   };
  //   this.hideBar = this.hideBar.bind(this);
  // }
  //
  // hideBar(){
  //    let {isHide} = this.state
  //    window.scrollY > 150 ?
  //    isHide && this.setState({isHide:false})
  //    :
  //    !isHide && this.setState({isHide:true})
  // }
  //
  // componentDidMount(){
  //     window.addEventListener('scroll',this.hideBar);
  // }
  //
  // componentWillUnmount(){
  //      window.removeEventListener('scroll',this.hideBar);
  // }

  render() {
    // let classHide = this.state.isHide ? "hide" : "show";
    return (
        <div className="navbar-main">
        <Navbar
          brand={
            <div>
              <img
                src={GRSlogo}
                alt="GRS"
                className="nav-logo" />
              <p className="nav-description-up">
                "Raising The Next Generation"
              </p>
              <h3 className="nav-description">
                Godawari Residential School
              </h3>
              <p className="nav-description-down">
                "Managed by Xavier Education System"
              </p>
            </div>
          }
          right>
          <NavItem><NavLink exact to='/' activeClassName="active-nav">Home</NavLink></NavItem>
          <Dropdown overlay={aboutUs}>
            <NavItem>
              <NavLink to='/about' activeClassName="active-nav">
                About Us <Icon type="down" />
              </NavLink>
            </NavItem>
          </Dropdown>
          <Dropdown overlay={admissions}>
            <NavItem>
              <NavLink exact to='/admission' activeClassName="active-nav">
                Admission <Icon type="down" />
              <span className="badge">OPEN</span>
              </NavLink>
            </NavItem>
          </Dropdown>
          {// <Dropdown overlay={programs}>
          //   <NavItem>
          //     <NavLink exact to='#' activeClassName="active-nav">
          //     Programs <Icon type="down" />
          //     </NavLink>
          //   </NavItem>
          // </Dropdown>
          // <Dropdown overlay={facitities}>
          //   <NavItem>
          //     <NavLink exact to='#' activeClassName="active-nav">
          //     Facitities <Icon type="down" />
          //     </NavLink>
          //   </NavItem>
          // </Dropdown>
          }
          <NavItem>
            <NavLink exact to='/contact' activeClassName="active-nav">
            Contact
            </NavLink>
          </NavItem>
          <NavItem><NavLink exact to='/authentication/login/' activeClassName="active-nav" className="contact-btn" id="contact-btn-mobile">Login</NavLink></NavItem>
        </Navbar>
      </div>
    );
  }
}

export default NavBar;
