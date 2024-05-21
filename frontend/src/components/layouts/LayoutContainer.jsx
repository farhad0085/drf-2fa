import React from "react";
import classes from "./styles.module.scss";

const LayoutContainer = ({ children }) => {

  return (
    <div className={classes.dashboard}>
      <div className={classes.dashboard_main}>
        <div className={classes.dashboard_main_top}>{children}</div>
      </div>
    </div>
  );
};

export default LayoutContainer;
