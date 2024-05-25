import { OTP_REQUIRED_PAGE } from "../../../Routes/urls";
import { getHeaders } from "../../../utils";
import axios from "../../../utils/axios";
import * as Types from "../actionTypes";


export const login = (loginCreds, history) => (dispatch) => {
  dispatch({ type: Types.AUTH_LOADING });
  dispatch({ type: Types.USER_LOGIN_ERROR, payload: {} });

  axios
    .post("/auth/login/", loginCreds)
    .then((res) => {
      localStorage.setItem(process.env.REACT_APP_TOKEN_KEY, res.data.key);

      dispatch({ type: Types.USER_LOGGED_IN });
      history.push("/");
      dispatch(loadUserInfo());
    })
    .catch((error) => {
      dispatch({
        type: Types.USER_LOGIN_ERROR,
        payload: error.response ? error.response.data : {},
      });
      const code = error.response?.data?.code
      if (code === "2FA_REQUIRED"){ // important
        history.push({
          pathname: OTP_REQUIRED_PAGE,
          state: loginCreds
        })
      }
    });
};

export const submitOtpCode = (otpData, history) => dispatch => {
  dispatch({ type: Types.AUTH_LOADING });
  dispatch({ type: Types.USER_LOGIN_ERROR, payload: {} });

  axios
    .post("/drf-2fa/verify-otp/", otpData)
    .then((res) => {
      localStorage.setItem(process.env.REACT_APP_TOKEN_KEY, res.data.api_token);

      dispatch({ type: Types.USER_LOGGED_IN });
      history.push("/");
      dispatch(loadUserInfo());
    })
    .catch((error) => {
      dispatch({
        type: Types.USER_LOGIN_ERROR,
        payload: error.response ? error.response.data : {},
      });
    });
}

export const logout = (history) => (dispatch) => {
    localStorage.removeItem(process.env.REACT_APP_TOKEN_KEY);
    dispatch({ type: Types.USER_LOGGED_OUT });
};

export const loadUserInfo = () => (dispatch) => {
  dispatch({ type: Types.AUTH_LOADING });
  axios
    .get("/auth/user/me/", { headers: getHeaders() })
    .then((res) => {
      dispatch({ type: Types.USER_LOGGED_IN, payload: res.data });
    })
    .catch((error) => {
      localStorage.removeItem(process.env.REACT_APP_TOKEN_KEY);
      dispatch({ type: Types.USER_LOGGED_OUT });
    });
};
