import React, { StrictMode } from "react";
import ReactDOM from "react-dom";
import { BrowserRouter } from "react-router-dom";
import App from "./App";
import store from "./store";
import { Provider } from "react-redux";
import { loadUserInfo } from "./store/actions/auth/authActions";
import "./styles/style.scss";

const userToken = localStorage.getItem(process.env.REACT_APP_TOKEN_KEY);
if (userToken) {
  store.dispatch(loadUserInfo());
}


ReactDOM.render(
  <StrictMode>
    <Provider store={store}>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </Provider>
  </StrictMode>,
  document.getElementById("root")
);
