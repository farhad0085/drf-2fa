import React from "react";
import classes from "./styles.module.scss";
import { setPageTitle } from "../../utils";

const NotFound = ({ history }) => {
  setPageTitle("Page not found");


  return (
    <div
      className={classes.container}
    >
      <div className={classes.container_box}>
        <h1>404 - Page not found</h1>
        <button onClick={() => history.push("/")}>Go Home</button>
      </div>
    </div>
  );
};

export default NotFound;
