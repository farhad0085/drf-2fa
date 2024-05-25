import React from "react";
import classes from "./styles.module.scss";
import { setPageTitle } from "../../utils";

const AccessDenied = ({ history }) => {
  setPageTitle("Access denied");

  return (
      <div
        className={classes.container}
      >
        <div className={classes.container_box}>
          <h1>Access denied</h1>
          <p className={classes.notAllowedText}>
            You're not allowed in this page!
          </p>
          <button onClick={() => history.push("/")}>Go Home</button>
        </div>
      </div>
  )
};

export default AccessDenied;
