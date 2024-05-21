import * as Types from "../actions/actionTypes";

const initialState = {
  isAuthenticated: !!localStorage.getItem(process.env.REACT_APP_TOKEN_KEY),
  loginErrors: {},
  logoutErrors: {},
  loading: false,
  user: {},
};

function authReducer(state = initialState, action) {
  switch (action.type) {
    case Types.USER_LOGGED_IN: {
      return {
        ...state,
        loading: false,
        isAuthenticated: true,
        loginErrors: {},
        user: action.payload ? action.payload : { ...state.user },
      };
    }
    case Types.USER_LOGIN_ERROR: {
      return {
        ...state,
        loading: false,
        loginErrors: action.payload,
      };
    }
    case Types.AUTH_LOADING: {
      return {
        ...state,
        loading: true,
      };
    }
    case Types.USER_LOGGED_OUT: {
      return {
        ...state,
        loading: false,
        isAuthenticated: false,
      };
    }
    case Types.USER_LOGOUT_ERROR: {
      return {
        ...state,
        loading: false,
        logoutErrors: action.payload,
      };
    }
    default:
      return state;
  }
}

export default authReducer;
