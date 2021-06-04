import React from 'react';
import ReactDOM from 'react-dom';
import LoginScreen from './pages/LoginScreen';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import DashboardScreen from './pages/DashboardScreen';


ReactDOM.render(
  <React.StrictMode>
    <Router>
      <Switch>
        <Route exact path='/' component={LoginScreen} />
        <Route exact path='/login' component={LoginScreen} />
        <Route path='/dashboard' component={DashboardScreen} />
      </Switch>
    </Router>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
