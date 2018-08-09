import React, { Component } from 'react';
import { Route, Switch } from 'react-router-dom';

import Home from './pages/homepage/homepage.jsx';
import About from './pages/about/about.jsx';
import Admission from './pages/admission/admission.jsx';
import Contact from './pages/contact/contact.jsx';

class App extends Component {
  render() {
    return (
      <div className="App">
        <Switch>
          <Route exact path='/' component={Home} />
          <Route exact path='/about' component={About} />
          <Route exact path='/admission' component={Admission} />
          <Route exact path='/contact' component={Contact} />
        </Switch>
      </div>
    );
  }
}

export default App;
