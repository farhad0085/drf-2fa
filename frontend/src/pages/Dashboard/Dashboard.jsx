import React from "react";
import classes from "./styles.module.scss";
import LayoutContainer from "../../components/layouts/LayoutContainer";
import { useSelector } from "react-redux";


export default function Dashboard() {
  const auth = useSelector((state) => state.auth);


  return (
    <LayoutContainer>
      <div className={classes.dashboard}>
        <div className={classes.dashboard__header}>
          <div className={classes.dashboard__header__texts}>
            <h2>Welcome {auth?.user?.first_name}!</h2>
            <p>Here is the overview of your business</p>
          </div>
        </div>
      </div>
    </LayoutContainer>
  );
}
