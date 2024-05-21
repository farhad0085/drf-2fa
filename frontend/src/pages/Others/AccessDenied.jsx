import React from "react";
import classes from "./styles.module.scss";
import { setPageTitle } from "../../utils";
import LayoutContainer from "../../components/layouts/LayoutContainer";

const AccessDenied = ({ history }) => {
  setPageTitle("Access denied");

  return (
    <LayoutContainer>
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
    </LayoutContainer>
  )
};

export default AccessDenied;
