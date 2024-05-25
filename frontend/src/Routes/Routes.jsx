import React from "react";
import { Route, Switch } from "react-router-dom";
import * as URLS from "./urls";
import PrivateRoute from "./PrivateRoute";
import GuestRoute from "./GuestRoute";

import LoginPage from "../pages/auth/Login";
import OTPPage from "../pages/auth/OTPPage";
import Dashboard from "../pages/Dashboard/Dashboard";
import NotFound from "../pages/Others/NotFound";
import AccessDenied from "../pages/Others/AccessDenied";


const Routes = () => {
  return (
    <Switch>
      <GuestRoute exact path={URLS.LOGIN_PAGE} component={LoginPage} />
      <GuestRoute exact path={URLS.OTP_REQUIRED_PAGE} component={OTPPage} />
      <PrivateRoute path={"/"} exact component={Dashboard} />
      <Route exact path={URLS.ACCESS_DENIED_PAGE} component={AccessDenied} />
      <Route component={NotFound} />
    </Switch>
  );
};

export default Routes;
