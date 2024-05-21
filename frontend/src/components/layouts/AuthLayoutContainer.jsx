import React from "react";
import classes from "./styles.module.scss";
import logo from "../../assets/Assiduus_LogoSmall.png";
import logoNight from "../../assets/Assiduus_LogoSmallNight.png";
import nightIcon from "../../assets/images/sidebar/nightAuth.svg";
import lightIcon from "../../assets/images/sidebar/lightIcon.svg";
import { NIGHTMODE_TOGGLE } from "../../store/actions/actionTypes";
import { useSelector, useDispatch } from "react-redux";

const AuthLayoutContainer = ({ children }) => {
  const isNightMode = useSelector((state) => state?.theme?.nightMode);
  const dispatch = useDispatch();
  return (
    <>
      <div
        className={`${classes.authBody} ${
          isNightMode && classes.authBody_nightMode
        }`}
      >
        <div className={classes.whiteBG}>
          <div className={classes.headerContainer}>
            <div className={classes.logoContainer}>
              <a href="https://www.assiduusglobal.com/">
                <img
                  className={classes.siteLogo}
                  src={!isNightMode ? logo : logoNight}
                  alt=""
                />
              </a>
              <p style={{ color: isNightMode ? "#fff" : "#000" }}>
                Unified Dashboard for Cross-bord, multi-platform e-commerce
                insights
              </p>
            </div>
            <div className={classes.headerContainer_links}>
              <div
                className={classes.headerContainer_themeToggle}
                onClick={() => {
                  localStorage.setItem(
                    "theme",
                    localStorage.getItem("theme") === "dark" ? "light" : "dark"
                  );
                  dispatch({
                    type: NIGHTMODE_TOGGLE,
                    payload:
                      localStorage.getItem("theme") === "dark" ? true : false,
                  });
                }}
              >
                <img
                  src={isNightMode ? lightIcon : nightIcon}
                  alt="nightmode"
                />
              </div>
            </div>
          </div>
        </div>
        {children}
      </div>
    </>
  );
};

export default AuthLayoutContainer;
