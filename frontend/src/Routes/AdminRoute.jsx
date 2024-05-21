import React from 'react'
import { Route, Redirect } from 'react-router-dom'
import { useSelector } from 'react-redux';
import queryString from 'query-string'
import { LOGIN_PAGE, ACCESS_DENIED_PAGE } from './urls';
import { isAdmin, isCompanyAdmin } from '../utils/authUtils';


const AdminRoute = ({ component: Component, ...rest }) => {
  const auth = useSelector((state) => state.auth);

  return (
    <Route
      {...rest}
      render={(props) => {

        const params = { ...queryString.parse(props.location.search), return_url: props.location?.pathname || "/" }

        return (
          <>
            {auth.isAuthenticated ? (
              <>
                {((isAdmin(auth.user) || isCompanyAdmin(auth.user)) || auth.loading) ? (
                  <Component {...props} />
                ) : (
                  <Redirect
                    to={{
                      pathname: ACCESS_DENIED_PAGE,
                      state: { from: props.location },
                    }}
                  />
                )}
              </>
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
        )
      }}
    />
  );

}


export default AdminRoute
