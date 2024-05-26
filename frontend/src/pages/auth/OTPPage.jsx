import React, { useState } from 'react'
import classes from "./styles.module.scss";
import { useDispatch, useSelector } from "react-redux";
import { submitOtpCode } from "../../store/actions/auth/authActions";


const OTPPage = ({ history }) => {
  const dispatch = useDispatch();
  const auth = useSelector((state) => state.auth);

  const [otpCode, setOTPCode] = useState('');
  const { userId } = history.location.state

  const submitHandler = (e) => {
    e.preventDefault();

    dispatch(submitOtpCode({
      "otp_code": otpCode,
      "user_id": userId,
    }, history));
  };

  return (
    <div className={classes.Login}>
      <div className={classes.Login__wrapper}>
        <form onSubmit={submitHandler} className={classes.Login__wrapper__content}>
          <h1>OTP Required</h1>
          <small>
            We've just sent an OTP (One-Time Password) to your email address.
            Please check your inbox and enter the code here to proceed.
            If you haven't received the email yet, please check your spam folder!
          </small>

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
