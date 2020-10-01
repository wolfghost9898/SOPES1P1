import React, { Component } from 'react';
import {BrowserRouter as Router, Route, Link, BrowserRouter, Redirect, Switch} from 'react-router-dom'
import './App.css';

import Home from './components/Home/Home'
import PageError from './components/Error/Error'
import NavBar from './components/NavBar/NavBar'
import Graficos from './components/Graficos/Graficos'

class App extends Component{
  render(){
    return(
      <BrowserRouter>
        <div>
          <NavBar/>
          <Switch>
            <Route
              exact
              path="/"
              component={Home}
            />
            <Route
              exact 
              path="/Graficos"
              component={Graficos}
            />
            <Route component={PageError}/>
          </Switch>
        </div>
      </BrowserRouter>
    );
  }
}

export default App;
