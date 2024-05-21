import React from 'react'
import ScaleLoader from 'react-spinners/ScaleLoader'
import classes from './styles.module.scss'


const FullScreenLoading = () => {

  return (
    <div className={classes.loader_container}>
      <ScaleLoader color={"#33357B"} />
    </div>
  )

}

export default FullScreenLoading