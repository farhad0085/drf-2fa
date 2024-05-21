import { useEffect } from "react";
import classes from "./authStyles.module.scss";
import { setPageTitle } from "../../utils";

import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { login } from "../../store/actions/auth/authActions";


export default function Login({ history }) {
  const auth = useSelector((state) => state.auth);
  const dispatch = useDispatch();

  const [disable, setDisable] = useState(false);
  const [creds, setCreds] = useState({
    username: "",
    password: "",
  });

  const submitHandler = (e) => {
    e.preventDefault();
    setDisable(true);

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
            <button disabled={disable}>
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
