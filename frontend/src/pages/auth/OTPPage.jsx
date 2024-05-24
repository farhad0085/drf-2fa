import React, { useState } from 'react'
import classes from "./authStyles.module.scss";
import { useDispatch, useSelector } from "react-redux";
import { submitOtpCode } from "../../store/actions/auth/authActions";


const OTPPage = ({ history }) => {
  const dispatch = useDispatch();
  const auth = useSelector((state) => state.auth);

  const [otpCode, setOTPCode] = useState('');
  const { username, password } = history.location.state

  const submitHandler = (e) => {
    e.preventDefault();

    dispatch(submitOtpCode({
      "otp_key": otpCode,
      "username": username,
      "password": password
    }, history));
  };

  return (
    <div className={classes.Login}>
      <div className={classes.Login__wrapper}>
        <form onSubmit={submitHandler} className={classes.Login__wrapper__content}>
          <h1>OTP Required</h1>

          <input
            type='number'
            value={otpCode}
            onChange={e => setOTPCode(e.target.value)}
          />
          <button disabled={auth.loading}>
            {auth.loading ? "Please wait..." : "SUBMIT"}
          </button>
        </form>
      </div>
    </div>
  )

}


export default OTPPage
