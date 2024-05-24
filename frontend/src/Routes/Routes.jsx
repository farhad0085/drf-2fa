import React from "react";
import { Route, Switch } from "react-router-dom";
import * as URLS from "./urls";
import withSuspense from "../utils/withSuspense";
import PrivateRoute from "./PrivateRoute";
import GuestRoute from "./GuestRoute";


const LoginPage = React.lazy(() => import("../pages/auth/Login"));
const OTPPage = React.lazy(() => import("../pages/auth/OTPPage"));
const Dashboard = React.lazy(() => import("../pages/Dashboard/Dashboard"));
const NotFound = React.lazy(() => import("../pages/Others/NotFound"));
const AccessDenied = React.lazy(() => import("../pages/Others/AccessDenied"));


const Routes = () => {

  return (
    <Switch>
      <GuestRoute exact path={URLS.LOGIN_PAGE} component={withSuspense(LoginPage)} />
      <GuestRoute exact path={URLS.OTP_REQUIRED_PAGE} component={withSuspense(OTPPage)} />
      <PrivateRoute exact path={URLS.DASHBOARD} component={withSuspense(Dashboard)} />
      <Route exact path={URLS.ACCESS_DENIED_PAGE} component={withSuspense(AccessDenied)} />
      <PrivateRoute path={"/"} exact component={withSuspense(Dashboard)} />
      <Route component={withSuspense(NotFound)} />
    </Switch>
  );
};

export default Routes;
