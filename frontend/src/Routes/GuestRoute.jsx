import React from 'react'
import { useSelector } from 'react-redux'
import { Route, Redirect } from 'react-router-dom'

const GuestRoute = ({ component: Component, ...rest }) => {
  const auth = useSelector((state) => state.auth);

  return (
    <Route
      {...rest}
      render={(props) => (
        <>
          {!auth.isAuthenticated ? (
            <Component {...props} />
          ) : (
            <Redirect
              to={{
                pathname: "/",
                search: props.location.search,
                state: {
                  from: props.location,
                  search: props.location.search
                },
              }}
            />
          )}
        </>
      )}
    />
  );
};


export default GuestRoute