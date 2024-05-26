import React, { useEffect, useState } from "react";
import classes from "./styles.module.scss";
import { setPageTitle } from "../../utils";
import { getAuthSecret } from "./apiService";


export default function SetupAuthenticator({ history }) {

  const [authSecretData, setAuthSecretData] = useState({})

  useEffect(() => {
    setPageTitle("Setup Authenticator App");

    getAuthSecret().then(res => {
      setAuthSecretData(res.data)
    })
  }, []);

  return (
    <div className={classes.wrapper}>
      <div className={classes.content}>
        <h3>OTP Secret:</h3>
        <p><strong>{authSecretData.auth_secret}</strong></p>
        <p>Enter it inside a 2FA app (Google Authenticator, Authy) or scan the QR code below.</p>
        <img src={`data:image/svg+xml;utf8,${encodeURIComponent(authSecretData.qr_code)}`} alt="SVG" />
      </div>
    </div>
  );
}
