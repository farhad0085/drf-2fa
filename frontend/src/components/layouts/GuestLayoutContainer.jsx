import React from "react";
import classes from "./styles.module.scss";
import GuestSidebar from "./GuestSidebar/GuestSidebar";
import { useSelector } from "react-redux";

const GuestLayoutContainer = ({ children, withLogo }) => {
  const isNightMode = useSelector((state) => state?.theme?.nightMode);

  return (
    <div
      className={`${classes.dashboard} ${
        isNightMode && classes.dashboard_nightMode
      }`}
    >
      <div className={classes.dashboard_main} id="dashboard">
        <div className={classes.dashboard_main_top}>{children}</div>
      </div>

      <GuestSidebar />
    </div>
  );
};

export default GuestLayoutContainer;
