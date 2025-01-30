import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import Login from './components/Login';
import Registration from './components/Registration';
import Recommendation from './components/Recommendation';
import ImageUpload from './components/ImageUpload';
import Chatbot from './components/Chatbot';
import Forum from './components/Forum';

const App = () => {
  return (
    <Router>
      <Switch>
        <Route path="/dashboard" component={Dashboard} />
        <Route path="/login" component={Login} />
        <Route path="/register" component={Registration} />
        <Route path="/recommendation" component={Recommendation} />
        <Route path="/image-upload" component={ImageUpload} />
        <Route path="/chatbot" component={Chatbot} />
        <Route path="/forum" component={Forum} />
      </Switch>
    </Router>
  );
}

export default App;
