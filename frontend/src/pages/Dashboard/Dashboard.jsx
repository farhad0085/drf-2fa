import React from "react";
import classes from "./styles.module.scss";
import { useDispatch, useSelector } from "react-redux";
import { logout } from "../../store/actions/auth/authActions";


export default function Dashboard({ history }) {
  const dispatch = useDispatch()
  const auth = useSelector((state) => state.auth);


  return (
    <div className={classes.dashboardWrapper}>
      <div className={classes.content}>
        <h2>Congratulations, {auth?.user?.first_name}!</h2>
        <p>You've passed 2 Factor Authentication Successfully</p>
      </div>
      <div>
        <button
          onClick={() => dispatch(logout(history))}
          className={classes.logoutButton}
        >
          Logout
        </button>
      </div>
    </div>
  );
}
