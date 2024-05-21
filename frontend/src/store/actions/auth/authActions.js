import { getHeaders } from "../../../utils";
import axios from "../../../utils/axios";
import * as Types from "../actionTypes";


export const login = (loginCreds, history) => (dispatch) => {
  dispatch({ type: Types.AUTH_LOADING });
  dispatch({ type: Types.USER_LOGIN_ERROR, payload: {} });

  const url = "/";

  axios
    .post("/auth/login/", loginCreds)
    .then((res) => {
      localStorage.setItem(process.env.REACT_APP_TOKEN_KEY, res.data.key);

      dispatch({ type: Types.USER_LOGGED_IN });
      history.push(url);
      dispatch(loadUserInfo());
    })
    .catch((error) => {
      dispatch({
        type: Types.USER_LOGIN_ERROR,
        payload: error.response ? error.response.data : {},
      });
    });
};

export const logout = (history) => (dispatch) => {
  dispatch({ type: Types.AUTH_LOADING });

  axios
    .post("/auth/logout/", {}, { headers: getHeaders() })
    .then((res) => {
      localStorage.removeItem(process.env.REACT_APP_TOKEN_KEY);

      dispatch({ type: Types.USER_LOGGED_OUT });
    })
    .catch((error) => {
      dispatch({
        type: Types.USER_LOGOUT_ERROR,
        payload: error.response ? error.response.data : {},
      });
    });
};

export const loadUserInfo = () => (dispatch) => {
  dispatch({ type: Types.AUTH_LOADING });
  axios
    .get("/auth/user/me/", { headers: getHeaders() })
    .then((res) => {
      if (res.data.should_logout) {
        dispatch(logout());
      }
      dispatch({ type: Types.USER_LOGGED_IN, payload: res.data });
    })
    .catch((error) => {
      //   console.log(error.response);
      localStorage.removeItem(process.env.REACT_APP_TOKEN_KEY);
      dispatch({ type: Types.USER_LOGGED_OUT });
    });
};
