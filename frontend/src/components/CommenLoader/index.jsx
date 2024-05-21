import React from "react";
import classes from "./styles.module.scss";

const CommenLoader = ({ width, height, size, style, borderWidth }) => {
  return (
    <div
      className={classes.wrapper}
      style={{ height: height || 330, width: width || "100%", ...style }}
    >
      <div
        className={classes.lds_ring}
        style={{
          width: `${size ? size + "px" : "80px"}`,
          height: `${size ? size + "px" : "80px"}`,
          borderWidth: `${borderWidth || "8px"}`,
        }}
      >
        <div
          style={{
            width: `${size ? size + "px" : "80px"}`,
            height: `${size ? size + "px" : "80px"}`,
            borderWidth: `${borderWidth || "8px"}`,
          }}
        ></div>
        <div
          style={{
            width: `${size ? size + "px" : "80px"}`,
            height: `${size ? size + "px" : "80px"}`,
            borderWidth: `${borderWidth || "8px"}`,
          }}
        ></div>
        <div
          style={{
            width: `${size ? size + "px" : "80px"}`,
            height: `${size ? size + "px" : "80px"}`,
            borderWidth: `${borderWidth || "8px"}`,
          }}
        ></div>
        <div
          style={{
            width: `${size ? size + "px" : "80px"}`,
            height: `${size ? size + "px" : "80px"}`,
            borderWidth: `${borderWidth || "8px"}`,
          }}
        ></div>
      </div>
    </div>
  );
};

export default CommenLoader;
