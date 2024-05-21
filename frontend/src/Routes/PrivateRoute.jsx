import React from "react";
import { useSelector } from "react-redux";
import { Route, Redirect } from "react-router-dom";
import queryString from "query-string";
import { LOGIN_PAGE } from "./urls";

const PrivateRoute = ({ component: Component, ...rest }) => {
  const auth = useSelector((state) => state.auth);

  return (
    <Route
      {...rest}
      render={(props) => {
        const params = {
          ...queryString.parse(props.location.search),
          return_url: props.location?.pathname || "/",
        };

        return (
          <>
            {auth.isAuthenticated ? (
              <Component {...props} />
            ) : (
              <Redirect
                to={{
                  pathname: LOGIN_PAGE,
                  search: queryString.stringify(params),
                  state: { from: props.location },
                }}
              />
            )}
          </>
        );
      }}
    />
  );
};

export default PrivateRoute;
