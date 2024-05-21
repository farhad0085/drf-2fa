import React from "react";
import { Route, Switch } from "react-router-dom";
import * as URLS from "./urls";
import withSuspense from "../utils/withSuspense";

import PrivateRoute from "./PrivateRoute";
import GuestRoute from "./GuestRoute";

// Auth
const LoginPage = React.lazy(() => import("../pages/auth/Login"));

// Dashboard
const Dashboard = React.lazy(() => import("../pages/Dashboard/Dashboard"));

// Others
const NotFound = React.lazy(() => import("../pages/Others/NotFound"));
const AccessDenied = React.lazy(() => import("../pages/Others/AccessDenied"));


const Routes = () => {

  return (
    <Switch>
      {/* Auth */}
      <GuestRoute
        exact
        path={URLS.LOGIN_PAGE}
        component={withSuspense(LoginPage)}
      />
      
      {/* Dashboard */}
      <PrivateRoute
        path={URLS.DASHBOARD}
        exact
        component={withSuspense(Dashboard)}
      />
      
      <Route
        exact
        path={URLS.ACCESS_DENIED_PAGE}
        component={withSuspense(AccessDenied)}
      />
      <PrivateRoute path={"/"} exact component={withSuspense(Dashboard)} />

      <Route component={withSuspense(NotFound)} />
    </Switch>
  );
};

export default Routes;
