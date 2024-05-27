import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import classes from "./styles.module.scss";
import { setPageTitle } from "../../utils";
import { login } from "../../store/actions/auth/authActions";


export default function Login({ history }) {
  const auth = useSelector((state) => state.auth);
  const dispatch = useDispatch();

  const [creds, setCreds] = useState({
    username: "",
    password: "",
  });

  const submitHandler = (e) => {
    e.preventDefault();

    dispatch(login(creds, history));
  };

  function handleChange({ target }) {
    const { name, value } = target;
    setCreds((prev) => ({
      ...prev,
      [name]: value,
    }));
  }

  useEffect(() => {
    setPageTitle("Login");
  }, []);

  return (
    <div className={classes.Login}>
      <div className={classes.Login__wrapper}>
        <form onSubmit={submitHandler} className={classes.Login__wrapper__content}>
            <h1>USER LOGIN</h1>

            <input
              placeholder="Email ID"
              type="text"
              name="username"
              id="username"
              value={creds.username}
              onChange={handleChange}
            />
            <input
              placeholder="Password"
              type="password"
              name="password"
              id="password"
              value={creds.password}
              onChange={handleChange}
            />
            <button disabled={auth.loading}>
              {auth.loading ? "Please wait..." : "Login"}
            </button>
            {auth.loginErrors?.error && (
              <div className={classes.Login__err}>
                <span>{auth.loginErrors.error}</span>
              </div>
            )}
        </form>
      </div>
    </div>
  );
}
